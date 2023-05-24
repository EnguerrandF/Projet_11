import server
from .fixture import club_fixture, club_fixture_2
import pytest


@pytest.mark.usefixtures("club_fixture_2", "club_fixture")
def test_list_points_clubs():
    response = server.app.test_client().get('/clubs')
    data = response.data.decode()

    data = response.data.decode()
    assert "test club : 20" in data
    assert "test club 2 : 40" in data
