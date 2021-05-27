import requests

from src.updater.config import BASE_URL, GROUP_ID, VERIFICATION_CODE


def get_groups_competitions(id: int = GROUP_ID) -> requests.Response:
    url = f'{BASE_URL}/groups/{id}/competitions'
    response = requests.get(url)
    return response if response.ok else None


def post_competitions_update_all(id: int) -> requests.Response:
    url = f'{BASE_URL}/competitions/{id}/update-all'
    body = {'verificationCode': VERIFICATION_CODE}
    response = requests.post(url, json=body)
    return response if response.ok else None


def get_groups_members(id: int = GROUP_ID) -> requests.Response:
    url = f'{BASE_URL}/groups/{id}/members'
    response = requests.get(url)
    return response if response.ok else None


def post_players_track(username: str) -> requests.Response:
    url = f'{BASE_URL}/players/track'
    body = {'username': username}
    response = requests.post(url, json=body)
    return response if response.ok else None
