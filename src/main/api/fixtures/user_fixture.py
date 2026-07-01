import pytest


from src.main.api.models.credit_request_model import CreditRequest
from src.main.api.models.transfer_request_model import TransferRequest
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
def account_id(api_manager, create_user_request):
    create_account = api_manager.user_steps.create_account(create_user_request)

    account_id = create_account.id
    response = {"create_user_request": create_user_request, "id": account_id }
    return response

@pytest.fixture
def another_account_id(api_manager, create_user_request):
    create_account = api_manager.user_steps.create_account(create_user_request)

    account_id = create_account.id
    response = {"create_user_request": create_user_request, "id": account_id }
    return response

@pytest.fixture
def deposit_requests(api_manager, account_id):
    deposit_request = RandomModelGenerator.generate(
        DepositRequest,
        accountId=account_id.get("id")
    )

    create_user_request = account_id.get("create_user_request")

    requests = {"create_user_request": create_user_request, "deposit_request": deposit_request}

    return requests

@pytest.fixture
def invalid_account_id(api_manager, create_user_request, create_another_user_request):
    account_id = api_manager.user_steps.create_account(create_user_request).id
    response = {"create_user_request": create_another_user_request, "id": account_id }

    return response

@pytest.fixture
def invalid_deposit_requests(api_manager, invalid_account_id):
    deposit_request = RandomModelGenerator.generate(
        DepositRequest,
        accountId=invalid_account_id.get("id")
    )

    create_user_request = invalid_account_id.get("create_user_request")

    requests = {"create_user_request": create_user_request, "deposit_request": deposit_request}

    return requests

@pytest.fixture
def transfer_requests(api_manager, deposit_requests, account_id, another_account_id):


    transfer_request = RandomModelGenerator.generate(
        TransferRequest,
        fromAccountId=account_id.get("id"),
        toAccountId=another_account_id.get("id")
    )

    deposit_request_before_transfer = RandomModelGenerator.generate(
        DepositRequest,
        accountId=account_id.get("id"),
        amount=9000
    )
    deposit_requests["deposit_request"] = deposit_request_before_transfer

    api_manager.user_steps.deposit(deposit_requests)
    api_manager.user_steps.deposit(deposit_requests)


    create_user_request = account_id.get("create_user_request")

    requests = {"create_user_request": create_user_request, "transfer_request": transfer_request}

    return requests

@pytest.fixture(params=[400, 11000])
def invalid_transfer_requests(api_manager, deposit_requests, account_id, another_account_id, request):


    transfer_request = TransferRequest(
        fromAccountId=account_id.get("id"),
        toAccountId=another_account_id.get("id"),
        amount=request.param
    )


    deposit_request_before_transfer = RandomModelGenerator.generate(
        DepositRequest,
        accountId=account_id.get("id"),
        amount=9000
    )
    deposit_requests["deposit_request"] = deposit_request_before_transfer

    api_manager.user_steps.deposit(deposit_requests)
    api_manager.user_steps.deposit(deposit_requests)


    create_user_request = account_id.get("create_user_request")

    requests = {"create_user_request": create_user_request, "transfer_request": transfer_request}

    return requests

@pytest.fixture
def create_credit_user_request(api_manager):
    credit_user_request = RandomModelGenerator.generate(
        CreateUserRequest,
        role="ROLE_CREDIT_SECRET"
    )
    api_manager.admin_steps.create_user(credit_user_request)

    return credit_user_request

@pytest.fixture
def credit_account_id(api_manager, create_credit_user_request):
    create_account = api_manager.user_steps.create_account(create_credit_user_request)

    account_id = create_account.id

    response = {"create_user_request": create_credit_user_request, "id": account_id }

    return response

@pytest.fixture
def credit(api_manager, credit_account_id):
    credit_request = RandomModelGenerator.generate(
        CreditRequest,
        accountId=credit_account_id.get("id")
    )

    create_user_request = credit_account_id.get("create_user_request")

    requests = {"create_user_request": create_user_request, "credit_request": credit_request}

    return requests