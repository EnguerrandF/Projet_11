import server


def test_valid_email():
    response = server.app.test_client().post('/showSummary', data={"email": "john@simplylift.com"})
    assert response.status_code == 200


def test_invalid_email():
    response = server.app.test_client().post('/showSummary', data={"email": ""})
    assert response.status_code == 302