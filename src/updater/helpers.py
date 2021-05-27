from datetime import datetime, timedelta


def filter_active_competitions(competitions: list) -> list[dict]:
    return [c for c in competitions if _is_active(c)]


def _is_active(competition: dict) -> bool:
    fmt = '%Y-%m-%dT%H:%M:%S.%fZ'
    start_time = datetime.strptime(competition['startsAt'], fmt)
    end_time = datetime.strptime(competition['endsAt'], fmt)
    return start_time <= _now() <= end_time


def _now() -> datetime:
    return datetime.utcnow()


def get_competition_ids(competitions: list) -> list[int]:
    return [c['id'] for c in competitions]


def filter_outdated_players(players: list) -> list[dict]:
    return [p for p in players if _is_player_outdated(p)]


def _is_player_outdated(player: dict) -> bool:
    fmt = '%Y-%m-%dT%H:%M:%S.%fZ'
    updated_at = datetime.strptime(player['updatedAt'], fmt)
    outdated_at = updated_at + timedelta(seconds=60)
    return _now() >= outdated_at


def get_player_usernames(players: list) -> list[str]:
    return [p['username'] for p in players]
