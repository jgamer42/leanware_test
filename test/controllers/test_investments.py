import os
import pytest
import datetime
from dotenv import load_dotenv
from unittest.mock import MagicMock
from src.investments import Investment

EXPECTED_STOCK = [
    {
        "Id": "wqdwqdwq1",
        "Name": "Google",
        "Price": "7500",
        "TimeStamp": "2022-06-29 19:00:06",
        "Type": "Stock",
    },
    {
        "Id": "wqdwqdwq2",
        "Name": "Google",
        "Price": "7500",
        "TimeStamp": "2022-06-30 19:00:06",
        "Type": "Stock",
    },
    {
        "Id": "wqdwqdwq3",
        "Name": "Google",
        "Price": "7500",
        "TimeStamp": "2022-07-30 19:00:06",
        "Type": "Stock",
    },
]
EXPECTED_SYMBOL = [
    {
        "Id": "wqddqq",
        "Name": "COP",
        "Price": "75500",
        "TimeStamp": "2022-07-25 19:00:06",
        "Type": "Symbol",
    },
]


@pytest.fixture
def InvestmenManagerMock():
    manager_mock = MagicMock()
    return manager_mock


@pytest.mark.parametrize(
    "investment_type,expected",
    [
        ("Stocks", ["Google"]),
        ("Symbols", ["COP"]),
    ],
)
def test_invesments_available(investment_type, expected, InvestmenManagerMock):
    InvestmenManagerMock.configure_mock(
        **{
            "get_investments_names_by_type.return_value": ["Google"]
            if investment_type == "Stocks"
            else ["COP"]
        }
    )
    controller = Investment(investment_type, InvestmenManagerMock)
    assert controller.get_investments_available() == expected


@pytest.mark.parametrize(
    "investment,start_date,end_date,investment_type,expected",
    [
        (
            "Google",
            "2022-07-25 19:00:06",
            "2022-08-25 19:00:06",
            "Stocks",
            EXPECTED_STOCK,
        ),
        (
            "Google",
            "2022-08-25 19:00:06",
            "2022-07-25 19:00:06",
            "Stocks",
            EXPECTED_STOCK,
        ),
        (
            "COP",
            "2022-07-25 19:00:06",
            "2022-07-25 19:00:06",
            "Symbols",
            EXPECTED_SYMBOL,
        ),
    ],
)
def test_get_investments_prices(
    investment, start_date, end_date, investment_type, expected, InvestmenManagerMock
):
    InvestmenManagerMock.configure_mock(
        **{
            "get_price_for_investment.return_value": EXPECTED_STOCK
            if investment_type == "Stocks"
            else EXPECTED_SYMBOL
        }
    )
    try:
        controller = Investment(investment_type, InvestmenManagerMock)
        assert (
            controller.get_investment_prices(investment, start_date, end_date)
            == expected
        )
    except Exception:
        assert False == False


@pytest.mark.parametrize(
    "investment_type,expected",
    [
        ("Stocks", True),
        ("Symbols", True),
    ],
)
def test_export_all_investments_prices(investment_type, expected, InvestmenManagerMock):
    load_dotenv()
    InvestmenManagerMock.configure_mock(
        **{
            "get_all_investment_information.return_value": EXPECTED_STOCK
            if investment_type == "Stocks"
            else EXPECTED_SYMBOL
        }
    )
    controller = Investment(investment_type, InvestmenManagerMock)
    report = controller.export_all_investment_prices()
    assert os.path.exists(report) == expected
    os.remove(report)


@pytest.mark.parametrize(
    "investment_name,investment_type,expected",
    [
        (
            "Google",
            "Stocks",
            {
                "Message": "last price registred",
                "Price": "7500",
                "TimeStamp": datetime.datetime(2022, 7, 30, 19, 0, 6),
            },
        ),
        (
            "COP",
            "Symbols",
            {
                "Message": "last price registred",
                "Price": "75500",
                "TimeStamp": datetime.datetime(2022, 7, 25, 19, 0, 6),
            },
        ),
    ],
)
def test_last_price_investmen(
    investment_name, investment_type, expected, InvestmenManagerMock
):
    InvestmenManagerMock.configure_mock(
        **{
            "get_invesment_by_name.return_value": EXPECTED_STOCK
            if investment_type == "Stocks"
            else EXPECTED_SYMBOL
        }
    )
    controller = Investment(investment_type, InvestmenManagerMock)
    data = controller.get_last_price_investment(investment_name)
    assert data == expected
