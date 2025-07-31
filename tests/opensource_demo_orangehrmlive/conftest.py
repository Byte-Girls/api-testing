import pytest
import config as conf

@pytest.fixture(scope="session")
def get_url():
    return conf.BASE_URI

@pytest.fixture(scope="session")
def get_token():
    return conf.TOKEN
