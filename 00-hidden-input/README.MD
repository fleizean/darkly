# Hidden Input / Gizli Girdi

This project involves working with hidden input fields in HTML forms. Hidden inputs are used to store data that should not be visible or editable by the user.

Bu proje, HTML formlarında gizli girdi alanları ile çalışmayı içerir. Gizli girdiler, kullanıcı tarafından görünmemesi veya düzenlenmemesi gereken verileri saklamak için kullanılır.

![Hidden Input](hidden_input.png)

## Purpose / Amaç

The purpose of this project is to understand how hidden inputs can be used to pass data between the client and server without displaying it to the user.

Bu projenin amacı, gizli girdilerin verileri kullanıcıya göstermeden istemci ve sunucu arasında nasıl iletilebileceğini anlamaktır.

## Example / Örnek

Here is a simple example of a hidden input field in an HTML form:

İşte bir HTML formunda gizli bir girdi alanının basit bir örneği:

```html
<form action="#" method="POST">
    <input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
    <input type="submit" name="Submit" value="Submit">
</form>
```

In this example, the `mail` value is sent to the server when the form is submitted, but it is not visible to the user.

Bu örnekte, form gönderildiğinde `mail` değeri sunucuya gönderilir, ancak kullanıcıya görünmez.

## Use Cases / Kullanım Durumları

- Storing session tokens / Oturum belirteçlerini saklama
- Passing user IDs / Kullanıcı kimliklerini iletme
- Keeping track of state information / Durum bilgilerini takip etme

## Security Considerations / Güvenlik Dikkatleri

While hidden inputs are not visible to users, they can still be manipulated through browser developer tools. Always validate and sanitize data on the server side to ensure security.

Gizli girdiler kullanıcılar tarafından görünmez olsa da, tarayıcı geliştirici araçları aracılığıyla hala manipüle edilebilirler. Güvenliği sağlamak için verileri her zaman sunucu tarafında doğrulayın ve temizleyin.

## Conclusion / Sonuç

Hidden inputs are a useful tool for web developers to pass data without displaying it to users. However, they should be used with caution and proper security measures.

Gizli girdiler, web geliştiricilerinin verileri kullanıcılara göstermeden iletmeleri için yararlı bir araçtır. Ancak, dikkatli ve uygun güvenlik önlemleri ile kullanılmalıdır.