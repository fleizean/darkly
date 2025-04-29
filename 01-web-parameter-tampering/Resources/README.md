# Parametre Kurcalama Açıklaması

Parametre kurcalama, saldırganların bir uygulamanın davranışını manipüle etmek için URL, form veya çerezlerdeki parametreleri değiştirdiği bir web güvenlik açığıdır. Daha detaylı örneklerle açıklayayım.

## Parametre Kurcalama Nasıl Çalışır

Web uygulamalarında, parametreler sayfalar arasında veya sunucuya veri aktarmak için kullanılır. Bu parametreler şu şekillerde bulunabilir:

1. **URL Sorgu Dizeleri**: `example.com/page?parametre=deger`
2. **Form Verileri**: Formlar aracılığıyla bilgi gönderirken
3. **Çerezler**: Tarayıcıda saklanan bilgiler
4. **HTTP Başlıkları**: Kullanıcılardan gizlenen ancak araçlarla değiştirilebilen bilgiler

## Yaygın Örnekler

### 1. URL Parametre Kurcalama

**Örnek 1: Fiyat Manipülasyonu**
```
Orijinal: https://shop.example.com/checkout?productID=123&price=50.00
Kurcalanmış: https://shop.example.com/checkout?productID=123&price=1.00
```

Burada, bir saldırgan bir ürün için daha az ödemek amacıyla fiyat parametresini değiştirmiştir. Eğer uygulama bu parametreyi sunucu tarafında doğrulamadan kabul ederse, saldırı başarılı olur.

### 2. Erişim Kontrolü Bypass

**Örnek 2: Kullanıcı Rolü Kurcalama**
```
Orijinal: https://app.example.com/dashboard?userRole=user
Kurcalanmış: https://app.example.com/dashboard?userRole=admin
```

Eğer uygulama erişim haklarını uygun kimlik doğrulama olmadan userRole parametresine dayanarak belirlerse, saldırgan yetkisiz admin erişimi elde eder.

### 3. Parametreler Üzerinden Dizin Geçişi

**Örnek 3: Dosya Erişimi**
```
Orijinal: https://website.com/view.php?file=rapor.pdf
Kurcalanmış: https://website.com/view.php?file=../../../etc/passwd
```

Bu, file parametresini manipüle ederek amaçlanan dizinin dışındaki sistem dosyalarına erişmeyi dener.

### 4. Sosyal Medya Yönlendirmesi (BornToSec Gibi)

**Örnek 4: Yönlendirme Manipülasyonu**
```
Orijinal: http://example.com/redirect?site=instagram
Kurcalanmış: http://example.com/redirect?site=kotu-site.com
```

Uygulama, "site" parametresini doğrulama yapmadan güvenebilir ve kullanıcıları potansiyel olarak zararlı web sitelerine yönlendirebilir.

## Neden Tehlikeli

Parametre kurcalama şunlara yol açabilir:
- Bilgi ifşası
- Kimlik doğrulama bypass
- Fonksiyon suistimali
- Cross-site scripting (XSS)
- SQL enjeksiyonu
- Hizmet reddi (DoS)