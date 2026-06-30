from src.main.api.models.base_model import BaseModel
from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule


class CreditRequest(BaseModel):
    accountId: int
    amount:  Annotated[float,CreationRule(regex=r'^(?:(?:[5-9]\d{3}|1[0-4]\d{3})(?:\.\d{1,3})?|15000(?:\.0{1,3})?)$')]
    termMonths: Annotated[int,CreationRule(regex=r'^(?:[1-9]|1[0-2])$')]