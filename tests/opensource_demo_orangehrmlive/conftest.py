import pytest
import config as conf
from  src.orange_api.endpoint import OrangeEndpoints

@pytest.fixture(scope="session")
def get_url():
    return conf.BASE_URI

@pytest.fixture(scope="session")
def get_token():
    return conf.TOKEN

@pytest.fixture(scope="session")
def header():
    return {
        'Content-Type': 'application/json',
        'Authorization':f'{conf.TOKEN}'
    }

@pytest.fixture(scope="session")
def category_url():
    return f"{conf.BASE_URI}{OrangeEndpoints.JOB_CATEGORIES.value}"

@pytest.fixture(scope="session")
def user_url():
    return f"{conf.BASE_URI}{OrangeEndpoints.USERS.value}"

@pytest.fixture(scope="session")
def statuses_url():
    return f"{conf.BASE_URI}{OrangeEndpoints.EMPLOYMENT_STATUSES.value}"

@pytest.fixture(scope="session")
def validation_username_url():
    return f"{conf.BASE_URI}{OrangeEndpoints.VALIDATION_USERNAME.value}"
