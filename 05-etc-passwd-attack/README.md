# Directory Traversal Attack Explanation

This README explains the directory traversal attack performed using the script in [main.py](#file:main.py-context). The goal of this attack was to access the `/etc/passwd` file on the server and retrieve the flag.

## Files

- **[main.py](#file:main.py-context)**: The main script that performs the directory traversal attack.
- **[flag.txt](#file:flag.txt-context)**: Contains the flag retrieved from the attack.
- **[success.html](#file:success.html-context)**: The HTML file generated upon successful retrieval of the target file.

## Attack Description

### Objective

The objective of this attack was to exploit a directory traversal vulnerability on the server to access the `/etc/passwd` file. This file typically contains user account information on Unix-based systems.

### Steps

1. **Setup**: The script uses the `aiohttp` library to perform asynchronous HTTP requests.
2. **Traversal Path**: The script constructs a traversal path by appending `../` to the base URL until the target file is found.
3. **Request Handling**: For each constructed URL, the script sends a GET request to the server.
4. **Response Check**: The script checks the response content for the presence of the word "flag". If found, it writes the content to `success.html`.
5. **Retry Mechanism**: The script includes a retry mechanism with a delay to handle intermittent failures.

### Execution

Run the script using the following command:

```sh
python main.py
```

The script will continue to append `../` to the URL and send requests until it successfully retrieves the `/etc/passwd` file.

## Flag

The flag retrieved from the attack is stored in [flag.txt](#file:flag.txt-context):

```
b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
```

## Result

Upon successful retrieval, the content of the `/etc/passwd` file is written to [success.html](#file:success.html-context).

## Conclusion

This attack demonstrates the importance of validating and sanitizing user input on the server-side to prevent directory traversal vulnerabilities. Always ensure that your web applications are secure against such attacks.
