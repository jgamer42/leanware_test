import os
import boto3
from boto3.dynamodb.conditions import Attr


class Traders(object):
    """
    Class used as a manager for Dynamo DB
    """

    def __init__(self, db=None):
        self.database_region = os.getenv("AWS_DYNAMO_DB_REGION")
        if db == None:
            self.resource = boto3.resource("dynamodb", region_name=self.database_region)
        else:
            self.resource = db
        self.traders = self.resource.Table(os.getenv("TRADERS_TABLE"))

    def get_user_information(self, trader_name):
        """
        Method to get the information for a user from the Traders table
        :param trader_name: Str with the name from the user to find
        :return dict: a with the user information
        """
        data = self.traders.scan(FilterExpression=Attr("UserName").eq(trader_name))
        if data.get("Items") != []:
            return data.get("Items")[0]
        else:
            return {"UserName": "", "Message": "Usser Doesn't exist"}

    def update_user_investments(self, new_investments, investment_type, trader_id):
        """
        Method to update the following investment from a trader
        :param new_investments: List with the new investments for the trader Ie: ['COP','USD']
        :param investment_type: Str with the type of investment to update Ie 'Symbols'
        :param trader_id: Str with the id for the trader
        :return:
        """
        try:
            output = self.traders.update_item(
                Key={"Id": trader_id},
                UpdateExpression=f"set {investment_type} = :new",
                ConditionExpression=f"attribute_exists({investment_type})",
                ExpressionAttributeValues={":new": new_investments},
                ReturnValues="UPDATED_NEW",
            )
            return output
        except Exception as E:
            return {"Message": "Usser Doesn't exist"}
