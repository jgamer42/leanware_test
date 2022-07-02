from datetime import datetime
import pytest
from src.helpers import date as dateHelper

NoneType = type(None)


@pytest.mark.parametrize(
    "date,output",
    [
        ("05-05-2022", True),
        ("30-02-2022", False),
        ("ewqe", False),
        ("05/17/199", False),
    ],
)
def test_validate_date_format(date, output):
    assert dateHelper.validate_date_format(date) == output


@pytest.mark.parametrize(
    "date,output",
    [
        ("05-05-2022", "2022-05-05 00:00:00"),
    ],
)
def test_validate_date_format(date, output):
    assert dateHelper.get_valid_date_format(date) == output


@pytest.mark.parametrize(
    "date,output",
    [("2022-05-05 00:00:00", datetime), ("05-05-2022", NoneType)],
)
def test_get_timestamp_object(date, output):
    result = dateHelper.get_timestamp_object(date)
    assert type(result) == output
