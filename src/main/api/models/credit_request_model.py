from src.main.api.models.base_model import BaseModel
from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule


class CreditRequest(BaseModel):
    accountId: int
    amount:  Annotated[float,CreationRule(min_int=5000, max_int=15000)]
    termMonths: Annotated[int,CreationRule(regex=r'^(?:[1-9]|1[0-2])$')]