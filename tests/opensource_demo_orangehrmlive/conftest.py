import pytest
import config as conf
import allure
from  src.orange_api.endpoint import OrangeEndpoints
from src.orange_api.resources_api import *
import logging

logging.basicConfig(level=logging.DEBUG)

# --- AUTHENTICATION ---
@pytest.fixture(scope="session")
def get_token():
    return conf.TOKEN

@pytest.fixture(scope="session")
def header():
    return {
        'Content-Type': 'application/json',
        'Authorization':f'{conf.TOKEN}'
    }

# --- RESOURCE URLs ---
@pytest.fixture(scope="session")
def get_url():
    return conf.BASE_URI

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
def employee_url():
    return f"{conf.BASE_URI}{OrangeEndpoints.EMPLOYEE.value}"

@pytest.fixture(scope="session")
def validation_username_url():
    return f"{conf.BASE_URI}{OrangeEndpoints.VALIDATION_USERNAME.value}"

# --- RESOURCE APIs ---
@pytest.fixture(scope="module")
def user_api(user_url, header):
    return UserAPI(user_url, header)

@pytest.fixture(scope="module")
def employee_api(employee_url, header):
    return EmployeeAPI(employee_url, header)

MARKERS_CATEGORIES = [
    "smoke",
    "regression",
    "funcional",
    "negativo",
    "positivo",
    "seguridad",
    "rendimiento",
    "valor_limite",
    "e2e",
]

def pytest_runtest_makereport(item, call):
    """Convierte los pytest.mark en categorías de Allure automáticamente"""
    for mark in item.iter_markers():
        if mark.name in MARKERS_CATEGORIES:
            allure.dynamic.label('category', mark.name)

            