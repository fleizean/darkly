
# XSS Attack Feedback

In our project, we have tested multiple XSS (Cross-Site Scripting) attack vectors. Here are some examples of the XSS payloads we tried:

We tried many XSS injections (e.g., `<script>alert('XSS')</script>`, `<img src=x onerror=alert('XSS')>`, and `"><svg onload=alert('XSS')>`), but we couldn't reach the flag. The XSS security here seems to be well-implemented.# XSS Attack Feedback

1. `<script>alert('XSS1')</script>`
2. `<img src="x" onerror="alert('XSS2')">`
3. `<svg onload="alert('XSS3')"></svg>`

Despite our efforts, we were unable to retrieve the flag, indicating that the XSS security measures in place are robust. This suggests that the application has been well-secured against XSS vulnerabilities.

## Conclusion

The XSS security in this project appears to be strong, as our attempts to exploit XSS vulnerabilities were unsuccessful. This is a positive indicator of the application's security posture.