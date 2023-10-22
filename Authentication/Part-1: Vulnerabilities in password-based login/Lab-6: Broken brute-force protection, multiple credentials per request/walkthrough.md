# Lab-6: Broken brute-force protection, multiple credentials per request
> Raj Pastagiya | 22/11/2023

## Problem Statement

> This lab is vulnerable due to a logic flaw in its brute-force protection. To solve the lab, brute-force Carlos's password, then access his account page.

#### Summary
- The application expects JSON values for the login credentials. This can be vulnerable if the username/password field can accept an array of values in a single request which may lead to bruteforcing the username and password
	- Here just to be safe we will send 10 passwords at a time in the json array.

#### \[+] The script is available at [brute-force.py](./scripts/brute-force.py)





