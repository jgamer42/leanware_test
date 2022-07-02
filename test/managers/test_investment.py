import pytest
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
    assert set(data) == output


@pytest.mark.parametrize(
    "investment,type,start_date,end_date,output",
    [
        ("Google", "Stock", "2022-06-29 19:00:06", "2022-06-30 19:00:06", 3),
        ("Google", "Stock", "2022-06-30 19:00:06", None, 1),
        ("Amaazon", "Stock", "2022-07-29 19:00:06", None, 0),
        ("Amaazon", "Stock", "2022-06-29 19:00:05", None, 1),
        ("COP", "Symbol", "2022-06-25 19:00:06", None, 0),
    ],
)
def test_get_investment_price_timeframe(investment, type, start_date, end_date, output):
    a = InvestmentManager()
    data = a.get_price_for_investment(investment, start_date, end_date, type)
    assert len(data) == output
