import boto3
import datetime
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError


class Investment(object):
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
        self,
        investment,
        start_date,
        end_date=None,
        type="Stock",
    ):
        try:
            if end_date == None:
                aux_end_date = datetime.datetime.now()
                end_date = aux_end_date.strftime("%Y-%m-%d") + " 23:59:59"
            data = self.investments.scan(
                FilterExpression=Attr("TimeStamp").between(start_date, end_date)
                & Attr("Name").eq(investment)
                & Attr("Type").eq(type)
            )
            return data.get("Items")
        except ClientError:
            return []

    def get_all_investment_infomration(self, type="Stock"):
        data = self.investments.scan(FilterExpression=Attr("Type").eq(type))
        return data.get("Items")

    def get_invesment_by_name(self, name, type):
        data = self.investments.scan(
            FilterExpression=Attr("Type").eq(type) & Attr("Name").eq(name)
        )
        return data.get("Items")
