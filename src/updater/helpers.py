from datetime import datetime


def filter_active_competitions(competitions):
    return [c for c in competitions if _is_active(c)]


def _is_active(competition):
    fmt = '%Y-%m-%dT%H:%M:%S.%fZ'
    start_time = datetime.strptime(competition['startsAt'], fmt)
    end_time = datetime.strptime(competition['endsAt'], fmt)
    return start_time <= _now() <= end_time


def _now():
    return datetime.utcnow()


def get_competition_ids(competitions):
    return [c['id'] for c in competitions]
