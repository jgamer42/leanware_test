import boto3
from boto3.dynamodb.conditions import Attr


class Traders(object):
    def __init__(self):
        self.database_region = "us-east-1"
        self.client = boto3.client("dynamodb", region_name=self.database_region)
        resource = boto3.resource("dynamodb", region_name=self.database_region)
        self.traders = resource.Table("Traders")

    def get_user_information(self, trader_name):
        data = self.traders.scan(FilterExpression=Attr("UserName").eq(trader_name))
        if data.get("Items") != []:
            return data.get("Items")[0]
        else:
            return {"UserName": "", "message": "Usser Doesn't exist"}

    def update_user_investments(self, new_investments, investment_type, trader_id):
        self.traders.update_item(
            Key = {
                "Id":trader_id
            },
            UpdateExpression=f"set {investment_type} = :new",
            ExpressionAttributeValues= {
                ":new":new_investments
            },
            ReturnValues="UPDATED_NEW"
        )
