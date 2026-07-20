import copy

import pytest

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_app_state():
    original_activities = copy.deepcopy(app_module.activities)
    yield
    app_module.activities = original_activities
