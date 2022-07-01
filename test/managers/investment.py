import sys
import pytest

sys.path.append("../..")
from src.managers.investments import Investment as InvestmentManager


@pytest.mark.parametrize(
    "type,output",
    [
        ("Stock", set(["Amaazon", "Google"])),
        ("Symbol", set(["USD", "COP"])),
    ],
)
def test_get_investments_available(type, output):
    a = InvestmentManager()
    data = a.get_investments_names_by_type(type)
    assert data == output


@pytest.mark.parametrize(
    "investment,type,start_date,end_date,output",
    [
        ("Google", "Stock", "29/06/2022 19:00:06", "30/06/2022 19:00:06", 3),
        ("Google", "Stock", "30/06/2022 19:00:06", None, 1),
        ("Amaazon", "Stock", "29/07/2022 19:00:06", None, 0),
        ("Amaazon", "Stock", "29/06/2022 19:00:05", None, 1),
        ("COP", "Symbol", "25/07/2022 19:00:06", None, 1),
    ],
)
def test_get_investment_price_timeframe(investment, type, start_date, end_date, output):
    a = InvestmentManager()
    data = a.get_price_for_investment(investment, start_date, type, end_date)
    assert len(data) == output
