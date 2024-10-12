# httpasswd admin Attack Explanation

1. **Accessing Hidden Directories**: The `robots.txt` file revealed hidden directories, including `/whatever` and `/.hidden`.

2. **Downloading .htpasswd**: By navigating to these directories, we were able to download the `.htpasswd` file, which contained hashed credentials. The content of this file is shown in [htpasswd](#file:htpasswd-context).

3. **Decrypting the Password**: Using an online MD5 decryption tool (https://md5.gromweb.com/), we decrypted the hash for the `root` user and obtained the password `qwerty123@`.

4. **Accessing Admin Page**: We navigated to the `/admin/` page and entered the decrypted password `qwerty123@` to gain access.

httpasswd ve admin alanını yaptık