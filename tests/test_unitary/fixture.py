import pytest
import server


@pytest.fixture
def competition_fixture():
    data = {
            "name": "test competition",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25",
            "clubsPlacesBooking": {}
    }
    server.competitions.append(data)


@pytest.fixture
def club_fixture():
    data = {
            "name": "test club",
            "email": "test@simplylift.com",
            "points": "30"
    }
    server.clubs.append(data)


@pytest.fixture
def club_fixture_2():
    data = {
            "name": "test club 2",
            "email": "test_2@simplylift.com",
            "points": "40"
    }
    server.clubs.append(data)
