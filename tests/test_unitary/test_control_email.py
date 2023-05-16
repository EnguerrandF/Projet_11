import server


def test_valid_email():
    response = server.app.test_client().post('/showSummary', data={"email": "john@simplylift.com"})
    assert response.status_code == 200


def test_invalid_email():
    response = server.app.test_client().post('/showSummary', data={"email": ""})
<<<<<<< HEAD
    assert response.status_code == 302
=======
    assert response.status_code == 302
>>>>>>> bug_#1_unknown_email
