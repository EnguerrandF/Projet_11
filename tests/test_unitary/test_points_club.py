import server
from .fixture import club_fixture, club_fixture_2


def test_list_points_clubs(club_fixture_2, club_fixture):
    response = server.app.test_client().get('/clubs')
    data = response.data.decode()

    data = response.data.decode()
    assert "test club : 30" in data
    assert "test club 2 : 40" in data
