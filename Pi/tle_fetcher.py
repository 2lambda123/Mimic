import aiohttp
import asyncio

# Dictionary of satellite names and their corresponding TLE URLs
TLE_URLS = {
    "ISS": "https://www.celestrak.com/NORAD/elements/stations.txt",
    "TDRS 12": "https://www.celestrak.com/NORAD/elements/tdrss.txt",
    "TDRS 11": "https://www.celestrak.com/NORAD/elements/tdrss.txt",
    "TDRS 10": "https://www.celestrak.com/NORAD/elements/tdrss.txt",
    "TDRS 7": "https://www.celestrak.com/NORAD/elements/tdrss.txt",
    "TDRS 6": "https://www.celestrak.com/NORAD/elements/tdrss.txt",
}


async def fetch_tle(url):
    """
    Asynchronously fetches the TLE from the given URL using aiohttp.
    Args:
        url (str): The URL of the TLE to fetch.
    Returns:
        str: The TLE as a string.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            tle = await response.text()
            return tle

async def get_tles():
    """
    Asynchronously fetches the TLEs for all satellites in the TLE_URLS dictionary.

    Returns:
        dict: A dictionary containing the TLEs for all satellites, with satellite names as keys and TLE strings as values.
    """
    tles = {}
    tasks = []
    
    # Create a list of tasks to fetch the TLEs for all satellites in TLE_URLS
    for name, url in TLE_URLS.items():
        task = asyncio.create_task(fetch_tle(url))
        tasks.append(task)
    
    # Execute all tasks in parallel and wait for them to complete
    results = await asyncio.gather(*tasks)
    
    # Associate each TLE with its corresponding satellite name in a dictionary
    for i, name in enumerate(TLE_URLS.keys()):
        #snag ISS TLE from results
        if name == "ISS":
            lines = results[i].strip().split("\n")
            for j in range(len(lines)):
                if name in lines[j]:
                    tles[name] = "\n".join(lines[j:j+3])
                    break
        #snag relevant TDRS TLEs from results
        else:
            lines = results[i].strip().split("\n")
            for j in range(len(lines)):
                if name in lines[j]:
                    tles[name] = "\n".join(lines[j:j+3])
                    break

    #return all ISS and TDRS TLEs
    return tles

