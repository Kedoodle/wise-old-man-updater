import unittest
from unittest.mock import Mock, patch

from src.updater.services import get_groups_competitions, post_competitions_update_all, get_groups_members


class TestGetGroupsCompetitions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._mock_get_patcher = patch('src.updater.services.requests.get')
        cls._mock_get = cls._mock_get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls._mock_get_patcher.stop()

    def test_when_response_is_ok(self):
        competitions = [{
            "id": 2887,
            "title": "Coffee House Construction Comp",
            "metric": "construction",
            "score": 260,
            "startsAt": "2021-05-15T00:00:00.000Z",
            "endsAt": "2021-05-22T00:00:00.000Z",
            "type": "classic",
            "groupId": 70,
            "createdAt": "2021-05-13T11:41:35.595Z",
            "updatedAt": "2021-05-15T06:00:02.165Z",
            "duration": "1 week",
            "participantCount": 95
        }]

        self._mock_get.return_value = Mock(status_code=200)
        self._mock_get.return_value.json.return_value = competitions

        response = get_groups_competitions()

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), competitions)

    def test_when_response_is_not_ok(self):
        self._mock_get.return_value.ok = False

        response = get_groups_competitions()

        self.assertIsNone(response)


class TestPostCompetitionsUpdateAll(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._mock_post_patcher = patch('src.updater.services.requests.post')
        cls._mock_post = cls._mock_post_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls._mock_post_patcher.stop()

    def test_when_response_is_ok(self):
        message = {
            "message": "2 outdated (updated < 60 mins ago) players are being updated. This can take up to a few minutes."
        }
        self._mock_post.return_value = Mock(status_code=200)
        self._mock_post.return_value.json.return_value = message

        response = post_competitions_update_all(Mock())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), message)

    def test_when_response_is_not_ok(self):
        self._mock_post.return_value.ok = False

        response = post_competitions_update_all(Mock())

        self.assertIsNone(response)


class TestGetGroupsMembers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._mock_get_patcher = patch('src.updater.services.requests.get')
        cls._mock_get = cls._mock_get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls._mock_get_patcher.stop()

    def test_when_response_is_ok(self):
        members = [{
            "exp": 287438551,
            "id": 3033,
            "username": "kedd",
            "displayName": "Kedd",
            "type": "regular",
            "build": "main",
            "country": "NZ",
            "flagged": False,
            "ehp": 1181.2346,
            "ehb": 67.81755,
            "ttm": 127.74393,
            "tt200m": 13781.21645,
            "lastImportedAt": "2021-05-27T12:34:58.883Z",
            "lastChangedAt": "2021-05-27T12:34:57.824Z",
            "registeredAt": "2020-05-02T22:38:09.634Z",
            "updatedAt": "2021-05-27T12:34:58.883Z",
            "role": "member",
            "joinedAt": "2020-06-28T21:10:06.636Z"
        }]

        self._mock_get.return_value = Mock(status_code=200)
        self._mock_get.return_value.json.return_value = members

        response = get_groups_members()

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), members)

    def test_when_response_is_not_ok(self):
        self._mock_get.return_value.ok = False

        response = get_groups_members()

        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
