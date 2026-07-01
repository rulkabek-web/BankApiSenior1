class TestCreditRequest:

    def test_credit_request(self, api_manager, credit, credit_account_id):
        credit_request_response = api_manager.user_steps.credit_request(credit)
        transactions_response = api_manager.user_steps.transactions(credit_account_id)
        print("credit_request_response",credit_request_response)
        print("transactions_response",transactions_response)