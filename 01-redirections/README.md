# Redirection / Yönlendirme

This project involves working with redirection in web applications. Redirection is used to navigate users to different pages or external sites.

Bu proje, web uygulamalarında yönlendirme ile çalışmayı içerir. Yönlendirme, kullanıcıları farklı sayfalara veya harici sitelere yönlendirmek için kullanılır.

![Redirection](redirections.png)

## Purpose / Amaç

The purpose of this project is to understand how redirection can be used to navigate users to different pages or external sites.

Bu projenin amacı, yönlendirmenin kullanıcıları farklı sayfalara veya harici sitelere nasıl yönlendirebileceğini anlamaktır.

## Example / Örnek

Here is a simple example of redirection in an HTML page:

İşte bir HTML sayfasında yönlendirmenin basit bir örneği:

```html
<ul class="icons">
    <li><a href="index.php?page=redirect&amp;site=facebook" class="icon fa-facebook"></a></li>
    <li><a href="index.php?page=redirect&amp;site=twitter" class="icon fa-twitter"></a></li>
    <li><a href="index.php?page=redirect&amp;site=instagram" class="icon fa-instagram"></a></li>
</ul>
```

In this example, clicking on the icons will redirect the user to the specified social media sites.

Bu örnekte, simgelere tıklamak kullanıcıyı belirtilen sosyal medya sitelerine yönlendirecektir.

## Use Cases / Kullanım Durumları

- Navigating to external sites / Harici sitelere yönlendirme
- Redirecting after form submission / Form gönderiminden sonra yönlendirme
- Handling outdated URLs / Güncel olmayan URL'leri yönetme

## Security Considerations / Güvenlik Dikkatleri

While redirection is useful, it can be exploited for phishing attacks. Always validate and sanitize URLs to ensure security.

Yönlendirme yararlı olsa da, kimlik avı saldırıları için kullanılabilir. Güvenliği sağlamak için URL'leri her zaman doğrulayın ve temizleyin.

## Conclusion / Sonuç

Redirection is a useful tool for web developers to navigate users to different pages or external sites. However, it should be used with caution and proper security measures.

Yönlendirme, web geliştiricilerinin kullanıcıları farklı sayfalara veya harici sitelere yönlendirmeleri için yararlı bir araçtır. Ancak, dikkatli ve uygun güvenlik önlemleri ile kullanılmalıdır.