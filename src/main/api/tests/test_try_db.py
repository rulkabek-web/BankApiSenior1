import pytest
from sqlalchemy.orm import Session

from src.main.api.db.crud.account_crud import AccountCrudDb as Account
from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request_model import CreateUserRequest
from src.main.api.db.crud.user_crud import UserCrudDb as User


class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_try_create_user(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):

        create_user_response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_response.username == create_user_request.username

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, "Созданного пользователя нет в бд"

    def test_try_create_user_invalid(self, api_manager: ApiManager, db_session: Session):
        create_user_request = CreateUserRequest(
            username="G2",
            password="Pas!sw0rd",
            role="ROLE_USER"
        )
        create_user_response = api_manager.admin_steps.create_invalid_user(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert user_from_db is None, "пользователь создался, ошибка"

    def test_try_create_account(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        create_account_response = api_manager.user_steps.create_account(
            create_user_request)

        assert create_account_response.balance == 0

        account_from_db = Account.get_account_by_id(db_session, create_account_response.id)
        assert account_from_db.id == create_account_response.id, "Аккаунт не создан, аккаунта нет в бд"
        assert account_from_db.balance is not None, "поле баланс отсутсвует"