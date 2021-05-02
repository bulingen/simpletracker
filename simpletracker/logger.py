import logging
from datetime import datetime


logger = logging.getLogger(__name__)


def log_pageview(page, visitor_id):
    now = datetime.utcnow().replace(microsecond=0)
    timestamp_string = "{}UTC".format(now)
    message = "{} {} {}".format(timestamp_string, page, visitor_id)
    logger.info(message)
