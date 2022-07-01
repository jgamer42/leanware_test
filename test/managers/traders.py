import sys
import pytest

sys.path.append("../..")
from src.managers.traders import Traders as TradersManager


@pytest.mark.parametrize(
    "trader_name,output",
    [("user1", "user1"), ("user2", "")],
)
def test_get_trader_information(trader_name, output):
    a = "a"
    data = a.get_user_information(trader_name)
    assert data.get("UserName") == output
