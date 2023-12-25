import requests
from urllib.parse import urlencode

def verify_login():
    # Define the base URL
    base_url = "https://automationexercise.com/api/verifyLogin"

    # Define email and password
    email = "kamali9@gmail.com"
    password = "kamali5@Automation"

    # URL encode email and password
    encoded_email = urlencode({'email': email})[6:]
    encoded_password = urlencode({'password': password})[9:]
    breakpoint()
    # Combine the encoded form parameters
    encoded_params = f"email={encoded_email}&password={encoded_password}"

    # Make the HTTP POST request
    response = requests.post(f"{base_url}?{encoded_params}")

    # Parse the JSON response
    resbody = response.json()
    message_code = resbody.get("message")
    status = resbody.get("responseCode")

    # Set response details (adjust this based on your context or requirements)
    test_context.set_actual_response_code(status)
    test_context.set_actual_response_message(message_code)

# Assuming the TestRoutes class and test_context object are defined elsewhere in your code.
# You might need to adjust this part based on your actual implementation.
class TestRoutes:
    @staticmethod
    def verifyLoginEndpoint():
        # Implement the logic to return the base URL for the verifyLogin endpoint
        pass

# Create a placeholder for the test context
class TestContext:
    def __init__(self):
        self.actual_response_code = None
        self.actual_response_message = None

    def set_actual_response_code(self, code):
        self.actual_response_code = code

    def set_actual_response_message(self, message):
        self.actual_response_message = message

# Instantiate the test context
test_context = TestContext()

# Call the function to verify login
verify_login()

# Access the response details from the test context
print("Actual Response Code:", test_context.actual_response_code)
print("Actual Response Message:", test_context.actual_response_message)
