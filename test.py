import asyncio
from datetime import datetime


def temp_block():
    for i in range(1000):
        print(i)


async def temp_nonblock():
    for i in range(1000):
        print(i)


if __name__ == '__main__':
    nb_start = datetime.now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(temp_nonblock())
    loop.close()
    nb_end = datetime.now()

    b_start = datetime.now()
    temp_block()
    b_end = datetime.now()

    print("nb:", nb_end - nb_start)
    print("b", b_end - b_start)
