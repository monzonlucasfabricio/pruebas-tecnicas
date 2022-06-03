import pytest
from tests.fixtures.fixtures import *
from tests import *

def pytest_addoption(parser):
    
    parser.addoption(   "--files",
                        action = "store",
                        default = "1,2,3,4,5",
                        help = "Pass the number of test file you want to check"
                    )