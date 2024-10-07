# Cookies / Çerezler

This project involves working with cookies in web applications. Cookies are used to store data on the client's browser to track and identify users.

Bu proje, web uygulamalarında çerezlerle çalışmayı içerir. Çerezler, kullanıcıları izlemek ve tanımlamak için istemcinin tarayıcısında veri saklamak için kullanılır.

![Cookies](cookie.png)
![Cookies](cookie2.png)

## Purpose / Amaç

The purpose of this project is to understand how cookies can be used to store data on the client's browser and how they can be managed securely.

Bu projenin amacı, çerezlerin istemcinin tarayıcısında veri saklamak için nasıl kullanılabileceğini ve güvenli bir şekilde nasıl yönetilebileceğini anlamaktır.

## Example / Örnek

Here is a simple example of setting a cookie in JavaScript:

İşte JavaScript'te bir çerez ayarlamanın basit bir örneği:

```javascript
// Set a cookie
document.cookie = 'I_am_admin=b326b5062b2f0e69046810717534cb09';
```

The second value `b326b5062b2f0e69046810717534cb09` in the cookie appears to be an MD5 hash. MD5 (Message-Digest Algorithm 5) is a widely used cryptographic hash function that produces a 128-bit (16-byte) hash value, typically represented as a 32-character hexadecimal number.

Çerezdeki ikinci değer olan `b326b5062b2f0e69046810717534cb09` bir MD5 hash gibi görünüyor. MD5 (Message-Digest Algorithm 5), genellikle 32 karakterlik onaltılık bir sayı olarak temsil edilen 128-bit (16 bayt) bir hash değeri üreten yaygın olarak kullanılan bir kriptografik hash fonksiyonudur.

In your example:

Sizin örneğinizde:

- `I_am_admin`: Likely represents the user role or username.
- `b326b5062b2f0e69046810717534cb09`: This looks like an MD5 hash of the string `admin`.

- `I_am_admin`: Muhtemelen kullanıcı rolünü veya kullanıcı adını temsil eder.
- `b326b5062b2f0e69046810717534cb09`: Bu, `admin` kelimesinin bir MD5 hash'i gibi görünüyor.

To verify, you can check by hashing the word `admin` using an MD5 hashing tool or function. Here is the result for `admin`:

Doğrulamak için, `admin` kelimesini bir MD5 hash aracı veya fonksiyonu kullanarak hashleyebilirsiniz. İşte `admin` için sonuç:

```plaintext
MD5("admin") = b326b5062b2f0e69046810717534cb09
```

This indicates that the second value is the MD5 hash of the string `admin`.

Bu, ikinci değerin `admin` kelimesinin MD5 hash'i olduğunu gösterir.

## Security Considerations / Güvenlik Dikkatleri

Note: MD5 is considered cryptographically broken and unsuitable for further use due to vulnerabilities, so it is not recommended for securing sensitive data. It can easily be reversed using rainbow tables or other tools.

Not: MD5, kriptografik olarak kırılmış ve güvenlik açıkları nedeniyle daha fazla kullanım için uygun değildir, bu nedenle hassas verileri güvence altına almak için önerilmez. Rainbow tabloları veya diğer araçlar kullanılarak kolayca tersine çevrilebilir.

## Conclusion / Sonuç

Cookies are a useful tool for web developers to store data on the client's browser. However, they should be used with caution and proper security measures.

Çerezler, web geliştiricilerinin istemcinin tarayıcısında veri saklamaları için yararlı bir araçtır. Ancak, dikkatli ve uygun güvenlik önlemleri ile kullanılmalıdır.