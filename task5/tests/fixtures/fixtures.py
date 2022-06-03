import pytest

# This is a demostration for Task 4 - item 3
@pytest.fixture(scope="session")
def files(request):
    values = request.config.getoption("--files")
    return values