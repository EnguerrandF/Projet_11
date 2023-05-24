import pytest
import server


@pytest.fixture(scope="class")
def competition_fixture_app():
    data = {
            "name": "test competition",
            "date": "2025-03-27 10:00:00",
            "numberOfPlaces": "25",
        }
    server.competitions.append(data)
    yield
    server.competitions.pop()

@pytest.fixture(scope="class")
def club_fixture_app():
    data = {
            "name": "test club",
            "email": "test@simplylift.com",
            "points": "30"
    }
    server.clubs.append(data)
    yield
    server.clubs.pop()
