import boto3
import pytest
from dotenv import load_dotenv
from moto import mock_dynamodb
from src.managers.investments import Investment as InvestmentManager

load_dotenv()
DATABASE_DATA = [
    {
        "Id": "dqdewd",
        "Name": "Amaazon",
        "Price": "7500",
        "TimeStamp": "2022-06-29 19:00:06",
        "Type": "Stock",
    },
    {
        "Id": "wqdwqdwq1",
        "Name": "Google",
        "Price": "7500",
        "TimeStamp": "2022-06-29 19:00:06",
        "Type": "Stock",
    },
    {
        "Id": "wqdwqdwq2",
        "Name": "Google",
        "Price": "7500",
        "TimeStamp": "2022-06-30 19:00:06",
        "Type": "Stock",
    },
    {
        "Id": "wqdwqdwq3",
        "Name": "Google",
        "Price": "7500",
        "TimeStamp": "2022-06-30 15:00:06",
        "Type": "Stock",
    },
    {
        "Id": "wqddqq",
        "Name": "COP",
        "Price": "7500",
        "TimeStamp": "2022-07-25 19:00:06",
        "Type": "Symbol",
    },
    {
        "Id": "wqddqDSADq",
        "Name": "USD",
        "Price": "7500",
        "TimeStamp": "2022-06-30 19:00:06",
        "Type": "Symbol",
    },
]
TABLE_DEFINITION = {
    "schema": [
        {"AttributeName": "Id", "KeyType": "HASH"},
        {"AttributeName": "Name", "KeyType": "RANGE"},
        {"AttributeName": "Price", "KeyType": "RANGE"},
        {"AttributeName": "TimeStamp", "KeyType": "RANGE"},
        {"AttributeName": "Type", "KeyType": "RANGE"},
    ],
    "attributes": [
        {"AttributeName": "Id", "AttributeType": "S"},
        {"AttributeName": "Name", "AttributeType": "S"},
        {"AttributeName": "Price", "AttributeType": "S"},
        {"AttributeName": "TimeStamp", "AttributeType": "S"},
        {"AttributeName": "Type", "AttributeType": "S"},
    ],
}


@pytest.mark.parametrize(
    "type,output",
    [
        ("Stock", set(["Amaazon", "Google"])),
        ("Symbol", set(["USD", "COP"])),
    ],
)
@mock_dynamodb
def test_get_investments_available(type, output):
    global DATABASE_DATA, TABLE_DEFINITION
    db = boto3.resource("dynamodb", region_name="us-east-1")

    table = db.create_table(
        TableName="Inversiones",
        KeySchema=TABLE_DEFINITION["schema"],
        AttributeDefinitions=TABLE_DEFINITION["attributes"],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    for item in DATABASE_DATA:
        table.put_item(Item=item)
    a = InvestmentManager(db)
    data = a.get_investments_names_by_type(type)
    assert set(data) == output


@pytest.mark.parametrize(
    "investment,type,start_date,end_date,output",
    [
        ("Google", "Stock", "2022-06-29 19:00:06", "2022-06-30 19:00:06", 3),
        ("Google", "Stock", "2022-06-30 19:00:06", None, 1),
        ("Amaazon", "Stock", "2022-07-29 19:00:06", None, 0),
        ("Amaazon", "Stock", "2022-06-29 19:00:05", None, 1),
        ("COP", "Symbol", "2022-06-25 19:00:06", None, 0),
    ],
)
@mock_dynamodb
def test_get_investment_price_timeframe(investment, type, start_date, end_date, output):
    global DATABASE_DATA, TABLE_DEFINITION
    db = boto3.resource("dynamodb", region_name="us-east-1")

    table = db.create_table(
        TableName="Inversiones",
        KeySchema=TABLE_DEFINITION["schema"],
        AttributeDefinitions=TABLE_DEFINITION["attributes"],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    for item in DATABASE_DATA:
        table.put_item(Item=item)
    a = InvestmentManager(db)
    data = a.get_price_for_investment(investment, start_date, end_date, type)
    assert len(data) == output
