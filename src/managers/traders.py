import boto3
from boto3.dynamodb.conditions import Attr


class Traders(object):
    """"""

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

    def update_user_investments(self, new_investments, product_to_update, trader_name):
        user_to_update = self.get_user_information(trader_name)
        if "message" in user_to_update.keys():
            return {}
        data_updated = self.traders.update_item(
            Key={"Id": user_to_update.get("Id")},
            UpdateExpression=f"SET {product_to_update}= :new_data",
            ExpressionAttributeValues={":new_data": new_investments},
            ReturnValues="UPDATED_NEW",
        )
        return data_updated
