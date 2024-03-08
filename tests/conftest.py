import pytest
from .setup_vertica_testing import SetupVerticaTesting

@pytest.fixture(scope="session", autouse=True)
def setup_before_tests():
    # Put your setup code here
    print("BEFORE TESTS")
    setup_vertica_testing = SetupVerticaTesting()
    setup_vertica_testing.setup()
    # This fixture will run before all tests and after all tests have completed
    # yield
    
    # Teardown code can also be placed here if necessary
    print("Teardown after running all tests")
    # For example, clean up resources