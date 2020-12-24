import asyncio
import aiohttp

FILE_NAME = 'myfile'
EXTENSION = 'jpg'


def save_on_disk(file, filename):
    with open(f'{filename}', 'wb') as photo:
        photo.write(file)


async def make_request(url, session, filename):
    async with session.get(url) as response:
        file = await response.content.read()
        save_on_disk(file, filename)
        return filename


async def make_requests(*urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, u in enumerate(urls):
            tasks.append(
                asyncio.create_task(make_request(u, session, f'{FILE_NAME}{i}.{EXTENSION}'))
            )
        result = await asyncio.gather(*tasks)
        print(result)


async def main():
    urls = ['https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg'] * 10
    await make_requests(*urls)


asyncio.run(main())
