import pytest
import server


@pytest.fixture
def competition_fixture():
    data = {
            "name": "test competition",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
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
    yield


@pytest.fixture
def club_fixture_2():
    data = {
            "name": "test club 2",
            "email": "test_2@simplylift.com",
            "points": "40"
    }
    server.clubs.append(data)
    yield


def test_valid_place(competition_fixture, club_fixture):
    response = server.app.test_client().post('/purchasePlaces',
                                             data={"club": "test club",
                                                   "competition": "test competition",
                                                   "places": 5})

    data = response.data.decode()
    assert 'Great-booking complete!' in data
    assert response.status_code == 200


def test_invalid_place_club(competition_fixture, club_fixture):
    response = server.app.test_client().post('/purchasePlaces',
                                             data={"club": "test club",
                                                   "competition": "test competition",
                                                   "places": 35})

    data = response.data.decode()
    assert "Your selected place number is superior than 25" in data
    assert response.status_code == 200


def test_invalid_place_competition(competition_fixture, club_fixture_2):
    response = server.app.test_client().post('/purchasePlaces',
                                             data={"club": "test club 2",
                                                   "competition": "test competition",
                                                   "places": 35})

    data = response.data.decode()
    assert ("""The number of places selected is greater than the place of competition,
                you only have them 20""" in data)
    assert response.status_code == 200
