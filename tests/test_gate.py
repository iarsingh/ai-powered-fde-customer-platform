from fastapi.testclient import TestClient
from aifde.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'constraint': 'no egress', 'metric': 'under two minutes'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'constraint': 'no egress'}).json()
    assert bad["passed"] is False
    assert "metric" in bad["failed"]
