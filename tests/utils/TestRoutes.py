class TestRoutes:
    def __init__(self):
        # Define properties with default values
        self._product_list_endpoint = "/api/productsList"
        self._brand_list_endpoint = "/api/brandsList"
        self._search_product_endpoint = "/api/searchProduct"
        self._verify_login_endpoint = "/api/verifyLogin"
        self._create_account_endpoint = "/api/createAccount"
        self._delete_account_endpoint = "/api/deleteAccount"
        self._update_account_endpoint = "/api/updateAccount"
        self._get_user_detail_by_email_endpoint = "/api/getUserDetailByEmail"

    @property
    def product_list_endpoint(self):
        return self._product_list_endpoint

    @property
    def brand_list_endpoint(self):
        return self._brand_list_endpoint

    @property
    def search_product_endpoint(self):
        return self._search_product_endpoint

    @property
    def verify_login_endpoint(self):
        return self._verify_login_endpoint

    @property
    def create_account_endpoint(self):
        return self._create_account_endpoint

    @property
    def delete_account_endpoint(self):
        return self._delete_account_endpoint

    @property
    def update_account_endpoint(self):
        return self._update_account_endpoint

    @property
    def get_user_detail_by_email_endpoint(self):
        return self._get_user_detail_by_email_endpoint

    def get_endpoint_by_partial_keyword(self, partial_keyword):
        # Search for the endpoint that contains the partial keyword
        for endpoint_name in dir(self):
            if (
                endpoint_name.endswith("_endpoint")
                and partial_keyword.lower() in endpoint_name.lower()
            ):
                return getattr(self, endpoint_name)
        return None


# Instantiate the TestRoutes class
test_routes = TestRoutes()

# Get the endpoint containing the partial keyword 'login'
login_related_endpoint = test_routes.get_endpoint_by_partial_keyword("login")

# Print the result
print("Login-related Endpoint:", login_related_endpoint)
