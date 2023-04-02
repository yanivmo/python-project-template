from newproject.hello_world import get_hello, get_world


def test_hello():
    assert get_hello() == "Hello"


def test_world():
    assert get_world() == "World!!!"
