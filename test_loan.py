import pytest
from loan import app


@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get("/predict")
    assert resp.status_code == 200
    assert resp.json == {"message": "Prediction results will be displayed here."}
