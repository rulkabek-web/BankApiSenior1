class TestDeposit:

    def test_deposit(self,api_manager, deposit_requests):
        deposit_response = api_manager.user_steps.deposit(deposit_requests)

        assert deposit_requests.get("deposit_request").amount == deposit_response.balance

    def test_deposit_invalid(self,api_manager, invalid_deposit_requests):
        deposit_response = api_manager.user_steps.invalid_deposit(invalid_deposit_requests) # не можем депозитнуть другим юзером получаем 404 код
