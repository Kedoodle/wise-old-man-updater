from datetime import datetime


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
