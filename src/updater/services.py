import requests

from src.updater.config import BASE_URL


def get_groups_competitions(group_id):
    url = f'{BASE_URL}/groups/{group_id}/competitions'
    response = requests.get(url)
    return response if response.ok else None
