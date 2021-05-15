import unittest
from unittest.mock import Mock, patch

from src.updater.services import get_groups_competitions


class TestGroups(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._mock_get_patcher = patch('src.updater.services.requests.get')
        cls._mock_get = cls._mock_get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls._mock_get_patcher.stop()

    def test_get_groups_competitions_when_response_is_ok(self):
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

        response = get_groups_competitions(Mock())

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), competitions)

    def test_get_groups_competitions_when_response_is_not_ok(self):
        self._mock_get.return_value.ok = False

        response = get_groups_competitions(Mock())

        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()