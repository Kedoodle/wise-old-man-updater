from src.updater.services import get_groups_members, post_competitions_update_all, post_players_track
from src.updater.helpers import filter_active_competitions, get_competition_ids, filter_outdated_players, \
    get_player_usernames


def run():
    players = get_groups_members().json()
    outdated_players = filter_outdated_players(players)
    usernames = get_player_usernames(outdated_players)
    print(f'Updating {len(usernames)} players...')
    for username in usernames:
        print(f'Updating player with username "{username}"')
        post_players_track(username)


if __name__ == '__main__':
    run()
