from .fixture import club_fixture, club_fixture_2, competition_fixture
import server


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


def test_place_more_of_12(competition_fixture, club_fixture_2):
    response = server.app.test_client().post('/purchasePlaces',
                                             data={"club": "test club 2",
                                                   "competition": "test competition",
                                                   "places": 13})

    data = response.data.decode()
    assert ("You cannot reserve more than 12 places for this tournament." in data)
    assert response.status_code == 200


def test_place_more_of_12_more_selection(competition_fixture, club_fixture_2):
    response = server.app.test_client().post('/purchasePlaces',
                                             data={"club": "test club 2",
                                                   "competition": "test competition",
                                                   "places": 5})
    assert 'Great-booking complete! 5 places' in response.data.decode()
    assert response.status_code == 200
    response_2 = server.app.test_client().post('/purchasePlaces',
                                               data={"club": "test club 2",
                                                     "competition": "test competition",
                                                     "places": 2})
    assert 'Great-booking complete! 2 places' in response_2.data.decode()
    assert response.status_code == 200
    response_3 = server.app.test_client().post('/purchasePlaces',
                                               data={"club": "test club 2",
                                                     "competition": "test competition",
                                                     "places": 10})
    data = response_3.data.decode()
    assert "You cannot buy more than 12 seats, you have left 5 for test club 2" in data
    assert response.status_code == 200
