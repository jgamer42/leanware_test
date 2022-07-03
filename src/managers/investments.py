import boto3
import datetime
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError


class Investment(object):
    """
    Class used as a manager for Dynamo DB
    """

    def __init__(self):
        self.database_region = "us-east-1"
        self.client = boto3.client("dynamodb", region_name=self.database_region)
        resource = boto3.resource("dynamodb", region_name=self.database_region)
        self.investments = resource.Table("Inversiones")

    def get_investments_names_by_type(self, type):
        """
        Method to get all available investment in the DB
        :param type: Str with the type of investment to find Ie Symbols
        :return list: List with the all investment for a type
        """
        data = self.investments.scan(
            FilterExpression=Attr("Type").eq(type),
        )
        return list(set([d.get("Name", "") for d in data.get("Items", [])]))

    def get_price_for_investment(
        self,
        investment,
        start_date,
        end_date=None,
        type="Stock",
    ):
        """
        Method to get all prices for a specific investment
        :param investment: Str with the investment name Ie COP
        :param start_date: Previously validated str with the start date with format YYY-mm-dd
        :param end_date: Previously validated str with the start date with format YYY-mm-dd by default has today date
        :param type: Str with the type of investment to find Ie 'Symbols' , by default uses Stock
        :return list: List with the all prices registred for a investment
        """
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

    def get_all_investment_information(self, type="Stock"):
        """
        Method to get all prices for all investments from one type
        :param type: Str with a type of investments to find
        :return list: List with the all prices registred for a type of investment
        """
        data = self.investments.scan(FilterExpression=Attr("Type").eq(type))
        return data.get("Items")

    def get_invesment_by_name(self, name, type):
        """
        Method to get all prices for an specific investment
        :param name: Str with a investment to find
        :param type: Str with a type of investments to find
        :return list: List with the all prices registred for a investment
        """
        data = self.investments.scan(
            FilterExpression=Attr("Type").eq(type) & Attr("Name").eq(name)
        )
        return data.get("Items")
