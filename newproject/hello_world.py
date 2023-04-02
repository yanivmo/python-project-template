from .config import settings


def get_hello():
    return settings.prompt.hello


def get_world():
    return settings.prompt.world
