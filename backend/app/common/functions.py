import uuid
from datetime import datetime, timezone


def get_short_uuid():
    return str(uuid.uuid4())


def get_current_utc_time():
    return datetime.now(timezone.utc)