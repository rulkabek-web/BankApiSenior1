from typing import Optional

from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response_model import CreateAccountResponse

class CreateUserResponse(BaseModel):
    id: int
    username: str
    password: str
    role: str

