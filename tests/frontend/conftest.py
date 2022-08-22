import pytest
from core.browser import Chrome


@pytest.fixture()
def frontend():
    return Chrome()
