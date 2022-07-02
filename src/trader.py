import hashlib
import copy
from black import out
from numpy import product
from src.managers import Traders


class Trader(object):
    def __init__(self, username):
        self.username = username
        self.manager = Traders()
        self.user_information = self.get_user_info()

    def login(self, password):
        hasshed_password = hashlib.md5(password.encode())
        hasshed_password = hasshed_password.hexdigest()
        return self.user_information.get("Password") == hasshed_password

    def get_user_info(self):
        if not hasattr(self, "user_information"):
            self.user_information = self.manager.get_user_information(self.username)
        return self.user_information

    def get_follwing_investment(self, investment_type):
        return self.user_information.get(investment_type, [])

    def update_user_investment(self, investment_type, new_investments):
        self.user_information[investment_type] = new_investments
        output = copy.deepcopy(self.user_information)
        self.manager.update_user_investments(new_investments,investment_type,self.user_information.get("Id"))
        output.pop("Password")
        output["Stocks"] = list(output["Stocks"])
        output["Symbols"] = list(output["Symbols"])
        return output
