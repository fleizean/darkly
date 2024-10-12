# Member Search SQL Injection Attack

## Description
In this project, we are testing for SQL injection vulnerabilities in a member search feature.

## Steps to Reproduce

1. Navigate to the following URL:
    ```
    http://localhost:8080/index.php?page=member&id=1'&Submit=Submit#
    ```

    ID: 1 
    First name: one
    Surname : me

2. Try this SQL Injection Code:
    ```
    SELECT * FROM users
    ```

    - You get this error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SELECT * FROM users' at line 1

