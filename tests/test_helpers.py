import unittest
from datetime import datetime
from unittest.mock import patch

from src.updater.helpers import filter_active_competitions,get_competition_ids, filter_outdated_players, get_player_usernames


class TestFilterActiveCompetitions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._mock_now_patcher = patch('src.updater.helpers._now')
        cls._mock_now = cls._mock_now_patcher.start()
        cls._mock_now.return_value = datetime(2021, 5, 15, 10, 58, 52, 298766)

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


class TestFilterOutdatedPlayers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._mock_now_patcher = patch('src.updater.helpers._now')
        cls._mock_now = cls._mock_now_patcher.start()
        cls._mock_now.return_value = datetime(2021, 5, 27, 14, 41, 32, 709490)

    @classmethod
    def tearDownClass(cls):
        cls._mock_now_patcher.stop()

    def test_when_no_players(self):
        players = []

        outdated_players = filter_outdated_players(players)

        self.assertListEqual(outdated_players, [])

    def test_when_no_outdated_players(self):
        players = [
            {
                "username": "kedd",
                "updatedAt": "2021-05-27T14:41:00.000Z"
            },
            {
                "username": "alvx",
                "updatedAt": "2021-05-27T14:40:33.000Z"
            }
        ]

        outdated_players = filter_outdated_players(players)

        self.assertListEqual(outdated_players, [])

    def test_when_one_outdated_player(self):
        players = [
            {
                "username": "kedd",
                "updatedAt": "2021-05-27T14:40:00.000Z"
            },
            {
                "username": "alvx",
                "updatedAt": "2021-05-27T14:40:33.000Z"
            }
        ]

        outdated_players = filter_outdated_players(players)

        self.assertListEqual(outdated_players, [players[0]])

    def test_when_multiple_outdated_players(self):
        players = [
            {
                "username": "kedd",
                "updatedAt": "2021-05-27T14:40:00.000Z"
            },
            {
                "username": "alvx",
                "updatedAt": "2021-05-27T14:40:32.000Z"
            },
            {
                "username": "detredwings",
                "updatedAt": "2021-05-27T14:41:00.000Z"
            }
        ]

        outdated_players = filter_outdated_players(players)

        self.assertListEqual(outdated_players, players[:-1])


class TestGetPlayerUsernames(unittest.TestCase):
    def test_when_no_players(self):
        players = []

        usernames = get_player_usernames(players)

        self.assertListEqual(usernames, [])

    def test_when_one_player(self):
        players = [
            {
                "username": "kedd"
            }
        ]

        usernames = get_player_usernames(players)

        self.assertListEqual(usernames, ["kedd"])

    def test_when_multiple_players(self):
        players = [
            {
                "username": "kedd"
            },
            {
                "username": "alvx"
            }
        ]

        usernames = get_player_usernames(players)

        self.assertListEqual(usernames, ["kedd", "alvx"])


if __name__ == '__main__':
    unittest.main()
