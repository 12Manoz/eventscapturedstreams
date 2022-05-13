import logging
logger = logging.getLogger(__name__)


def handler(event, context):
    logger.info(event)
