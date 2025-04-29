# Directory Traversal Attack Explanation

Bu README, [main.py](#file:main.py-context) dosyasını kullanarak gerçekleştirilen dizin geçiş saldırısını açıklar. Bu saldırının amacı, sunucudaki `/etc/passwd` dosyasına erişmek ve bayrağı elde etmekti.

## Dosyalar

- **[main.py](#file:main.py-context)**: Dizin geçiş saldırısını gerçekleştiren ana betik.
- **[flag.txt](#file:flag.txt-context)**: Saldırıdan elde edilen bayrağı içerir.
- **[success.html](#file:success.html-context)**: Hedef dosyanın başarılı bir şekilde alınması durumunda oluşturulan HTML dosyası.

## Saldırı Açıklaması

### Amaç

Bu saldırının amacı, sunucudaki bir dizin geçiş zafiyetini kullanarak `/etc/passwd` dosyasına erişmekti. Bu dosya genellikle Unix tabanlı sistemlerde kullanıcı hesap bilgilerini içerir.

### Adımlar

1. **Kurulum**: Betik, asenkron HTTP istekleri gerçekleştirmek için `aiohttp` kütüphanesini kullanır.
2. **Geçiş Yolu**: Betik, hedef dosya bulunana kadar temel URL'ye `../` ekleyerek bir geçiş yolu oluşturur.
3. **İstek İşleme**: Oluşturulan her URL için sunucuya bir GET isteği gönderir.
4. **Yanıt Kontrolü**: Betik, yanıt içeriğinde "flag" kelimesinin varlığını kontrol eder. Eğer bulunursa, içeriği `success.html` dosyasına yazar.
5. **Yeniden Deneme Mekanizması**: Betik, aralıklı hataları ele almak için bir gecikme ile yeniden deneme mekanizması içerir.

### Çalıştırma

Betiği aşağıdaki komutla çalıştırın:

```sh
python main.py
```

Betik, `/etc/passwd` dosyasını başarıyla alana kadar URL'ye `../` eklemeye ve istek göndermeye devam edecektir.

## Bayrak

Saldırıdan elde edilen bayrak [flag.txt](#file:flag.txt-context) dosyasında saklanır:

```
b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
```

## Sonuç

Başarılı bir şekilde alındığında, `/etc/passwd` dosyasının içeriği [success.html](#file:success.html-context) dosyasına yazılır.

## Sonuç

Bu saldırı, sunucu tarafında kullanıcı girdilerini doğrulamanın ve temizlemenin önemini göstermektedir. Web uygulamalarınızın bu tür saldırılara karşı güvenli olduğundan emin olun.

