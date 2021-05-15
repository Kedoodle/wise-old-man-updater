from src.updater.services import get_groups_competitions, post_competitions_update_all
from src.updater.helpers import filter_active_competitions, get_competition_ids


def run():
    competitions = get_groups_competitions().json()
    active_competitions = filter_active_competitions(competitions)
    competition_ids = get_competition_ids(active_competitions)
    print(f'Updating {len(competition_ids)} competitions...')
    for competition_id in competition_ids:
        print(f'Updating competition with id {competition_id}')
        post_competitions_update_all(competition_id)


if __name__ == '__main__':
    run()
