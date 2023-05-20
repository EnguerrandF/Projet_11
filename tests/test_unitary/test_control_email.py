import server
from .fixture import club_fixture, club_fixture_2, competition_fixture


def test_valid_email(club_fixture):
    response = server.app.test_client().post('/showSummary', data={"email": "test@simplylift.com"})
    assert response.status_code == 200


def test_invalid_email(club_fixture):
    response = server.app.test_client().post('/showSummary', data={"email": ""})
    assert response.status_code == 302
