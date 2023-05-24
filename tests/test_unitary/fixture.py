import pytest
import server


@pytest.fixture()
def competition_fixture():
        data = {
                "name": "test competition",
                "date": "2025-03-27 10:00:00",
                "numberOfPlaces": "25",
        }
        server.competitions.append(data)
        yield
        server.competitions.pop()


@pytest.fixture()
def club_fixture():
        data = {
                "name": "test club",
                "email": "test@simplylift.com",
                "points": "20"
        }
        server.clubs.append(data)
        yield
        server.clubs.pop()


@pytest.fixture()
def competition_fixture_2():
        data = {
                "name": "test competition 2",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25",
        }
        server.competitions.append(data)
        yield
        server.competitions.pop()


@pytest.fixture()
def club_fixture_2():
        data = {
                "name": "test club 2",
                "email": "test_2@simplylift.com",
                "points": "40"
        }
        server.clubs.append(data)
        yield
        server.clubs.pop()
