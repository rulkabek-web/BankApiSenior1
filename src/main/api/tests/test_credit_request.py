class TestCreditRequest:

    def test_credit_request(
            self,
            api_manager,
            credit,
            credit_account_id,
            transfer_requests):
        credit_request_response = api_manager.user_steps.credit_request(credit)
        transfer_response = api_manager.user_steps.transfer(transfer_requests)
        transactions_response = api_manager.user_steps.transactions(
            credit_account_id)

        # проверяем что баланс пополнился на сумму кредита
        assert transactions_response.balance == credit["credit_request"].amount

        for t in transactions_response.transactions:
            if t.toAccountId == transfer_requests.get(
                    "transfer_request").toAccountId:  # находим по id транзакцию на перевод
                # проверяем что сумма перевода совпадает
                assert t.amount == - \
                    transfer_requests.get("transfer_request").amount

    def test_invalid_credit_request(self, api_manager, credit):
        credit_request_response = api_manager.user_steps.credit_request(credit)
        # проверяем что не можем взять 2 кредит на аккаунт, получаем код 404
        # вместо 403:Уже есть активный кредит
        another_credit_request_response = api_manager.user_steps.invalid_credit_request(
            credit)
