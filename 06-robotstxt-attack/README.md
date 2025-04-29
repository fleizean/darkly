# robots.txt Attack Explanation

Bu projede, bir web sunucusunda gizli dizinleri ve dosyaları ortaya çıkarmak için bir `robots.txt` saldırısı gerçekleştirdik. Saldırı betiği Python ile yazılmış olup, asenkron HTTP istekleri için `aiohttp` kütüphanesini kullanmaktadır. Ana hedef, dizin geçişi yaparak `robots.txt` dosyasını bulmaktı.

## Yapılan Adımlar

1. **Betik Çalıştırma**: [main.py](#file:main.py-context) dosyasında bulunan betiği çalıştırdık. Bu betik, dizinleri geçerek `robots.txt` dosyasına erişmeye çalışır.
2. **robots.txt Bulma**: `robots.txt` dosyası bulunduğunda, içeriği `success.html` dosyasına kaydedildi. Bu dosyanın içeriğini [success.html](#file:success.html-context) adresinde görebilirsiniz.
3. **Gizli Dizinlere Erişim**: `robots.txt` dosyası, `/whatever` ve `/.hidden` gibi gizli dizinleri ortaya çıkardı.
4. **.htpasswd İndirme**: Bu dizinlere giderek, şifrelenmiş kimlik bilgilerini içeren `.htpasswd` dosyasını indirdik. Bu dosyanın içeriğini [htpasswd](#file:htpasswd-context) adresinde görebilirsiniz.
5. **Şifreyi Çözme**: Çevrimiçi bir MD5 şifre çözme aracı (https://md5.gromweb.com/) kullanarak, `root` kullanıcısının hash'ini çözdük ve `qwerty123@` şifresini elde ettik.
6. **Yönetici Sayfasına Erişim**: `/admin/` sayfasına giderek, çözülen `qwerty123@` şifresini girdik ve erişim sağladık.

Bu süreç, dizin geçişi ve `robots.txt` dosyasının analizinin bir web sunucusunda hassas bilgileri nasıl ortaya çıkarabileceğini göstermektedir.

