import pytest
from src.helpers import auth as authHelper


def test_token_generation():
    token = authHelper.generate_token("user1")
    assert True == authHelper.verify_token(token)
