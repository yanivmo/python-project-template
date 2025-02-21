import asyncio
import os
import sys

from loguru import logger

from .config import settings
from .hello_world import get_hello, get_world


def configure_logging():
    as_json: bool = not sys.stderr.isatty() or settings.log.force_json

    format_colorized = "{level.icon} | <g>{time}</g> | <lvl>{message}</lvl> {extra}"
    format_not_colorized = "{level.icon} | {time} | {message} {extra}"

    # Remove the default sink
    logger.remove()

    logger.add(
        sink=sys.stderr,
        serialize=as_json,
        colorize=True,
        level=settings.log.level,
        format=format_not_colorized if as_json else format_colorized,
    )


async def main():
    configure_logging()

    with logger.contextualize(pid=os.getpid()):
        logger.info("Starting", cwd=os.getcwd())
        print(get_hello())
        await asyncio.sleep(1)
        print(get_world())
        logger.debug("Done")

    logger.warning("The following error is not real")
    logger.error("Something bad happened")


asyncio.run(main())
