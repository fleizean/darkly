# robots.txt Attack Explanation

In this project, we performed a `robots.txt` attack to uncover hidden directories and files on a web server. The attack script is written in Python and utilizes the `aiohttp` library for asynchronous HTTP requests. The main goal was to locate the `robots.txt` file by attempting directory traversal.

## Steps Taken

1. **Script Execution**: We executed the script found in [main.py](#file:main.py-context). This script attempts to access the `robots.txt` file by traversing directories.
2. **Finding robots.txt**: Once the `robots.txt` file was found, its content was saved to `success.html`. The content of this file can be seen in [success.html](#file:success.html-context).


This process demonstrates how directory traversal and analysis of the `robots.txt` file can reveal sensitive information on a web server.

