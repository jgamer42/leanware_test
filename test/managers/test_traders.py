import pytest
from src.managers.traders import Traders as TradersManager


@pytest.mark.parametrize(
    "trader_name,output",
    [("user1", "user1"), ("user2", "")],
)
def test_get_trader_information(trader_name, output):
    a = TradersManager()
    data = a.get_user_information(trader_name)
    assert data.get("UserName") == output


@pytest.mark.parametrize(
    "new_investments,product_to_update,trader_name,output",
    [
        (["USD", "COP"], "Symbols", "user1", ["USD", "COP"]),
        (["Google"], "Stocks", "user1", ["Google"]),
        (["Google"], "Stocks", "user2", []),
    ],
)
def test_update_trader_investment(
    new_investments, product_to_update, trader_name, output
):
    a = TradersManager()
    data = a.update_user_investments(new_investments, product_to_update, trader_name)
    if "message" not in data.keys():
        assert "Attributes" in data.keys()
        assert data.get("Attributes").get(product_to_update) == output
    else:
        assert data.get("message") == "Usser Doesn't exist"
