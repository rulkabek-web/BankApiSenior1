import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request_model import CreateUserRequest

class TestCreateUser:

    def test_try_create_user(self, api_manager, create_user_request, create_another_user_request):

        create_user_response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_response.username == create_user_request.username

        create_another_user_response = api_manager.admin_steps.create_user(create_another_user_request)

        assert create_another_user_response.username == create_another_user_request.username

        #deposit_response = api_manager.admin_steps.deposit(create_user_request)
