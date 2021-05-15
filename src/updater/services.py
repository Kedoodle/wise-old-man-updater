import requests

from src.updater.config import BASE_URL, GROUP_ID, VERIFICATION_CODE


def get_groups_competitions(id):
    url = f'{BASE_URL}/groups/{id}/competitions'
    response = requests.get(url)
    return response if response.ok else None


def post_competitions_update_all(id):
    url = f'{BASE_URL}/competitions/{id}/update-all'
    body = {'verificationCode': VERIFICATION_CODE}
    response = requests.post(url, json=body)
    return response if response.ok else None
