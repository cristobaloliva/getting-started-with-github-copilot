from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


_BASELINE_ACTIVITIES = deepcopy(activities)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange: ensure each test starts from the same in-memory dataset.
    activities.clear()
    activities.update(deepcopy(_BASELINE_ACTIVITIES))

    yield

    # Cleanup: restore baseline to avoid cross-test leakage.
    activities.clear()
    activities.update(deepcopy(_BASELINE_ACTIVITIES))
