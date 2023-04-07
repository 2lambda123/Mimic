import asyncio
import tle_fetcher

async def main():
    tles = await tle_fetcher.get_tles()
    for name, tle in tles.items():
        print(tle)

asyncio.run(main())

