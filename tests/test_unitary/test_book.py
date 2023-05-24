from .fixture import competition_fixture, competition_fixture_2, club_fixture
import server
import pytest


@pytest.mark.usefixtures("club_fixture", "competition_fixture")
def test_valid_date():
    response = server.app.test_client().get('/book/test competition/test club')
    data = response.data.decode()
    assert 'You cannot reserve seats, expired date.' not in data


@pytest.mark.usefixtures("competition_fixture_2", "club_fixture")
def test_invalid_date():
    response = server.app.test_client().get('/book/test competition 2/test club')
    data = response.data.decode()
    assert 'You cannot reserve seats, expired date.' in data
