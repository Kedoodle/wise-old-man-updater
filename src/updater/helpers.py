from datetime import datetime, timedelta


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


def _now() -> datetime:
    return datetime.utcnow()