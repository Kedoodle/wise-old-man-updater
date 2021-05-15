import unittest
from datetime import datetime
from unittest.mock import patch

from src.updater.helpers import filter_active_competitions, get_competition_ids


class TestFilterActiveCompetitions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._mock_now_patcher = patch('src.updater.helpers')
        cls._mock_now = cls._mock_now_patcher.start()
        cls._mock_now._now = datetime(2021, 5, 15, 10, 58, 52, 298766)

    @classmethod
    def tearDownClass(cls):
        cls._mock_now_patcher.stop()

    def test_when_no_competitions(self):
        competitions = []

        active_competitions = filter_active_competitions(competitions)

        self.assertListEqual(active_competitions, [])

    def test_when_no_active_competitions(self):
        competitions = [
            {
                "startsAt": "2021-05-08T00:00:00.000Z",
                "endsAt": "2021-05-15T00:00:00.000Z",
            },
            {
                "startsAt": "2021-05-01T00:00:00.000Z",
                "endsAt": "2021-05-08T00:00:00.000Z"
            }
        ]

        active_competitions = filter_active_competitions(competitions)

        self.assertListEqual(active_competitions, [])

    def test_when_one_active_competition(self):
        competitions = [
            {
                "startsAt": "2021-05-15T00:00:00.000Z",
                "endsAt": "2021-05-22T00:00:00.000Z",
            },
            {
                "startsAt": "2021-05-08T00:00:00.000Z",
                "endsAt": "2021-05-15T00:00:00.000Z",
            }
        ]

        active_competitions = filter_active_competitions(competitions)

        self.assertListEqual(active_competitions, [competitions[0]])

    def test_when_multiple_active_competitions(self):
        competitions = [
            {
                "startsAt": "2021-05-15T00:00:00.000Z",
                "endsAt": "2021-05-22T00:00:00.000Z",
            },
            {
                "startsAt": "2021-05-15T00:00:00.000Z",
                "endsAt": "2021-05-22T00:00:00.000Z",
            },
            {
                "startsAt": "2021-05-08T00:00:00.000Z",
                "endsAt": "2021-05-15T00:00:00.000Z",
            }
        ]

        active_competitions = filter_active_competitions(competitions)

        self.assertListEqual(active_competitions, competitions[:-1])


class TestGetCompetitionIds(unittest.TestCase):
    def test_when_no_competitions(self):
        competitions = []

        competition_ids = get_competition_ids(competitions)

        self.assertListEqual(competition_ids, [])

    def test_when_one_competition(self):
        competitions = [
            {
                "id": 2887
            }
        ]

        competition_ids = get_competition_ids(competitions)

        self.assertListEqual(competition_ids, [2887])

    def test_when_multiple_competitions(self):
        competitions = [
            {
                "id": 2887
            },
            {
                "id": 2788
            }
        ]

        competition_ids = get_competition_ids(competitions)

        self.assertListEqual(competition_ids, [2887, 2788])


if __name__ == '__main__':
    unittest.main()
