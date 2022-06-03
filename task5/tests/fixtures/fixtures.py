import pytest

@pytest.fixture(scope="session")
def files(request):
    values = request.config.getoption("--files")
    return values