import unittest
from unittest.mock import Mock, patch

from src.updater.services import get_groups_members, post_players_track


class TestGetGroupsMembers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._mock_get_patcher = patch('src.updater.services.requests.get')
        cls._mock_get = cls._mock_get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls._mock_get_patcher.stop()

    def test_api_endpoint_is_called(self):
        group_id = Mock()

        get_groups_members(group_id)

        self._mock_get.assert_called_once_with(f"https://api.wiseoldman.net/groups/{group_id}/members")

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


class TestPostPlayersTrack(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._mock_post_patcher = patch('src.updater.services.requests.post')
        cls._mock_post = cls._mock_post_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls._mock_post_patcher.stop()

    def test_api_endpoint_is_called(self):
        username = Mock()

        post_players_track(username)

        self._mock_post.assert_called_once_with("https://api.wiseoldman.net/players/track", json={"username": username})

    def test_when_response_is_ok(self):
        player = {
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
            "lastImportedAt": "2021-05-27T14:15:15.929Z",
            "lastChangedAt": "2021-05-27T12:34:57.824Z",
            "registeredAt": "2020-05-02T22:38:09.634Z",
            "updatedAt": "2021-05-27T14:27:32.334Z",
            "combatLevel": 123,
            "latestSnapshot": {
                "createdAt": "2021-05-27T14:27:32.338Z",
                "importedAt": None,
                "overall": {
                    "rank": 22901,
                    "experience": 287438551,
                    "ehp": 1181.2346
                },
                "attack": {
                    "rank": 248931,
                    "experience": 10644366,
                    "ehp": 32.7519
                },
                "ehp": {
                    "rank": 11824,
                    "value": 1181.2346
                },
                "ehb": {
                    "rank": 45665,
                    "value": 67.81755
                }
            }
        }
        self._mock_post.return_value = Mock(status_code=200)
        self._mock_post.return_value.json.return_value = player

        response = post_players_track(Mock())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), player)

    def test_when_response_is_not_ok(self):
        self._mock_post.return_value.ok = False

        response = post_players_track(Mock())

        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
