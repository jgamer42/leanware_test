import boto3
import datetime
from boto3.dynamodb.conditions import Attr


class Investment(object):
    """"""

    def __init__(self):
        self.database_region = "us-east-1"
        self.client = boto3.client("dynamodb", region_name=self.database_region)
        resource = boto3.resource("dynamodb", region_name=self.database_region)
        self.investments = resource.Table("Inversiones")
        self.traders = resource.Table("Traders")

    def get_investments_names_by_type(self, type):
        data = self.investments.scan(
            FilterExpression=Attr("Type").eq(type),
        )
        return set([d.get("Name", "") for d in data.get("Items", [])])

    def get_price_for_investment(
        self, investment, start_date, type="Stock", end_date=None
    ):
        if end_date == None:
            end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = self.investments.scan(
            FilterExpression=Attr("TimeStamp").between(start_date, end_date)
            & Attr("Name").eq(investment)
            & Attr("Type").eq(type)
        )
        return data.get("Items")

    def get_all_investment_infomration(self, type="Stock"):
        data = self.investments.scan(FilterExpression=Attr("Type").eq(type))
        return data.get("Items")
