import asyncio
from .hello_world import get_hello, get_world


async def main():
    print(get_hello())
    await asyncio.sleep(1)
    print(get_world())


asyncio.run(main())
