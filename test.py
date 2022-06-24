import asyncio
from datetime import datetime


def temp_block():
    for i in range(1000):
        print(i)


async def temp_nonblock():
    for i in range(1000):
        print(i)


if __name__ == '__main__':
    temp = {'a': 15, 'c': 25, 'e': 55, 'b': 13}
    print(temp.items())
    print(sorted(temp.items(), key=lambda x: (-x[1], [0])))


