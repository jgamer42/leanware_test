import boto3
import pytest
from dotenv import load_dotenv
from moto import mock_dynamodb
from src.managers.traders import Traders as TradersManager


load_dotenv()
DATABASE_DATA = [
    {
        "Id": "dqdewd",
        "UserName": "user1",
        "Stocks": ["Google"],
        "Symbols": ["USD", "COP"],
        "Password": "8d9d883a0eb4723e2f614b2c4240f7eb",
    },
]
TABLE_DEFINITION = {
    "schema": [
        {"AttributeName": "Id", "KeyType": "HASH"},
        {"AttributeName": "UserName", "KeyType": "RANGE"},
        {"AttributeName": "Stocks", "KeyType": "RANGE"},
        {"AttributeName": "Symbols", "KeyType": "RANGE"},
        {"AttributeName": "Password", "KeyType": "RANGE"},
    ],
    "attributes": [
        {"AttributeName": "Id", "AttributeType": "S"},
        {"AttributeName": "UserName", "AttributeType": "S"},
        {"AttributeName": "Stocks", "AttributeType": "L"},
        {"AttributeName": "Symbols", "AttributeType": "L"},
        {"AttributeName": "Password", "AttributeType": "S"},
    ],
}


@pytest.mark.parametrize(
    "trader_name,output",
    [("user1", "user1"), ("user2", "")],
)
@mock_dynamodb
def test_get_trader_information(trader_name, output):
    global DATABASE_DATA, TABLE_DEFINITION
    db = boto3.resource("dynamodb", region_name="us-east-1")

    table = db.create_table(
        TableName="Traders",
        KeySchema=TABLE_DEFINITION["schema"],
        AttributeDefinitions=TABLE_DEFINITION["attributes"],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    for item in DATABASE_DATA:
        table.put_item(Item=item)
    a = TradersManager(db)
    data = a.get_user_information(trader_name)
    assert data.get("UserName") == output


@pytest.mark.parametrize(
    "new_investments,product_to_update,trader_name,output",
    [
        (["USD", "COP"], "Symbols", "656516wd", ["USD", "COP"]),
        (["Google"], "Stocks", "656516wd", ["Google"]),
        (["Google"], "Stocks", "656516wdawd", []),
    ],
)
@mock_dynamodb
def test_update_trader_investment(
    new_investments, product_to_update, trader_name, output
):
    global DATABASE_DATA, TABLE_DEFINITION
    db = boto3.resource("dynamodb", region_name="us-east-1")

    table = db.create_table(
        TableName="Traders",
        KeySchema=TABLE_DEFINITION["schema"],
        AttributeDefinitions=TABLE_DEFINITION["attributes"],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    for item in DATABASE_DATA:
        table.put_item(Item=item)
    a = TradersManager(db)
    data = a.update_user_investments(new_investments, product_to_update, trader_name)
    if "message" not in data.keys():
        assert "Attributes" in data.keys()
        assert data.get("Attributes").get(product_to_update) == output
    else:
        assert data.get("message") == "Usser Doesn't exist"
