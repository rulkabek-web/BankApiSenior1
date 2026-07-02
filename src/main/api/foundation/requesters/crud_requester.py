from typing import Optional


import requests
from requests import Response

from src.main.api.configs.config import Config
from src.main.api.models.base_model import BaseModel
from src.main.api.foundation.http_requester import HttpRequester

class CrudRequester(HttpRequester):
    def post(self, model: Optional[BaseModel]) -> Response:
        body = model.model_dump() if model is not None else ""
        backend_url = Config.fetch('backendUrl')
        response = requests.post(
            url=f"{backend_url}{self.endpoint.value.url}",
            headers=self.request_spec,
            json=body
        )
        self.response_spec(response)
        return response

    def delete(self, user_id: int) -> Response:
        backend_url = Config.fetch('backendUrl')
        response = requests.delete(
            url=f"{backend_url}{self.endpoint.value.url}/{user_id}",
            headers=self.request_spec
        )
        self.response_spec(response)
        return response

    def get(self, account_id: Optional[int] = "") -> Response:
        backend_url = Config.fetch('backendUrl')
        response = requests.get(
            url=f"{backend_url}{self.endpoint.value.url}/{account_id}",
            headers=self.request_spec
        )
        self.response_spec(response)

        return response