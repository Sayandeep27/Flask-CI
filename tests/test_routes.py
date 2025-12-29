def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_add_route(client):
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.json["result"] == 5
