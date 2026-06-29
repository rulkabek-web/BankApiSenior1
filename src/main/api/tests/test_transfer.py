class TestCreateUser:

    def test_try_create_account(self,api_manager, create_user_request):
        create_account_response = api_manager.user_steps.create_account(create_user_request)
        print("1: ",create_account_response)
        create2_account_response = api_manager.user_steps.create_account(create_user_request)
        print("2: ",create2_account_response)
