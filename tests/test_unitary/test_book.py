from .fixture import competition_fixture, competition_fixture_2, club_fixture
import server


def test_valid_date(competition_fixture, club_fixture):
    response = server.app.test_client().get('/book/test competition/test club')
    data = response.data.decode()
    assert 'You cannot reserve seats, expired date.' not in data


def test_invalid_date(competition_fixture_2, club_fixture):
    response = server.app.test_client().get('/book/test competition 2/test club')
    data = response.data.decode()
    assert 'You cannot reserve seats, expired date.' in data
