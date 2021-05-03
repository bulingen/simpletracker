import logging
from datetime import datetime
from django.utils import timezone
from .models import LogEntry


logger = logging.getLogger(__name__)


def log_pageview(page, visitor_id):
    utc_now = datetime.utcnow().replace(microsecond=0)
    timestamp_string = "{}UTC".format(utc_now)
    message = "{} {} {}".format(timestamp_string, page, visitor_id)
    logger.info(message)
    entry = LogEntry(created_at=timezone.now(),
                     visitor_id=visitor_id, page=page)
    entry.save()
