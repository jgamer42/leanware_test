import hashlib
from src.managers import Traders


class Trader(object):
    def __init__(self, username):
        self.username = username
        self.traders_manager = Traders()
        self.user_information = self.get_user_info()

    def login(self, password):
        hasshed_password = hashlib.md5(password.encode())
        hasshed_password = hasshed_password.hexdigest()
        return self.user_information.get("Password") == hasshed_password

    def get_user_info(self):
        if not hasattr(self, "user_information"):
            self.user_information = self.traders_manager.get_user_information(
                self.username
            )
        return self.user_information
