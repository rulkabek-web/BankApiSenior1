from src.main.api.specs.request_specs import RequestSpecs

from foundation.endpoint import Endpoint
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.models.create_user_request_model import CreateUserRequest

class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        create_account_response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            response_spec=ResponseSpecs.request_created(),
            endpoint=Endpoint.CREATE_ACCOUNT
        ).post()
        return create_account_response
