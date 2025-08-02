import pytest
import config as conf

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
    return f"{conf.BASE_URI}/admin/job-categories"

@pytest.fixture(scope="session")
def user_url():
    return f"{conf.BASE_URI}/admin/users"

