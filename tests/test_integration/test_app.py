import server
from .fixture import club_fixture_app, competition_fixture_app
import pytest


@pytest.mark.usefixtures("competition_fixture_app", "club_fixture_app")
class TestApp:
    client = server.app.test_client()

    def test_get_index(self):
        response = self.client.get('/')
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data

    def test_connexion_club(self):
        response = self.client.post('/showSummary', data={"email": "test@simplylift.com"})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome, test@simplylift.com" in data
        assert "test club : 30 points" in data

    def test_clubs(self):
        response = self.client.get('/clubs')
        data = response.data.decode()
        assert response.status_code == 200
        assert "test club : 30 points" in data

    def test_book(self):
        response = self.client.get('/book/test competition/test club')
        data = response.data.decode()
        assert response.status_code == 200
        assert "test competition" in data
        assert "Places available: 25" in data

    def test_purchasePlaces(self):
        response = server.app.test_client().post('/purchasePlaces',
                                                 data={"club": "test club",
                                                       "competition": "test competition",
                                                       "places": 10})
        data = response.data.decode()
        assert response.status_code == 200
        assert "Points available: 20" in data
        assert "test club : 20 points" in data

    def test_logout(self):
        response = self.client.get('/logout', follow_redirects=True)
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data
