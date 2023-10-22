# Lab-5: Username enumeration via account lock
> Raj Pastagiya | 17/11/2023

## Problem Statement

> This lab is vulnerable to username enumeration. It uses account locking, but this contains a logic flaw. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

#### Summary
- The application has 2 vulnerabilities which leads to username and password bruteforce.
	1. For a valid user, if 5 times wrong password is sent, then instead of showing the "Incorrect username or password" it displays message related to account lockdown, which leads to find valid usernames.
	2. Even if account is locked down, when correct username and password is supplied, the application doesn't return any error message. (At the very least it should reply with the same account lock down message) This leads to find out valid password for a valid username.

#### \[+] The script is available at [brute-force.py](./scripts/brute-force.py)





