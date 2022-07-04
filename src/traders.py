import hashlib
import copy
from src.managers import Traders


class Trader(object):
    """
    Class used as Trader controller
    also a trader works as User
    """

    def __init__(self, username, manager=None):
        self.username = username
        if manager == None:
            self.manager = Traders()
        else:
            self.manager = manager
        self.user_information = self.get_user_info()

    def login(self, password):
        """
        Method to validate the password from a trader
        :param password: Str with the user password
        :return bool: True is password id Ok
        """
        hasshed_password = hashlib.md5(password.encode())
        hasshed_password = hasshed_password.hexdigest()
        return self.user_information.get("Password") == hasshed_password

    def get_user_info(self):
        """
        Method to get trader information from the DB
        :return dict: A dict with the user information
        """
        if not hasattr(self, "user_information"):
            user_information = self.manager.get_user_information(self.username)
            if user_information and user_information.get("UserName") == self.username:
                self.user_information = user_information
            else:
                raise Exception("User Doesn't exists")
        return self.user_information

    def get_following_investment(self, investment_type):
        """
        Method to get which investments follows the trader
        :param investment_type: Str with the type of investment to get the info
        :return list: A list with the following investments
        """
        return self.user_information.get(investment_type, [])

    def update_user_investment(self, investment_type, new_investments):
        """
        Method to modify the following investments
        :param investment_type: Str with the investment type Ie Symbols
        :param new_investments: list with the investments to follow
        :retunr output: dict with the new user information
        """
        self.user_information[investment_type] = new_investments
        output = copy.deepcopy(self.user_information)
        self.manager.update_user_investments(
            new_investments, investment_type, self.user_information.get("Id")
        )
        output.pop("Password")
        output["Stocks"] = list(output["Stocks"])
        output["Symbols"] = list(output["Symbols"])
        return output
