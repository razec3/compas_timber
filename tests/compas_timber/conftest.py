from compas.tolerance import Tolerance
import pytest

@pytest.fixture(autouse=True)
def reset_tolerance():
    Tolerance().reset()