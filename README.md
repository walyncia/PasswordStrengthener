# PasswordStrengthener
This module is dedicated to a recieving password and validating the stregnth of the password against a set of rules. The testing of the password will continue until it has been fufilled, at which time the username and pass will be written to a database. 
 
 **NOTE: There are concerns with both username and password storage in the same db but that is not the focus of this project.  The hash value of the password stored, using a cryptographic hash function not the password in plain text. The guidelines for password storage and password strength are taken from the [Authentication OWASP Cheat Sheet series](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

## Languages used: SQL, Python

## Requirements
- Install python or (python3 on MacOS) to run the python script on the command line
- A code editor (VS Code, Pycharm, etc)


## How to Use

1. At the root project directory's terminal window enter and submit the following script
### Windows
```
$ python main.py username_Here
```
### MacOS
```
$ python3 main.py username_Here
```

2. If the username is stored in the database, then the program ends and the username and password should be in the database file. If not, review the displayed rules, enter a password and submit
3. If the password rules are met, the program the program ends and the username and password should be in the database file. If not, provide another password that mets the defined rules.