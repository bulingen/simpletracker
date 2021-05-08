import logging
from datetime import datetime
from django.utils import timezone, dateformat
from .models import LogEntry


logger = logging.getLogger(__name__)


def log_pageview(page, visitor_id):
    utc_now = datetime.utcnow()
    timestamp_string = "{}UTC".format(dateformat.format(
        utc_now, 'Y-m-d H:i'))
    message = "{} {} {}".format(timestamp_string, page, visitor_id)
    logger.info(message)
    entry = LogEntry(created_at=timezone.now(),
                     visitor_id=visitor_id, page=page)
    entry.save()
