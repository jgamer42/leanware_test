import hashlib
import pandas as pd
from src.managers import Investment as InvestmentManager
from src.helpers import date as dateHelper
import uuid
from operator import itemgetter


class Investment(object):
    """
    Class used as controller for investments
    """

    def __init__(self, type):
        self.type = type[:-1]
        self.manager = InvestmentManager()

    def get_investments_available(self):
        """
        Method to get all investments available for specific type
        :return list: List with all investments for a type Ie ["COP","USD"]
        """
        return self.manager.get_investments_names_by_type(self.type)

    def get_investment_prices(self, investment, start_date, end_date):
        """
        Method to get prices from a investment in a timeframe
        :param investmet: Str the name for the investment to retrieve the information
        :param start_date: Str the date to start the timeframe to find in format dd-mm-yyyy
        :param end_date: Str the date to end the timeframe to find in format dd-mm-yyyy
        :return list: List with all investments for a type Ie ["COP","USD"]
        """
        if dateHelper.validate_date_format(start_date):
            start_date = dateHelper.get_valid_date_format(start_date)
        else:
            raise Exception("Start of timeframe is wrong")

        if dateHelper.validate_date_format(end_date):
            end_date = dateHelper.get_valid_date_format(end_date)
        else:
            end_date = None
        output = self.manager.get_price_for_investment(
            investment, start_date, end_date, self.type
        )
        return output

    def export_all_investment_prices(self):
        """
        Method to retrieve and generate the report
        with the all investment prices for a specific investment type
        :return str: The path to the file with the information
        """
        output_file = hashlib.md5((self.type + str(uuid.uuid4)).encode()).hexdigest()
        data_to_export = self.manager.get_all_investment_information(self.type)
        dataframe = pd.DataFrame(data_to_export)
        dataframe.to_csv(
            f"/home/user/Escritorio/leanware_test/reports/{output_file}.csv"
        )
        return f"/home/user/Escritorio/leanware_test/reports/{output_file}.csv"

    def get_last_price_investment(self, investment_name):
        """
        Method to get the las prices registred for an insvestment
        :param investment_name: str with the investment to get data Ie COP
        :return dict: A dict with the information for the las prices from an investment
        """
        prices = self.manager.get_invesment_by_name(investment_name, self.type)
        if prices != []:
            for price in prices:
                price["TimeStamp"] = dateHelper.get_timestamp_object(
                    price.get("TimeStamp")
                )
            prices.sort(key=itemgetter("TimeStamp"))
            output = prices[-1]
            return {
                "message": "last price registred",
                "timeStamp": output.get("TimeStamp"),
                "prices": output.get("Price"),
            }
        else:
            return {"message": "not prices registred"}
