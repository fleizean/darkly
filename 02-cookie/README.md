# Cookies / Çerezler
This project involves working with cookies in web applications. Cookies are used to store data on the client's browser to track and identify users.

![Cookies](cookie.png)
![Cookies](cookie2.png)

## Purpose

The purpose of this project is to understand how cookies can be used to store data on the client's browser and how they can be managed securely.

## Example

Here is a simple example of setting a cookie in JavaScript:

```javascript
// Set a cookie
document.cookie = 'I_am_admin=b326b5062b2f0e69046810717534cb09';
```

The second value `b326b5062b2f0e69046810717534cb09` in the cookie appears to be an MD5 hash. MD5 (Message-Digest Algorithm 5) is a widely used cryptographic hash function that produces a 128-bit (16-byte) hash value, typically represented as a 32-character hexadecimal number.

In your example:

- `I_am_admin`: Likely represents the user role or username.
- `b326b5062b2f0e69046810717534cb09`: This looks like an MD5 hash of the string `admin`.

To verify, you can check by hashing the word `admin` using an MD5 hashing tool or function. Here is the result for `admin`:

```plaintext
MD5("admin") = b326b5062b2f0e69046810717534cb09
```

This indicates that the second value is the MD5 hash of the string `admin`.

## Security Considerations

Note: MD5 is considered cryptographically broken and unsuitable for further use due to vulnerabilities, so it is not recommended for securing sensitive data. It can easily be reversed using rainbow tables or other tools.

## Conclusion

Cookies are a useful tool for web developers to store data on the client's browser. However, they should be used with caution and proper security measures.
