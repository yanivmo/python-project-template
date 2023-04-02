import asyncio
import logging
import os
import sys

import structlog

from .config import settings
from .hello_world import get_hello, get_world

log = structlog.get_logger()


def configure_logging():
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=settings.log.level,
    )

    # These processors will be used in all cases
    shared_processors = [
        # If log level is too low, abort pipeline and throw away log entry
        structlog.stdlib.filter_by_level,
        # Add the name of the logger to event dict
        structlog.stdlib.add_logger_name,
        # Add log level to event dict
        structlog.processors.add_log_level,
        # If the "stack_info" key in the event dict is true, remove it and
        # render the current stack trace in the "stack" key
        structlog.processors.StackInfoRenderer(),
        # If the "exc_info" key in the event dict is either true or a
        # sys.exc_info() tuple, remove "exc_info" and render the exception
        # with traceback into the "exception" key
        structlog.dev.set_exc_info,
    ]

    if sys.stderr.isatty() and not settings.log.force_json:
        # Pretty printing when running in a terminal session
        processors = shared_processors + [
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.dev.ConsoleRenderer(),
        ]
    else:
        # Print JSON when not running in a terminal session; e.g., in a Docker container
        processors = shared_processors + [
            structlog.processors.TimeStamper(fmt=None, utc=True),
            # Log record main message/text will appear in "msg" attribute
            structlog.processors.EventRenamer("msg"),
            structlog.processors.JSONRenderer(),
        ]
    structlog.configure(
        processors,
        # `wrapper_class` is the bound logger that you get back from
        # get_logger(). This one imitates the API of `logging.Logger`.
        wrapper_class=structlog.stdlib.BoundLogger,
        # `logger_factory` is used to create wrapped loggers that are used for
        # OUTPUT. This one returns a `logging.Logger`. The final value (a JSON
        # string) from the final processor (`JSONRenderer`) will be passed to
        # the method of the same name as that you've called on the bound logger.
        logger_factory=structlog.stdlib.LoggerFactory(),
        # Effectively freeze configuration after creating the first bound
        # logger.
        cache_logger_on_first_use=True,
    )


async def main():
    configure_logging()

    log.info("Starting", cwd=os.getcwd())
    print(get_hello())
    await asyncio.sleep(1)
    print(get_world())
    log.debug("Done")


asyncio.run(main())
