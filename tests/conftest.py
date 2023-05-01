import pytest


# as we don't have access to the user data generation, we will use data of already existing user in our tests
@pytest.fixture()
def member_data():
    return {
        "position": "software engineer",
        "level": "sinior",
        "first_name": "Phillip",
        "last_name": "Jackson",
        "day_birth": 651792792,
        "hr_department": "UK(Head Office)",
        "email": "phillip.jackson@domain.com",
        "mobile": 3806795421782,
        "probation_period": 3,
        "ID": "025a626c4c9c"
    }
