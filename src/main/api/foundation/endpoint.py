from src.main.api.models.deposit_request_model import DepositRequest
from src.main.api.models.deposit_response_model import DepositResponse
from src.main.api.models.create_user_request_model import CreateUserRequest
from src.main.api.models.create_user_response_model import CreateUserResponse
from src.main.api.models.login_user_request_model import LoginUserRequest
from src.main.api.models.login_user_response_model import LoginUserResponse
from src.main.api.models.create_account_response_model import CreateAccountResponse
from src.main.api.models.transfer_request_model import TransferRequest
from src.main.api.models.transfer_response_model import TransferResponse
from src.main.api.models.transactions_response_model import TransactionsResponse
from src.main.api.models.credit_request_model import CreditRequest
from src.main.api.models.credit_response_model import CreditResponse

from src.main.api.models.base_model import BaseModel
from typing import Optional, Type
from dataclasses import dataclass
from enum import Enum

@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model=CreateUserRequest,
        response_model=CreateUserResponse,
        url="/admin/create"
    )
    LOGIN_USER = EndpointConfiguration(
        request_model=LoginUserRequest,
        response_model=LoginUserResponse,
        url="/auth/token/login"
    )
    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model=None,
        response_model=None,
        url="/admin/users"
    )
    CREATE_ACCOUNT = EndpointConfiguration(
        request_model=None,
        response_model=CreateAccountResponse,
        url="/account/create"
    )
    DEPOSIT = EndpointConfiguration(
        request_model=DepositRequest,
        response_model=DepositResponse,
        url="/account/deposit"
    )
    TRANSFER = EndpointConfiguration(
        request_model=TransferRequest,
        response_model=TransferResponse,
        url="/account/transfer"
    )
    TRANSACTIONS = EndpointConfiguration(
        request_model=None,
        response_model=TransactionsResponse,
        url="/account/transactions"
    )
    CREDIT_REQUEST = EndpointConfiguration(
        request_model=CreditRequest,
        response_model=CreditResponse,
        url="/credit/request"
    )