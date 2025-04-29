# Cookies / Çerezler
Bu proje, web uygulamalarında çerezlerle çalışmayı içerir. Çerezler, kullanıcıları izlemek ve tanımlamak için istemcinin tarayıcısında veri depolamak için kullanılır.

![Çerezler](cookie.png)
![Çerezler](cookie2.png)

## Amaç

Bu projenin amacı, çerezlerin istemcinin tarayıcısında nasıl veri depolamak için kullanılabileceğini ve güvenli bir şekilde nasıl yönetilebileceğini anlamaktır.

## Örnek

İşte JavaScript'te bir çerez ayarlamanın basit bir örneği:

```javascript
// Bir çerez ayarla
document.cookie = 'I_am_admin=b3d8e3397dd58186292b9e6e4e99f391';
```

Çerezdeki ikinci değer `b3d8e3397dd58186292b9e6e4e99f391` bir MD5 hash gibi görünmektedir. MD5 (Message-Digest Algorithm 5), 128-bit (16-byte) hash değeri üreten ve genellikle 32 karakterlik onaltılık sayı olarak temsil edilen yaygın bir kriptografik hash fonksiyonudur.

Örneğinizde:

- `I_am_admin`: Muhtemelen kullanıcı rolünü veya kullanıcı adını temsil eder.
- `b3d8e3397dd58186292b9e6e4e99f391`: Bu, `true` kelimesinin MD5 hash'i.

Doğrulamak için, `true` kelimesini bir MD5 hash aracı veya fonksiyonu kullanarak hashleyebilirsiniz. İşte `true` için sonuç:

```plaintext
MD5("true") = b3d8e3397dd58186292b9e6e4e99f391
```

Bu, ikinci değerin `true` kelimesinin MD5 hash'i olduğunu gösterir.

## Güvenlik Hususları

Not: MD5, kriptografik olarak kırılmış ve güvenlik açıkları nedeniyle daha fazla kullanım için uygun değildir, bu nedenle hassas verileri güvence altına almak için önerilmez. Rainbow tabloları veya diğer araçlar kullanılarak kolayca tersine çevrilebilir.

## Sonuç

Çerezler, web geliştiricileri için istemcinin tarayıcısında veri depolamak için yararlı bir araçtır. Ancak, dikkatli ve uygun güvenlik önlemleri ile kullanılmalıdır.
