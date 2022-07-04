import os
import pytest
import time
from src.helpers import auth as authHelper


@pytest.mark.parametrize("sleep,output", [(10, True), (70, False)])
def test_token_generation(sleep, output):
    os.environ["TOKEN_LIFETIME"] = "60"
    token = authHelper.generate_token("user1")
    time.sleep(sleep)
    assert output == authHelper.verify_token(token)
