import pytest
from unittest.mock import MagicMock
from src.traders import Trader


@pytest.fixture
def TradersManagerMock():
    manager_mock = MagicMock()
    manager_mock.configure_mock(
        **{
            "get_user_information.return_value": {
                "Id": "wqewqe",
                "Password": "8d9d883a0eb4723e2f614b2c4240f7eb",
                "Stocks": ["Google"],
                "Symbols": ["USD", "COP"],
                "UserName": "user1",
            },
            "update_user_investment.return_value": ["COP", "USD"],
        }
    )
    return manager_mock


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("user1", "mi_clave12", True),
        ("user2", "", False),
        ("user2", "mi_clave12", False),
    ],
)
def test_login(username, password, expected, TradersManagerMock):
    try:
        controller = Trader(username, TradersManagerMock)
        assert controller.login(password) == expected
    except Exception as E:
        assert False == expected


@pytest.mark.parametrize(
    "investment_type,new_investments,username,expected",
    [
        (
            "Symbols",
            ["COP", "USD", "EU"],
            "user1",
            {
                "Id": "wqewqe",
                "Password": "8d9d883a0eb4723e2f614b2c4240f7eb",
                "Stocks": ["Google"],
                "Symbols": ["USD", "COP", "EU"],
                "UserName": "user1",
            },
        ),
        (
            "Stocks",
            ["Amazon"],
            "user1",
            {
                "Id": "wqewqe",
                "Password": "8d9d883a0eb4723e2f614b2c4240f7eb",
                "Stocks": ["Amazon"],
                "Symbols": ["USD", "COP"],
                "UserName": "user1",
            },
        ),
        (
            "Symbols",
            ["USD", "COP"],
            "user2",
            {
                "Id": "wqewqe",
                "Password": "8d9d883a0eb4723e2f614b2c4240f7eb",
                "Stocks": ["Google"],
                "Symbols": ["USD", "COP"],
                "UserName": "user1",
            },
        ),
    ],
)
def test_update_investment_(
    investment_type, new_investments, username, expected, TradersManagerMock
):
    try:
        controller = Trader(username, TradersManagerMock)
        data = controller.update_user_investment(new_investments, investment_type)

        assert data == expected
    except Exception as E:
        assert False == False


@pytest.mark.parametrize(
    "username,investment_type,expected",
    [
        ("user1", "Symbols", ["Google"]),
        ("user1", "Stocks", ["USD", "COP"]),
        ("user2", "Symbols", []),
    ],
)
def test_get_following_investment(
    username, investment_type, expected, TradersManagerMock
):
    try:
        controller = Trader(username, TradersManagerMock)
        data = controller.get_following_investment(investment_type)
        assert data == expected
    except Exception as E:
        assert False == False
