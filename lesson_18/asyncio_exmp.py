import asyncio


async def blocking_io(id):
    print(f'{id} Sarted')
    await asyncio.sleep(3)
    print(f'{id} Stopped')


async def main():
    t1 = asyncio.create_task(blocking_io(1))
    t2 = asyncio.create_task(blocking_io(2))
    t3 = asyncio.create_task(blocking_io(3))
    t4 = asyncio.create_task(blocking_io(4))
    r = await t1
    r1 = await t2
    r2 = await t2
    r3 = await t3
    print(r, r1, r2, r3)

asyncio.run(main(), debug=True)