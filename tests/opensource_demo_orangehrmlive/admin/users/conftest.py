import pytest
import logging
from src.data_generators.user_data import *
from src.utils.fixture_helpers import create_and_cleanup

logger = logging.getLogger(__name__)

@pytest.fixture
def new_user(create_employee, user_api):
    new_user_data = generate_user_payload(emp_number=create_employee["empNumber"])
    yield from create_and_cleanup(user_api, new_user_data, id_key="id")

@pytest.fixture(scope="module")
def user(create_employee, user_api):
    new_user_data = generate_user_payload(emp_number=create_employee["empNumber"])
    yield from create_and_cleanup(user_api, new_user_data, id_key="id")

@pytest.fixture(scope="module")
def disabled_user(create_employee, user_api):
    new_user_data = generate_user_payload(emp_number=create_employee["empNumber"], status=False)
    yield from create_and_cleanup(user_api, new_user_data, id_key="id")

@pytest.fixture
def multiple_users(request, create_employee, user_api):
    num_users_to_create = request.param
    users = []
    for _ in range(num_users_to_create):
        new_user_data = generate_user_payload(emp_number=create_employee["empNumber"])
        response = user_api.create(new_user_data)
        assert response.status_code == 200
        users.append(response.json()["data"])
    yield users
    user_ids = [user["id"] for user in users]
    user_api.delete(payload={"ids": user_ids})

@pytest.fixture(scope="module")
def create_employee(employee_api):
    new_employee_data = generate_employee_payload()
    yield from create_and_cleanup(employee_api, new_employee_data, id_key="empNumber")

@pytest.fixture
def delete_all_users(user_api):
    response = user_api.get_all()
    users = response.json()["data"]
    # Note: El usuario con ID=1 es el admin y no se debe intentar eliminar, caso contrario lanza error.
    user_ids = [user["id"] for user in users if user["id"] != 1]
    user_api.delete(payload={"ids": user_ids})
    yield
    for user in users:
        user_api.create(user)

@pytest.fixture
def get_nth_user(request, user_api):
    position = request.param
    response = user_api.get_all()
    users = response.json()["data"]
    if len(users) >= position:
        return users[position]
    logger.info(f"Usuario {position} no encontrado")
    return None

