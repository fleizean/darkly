# Redirection / Yönlendirme
Bu proje, web uygulamalarında yönlendirme ile çalışmayı içerir. Yönlendirme, kullanıcıları farklı sayfalara veya harici sitelere yönlendirmek için kullanılır.

![Yönlendirme](redirections.png)

## Amaç

Bu projenin amacı, yönlendirmenin kullanıcıları farklı sayfalara veya harici sitelere yönlendirmek için nasıl kullanılabileceğini anlamaktır.

## Örnek

Bir HTML sayfasında yönlendirme örneği:

```html
<ul class="icons">
    <li><a href="index.php?page=redirect&amp;site=facebook" class="icon fa-facebook"></a></li>
    <li><a href="index.php?page=redirect&amp;site=twitter" class="icon fa-twitter"></a></li>
    <li><a href="index.php?page=redirect&amp;site=instagram" class="icon fa-instagram"></a></li>
</ul>
```

Bu örnekte, ikonlara tıklamak kullanıcıyı belirtilen sosyal medya sitelerine yönlendirecektir.

## Kullanım Durumları

- Harici sitelere yönlendirme
- Form gönderiminden sonra yönlendirme
- Güncel olmayan URL'leri yönetme

## Güvenlik Hususları

Yönlendirme faydalı olsa da, kimlik avı saldırıları için kullanılabilir. Her zaman URL'leri doğrulayın ve temizleyin, güvenliği sağlamak için.

## Sonuç

Yönlendirme, web geliştiricilerinin kullanıcıları farklı sayfalara veya harici sitelere yönlendirmesi için faydalı bir araçtır. Ancak, dikkatli ve uygun güvenlik önlemleri ile kullanılmalıdır.
