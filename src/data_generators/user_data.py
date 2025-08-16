from faker import Faker

fake = Faker()

def generate_user_payload(emp_number, status=True):
    return {
        "status": status,
        "password": fake.password(),
        "username": fake.user_name(),
        "userRoleId": 1,
        "empNumber": emp_number
    }

def generate_employee_payload():
    return {
        "lastName": fake.last_name(),
        "firstName": fake.first_name()
    }

