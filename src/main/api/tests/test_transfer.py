class TestCreateUser:

    def test_transfer(self, api_manager, transfer_requests, account_id):
        transfer_response = api_manager.user_steps.transfer(transfer_requests)
        assert transfer_response.fromAccountIdBalance == 18000 - \
            transfer_requests["transfer_request"].amount

        transactions_response = api_manager.user_steps.transactions(account_id)
        # id счета совпадает
        assert transactions_response.id == account_id.get("id")

        for t in transactions_response.transactions:
            # находим по id транзакцию на перевод
            if t.toAccountId == transfer_requests.get("transfer_request").toAccountId:
                # проверяем что сумма перевода совпадает
                assert t.amount == - transfer_requests.get("transfer_request").amount

    def test_invalid_transfer(self, api_manager, invalid_transfer_requests):
        # проверяем что не можем перевести меньше 500 или больше 10000
        api_manager.user_steps.invalid_transfer(invalid_transfer_requests)
