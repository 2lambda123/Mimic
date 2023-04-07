import aiohttp

ISS_TLE_URL = "https://www.celestrak.com/NORAD/elements/stations.txt"


async def fetch_iss_tle():
    async with aiohttp.ClientSession() as session:
        async with session.get(ISS_TLE_URL) as response:
            tle = await response.text()
            return tle


async def get_iss_tle():
    tle = await fetch_iss_tle()
    return tle.strip().split("\n")[:3]

