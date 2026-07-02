import pytest


class TestCreateUser:

    def test_transfer(self, api_manager, transfer_requests, account_id):
        transfer_response = api_manager.user_steps.transfer(transfer_requests)
        assert transfer_response.fromAccountIdBalance == 18000 - \
            transfer_requests["transfer_request"].amount

        transactions_response = api_manager.user_steps.transactions(account_id)

        assert transactions_response.id == account_id.get(
            "id")  # id счета совпадает
        for t in transactions_response.transactions:
            if t.toAccountId == transfer_requests.get(
                    "transfer_request").toAccountId:  # находим по id транзакцию на перевод
                # проверяем что сумма перевода совпадает
                assert t.amount == - \
                    transfer_requests.get("transfer_request").amount

    def test_invalid_transfer(self, api_manager, invalid_transfer_requests):
        api_manager.user_steps.invalid_transfer(invalid_transfer_requests)
