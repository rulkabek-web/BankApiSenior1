from src.main.api.models.base_model import BaseModel
from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule

class DepositRequest(BaseModel):
    accountId: int
    amount: Annotated[float,CreationRule(regex=r'^(?:[1-8]\d{3}(?:\.\d{1,3})?|9000(?:\.0{1,3})?)$')]