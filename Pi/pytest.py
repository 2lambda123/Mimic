import asyncio
import iss_tle

async def main():
    tle = await iss_tle.get_iss_tle()
    print(tle)

asyncio.run(main())

