import pytest

from src.main.api.models.deposit_request_model import DepositRequest
from src.main.api.models.create_user_request_model import CreateUserRequest
from src.main.api.generators.model_generator import RandomModelGenerator

@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)

    return user_request

@pytest.fixture
def create_another_user_request(api_manager):
    another_user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(another_user_request)

    return another_user_request

@pytest.fixture
def create_account_response(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)

@pytest.fixture
def deposit_request(api_manager, create_account_response):
    deposit_request = RandomModelGenerator.generate(DepositRequest)
    api_manager.user_steps.deposit(deposit_request)
    return deposit_request