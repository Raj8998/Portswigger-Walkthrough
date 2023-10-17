# Lab-3: # Username enumeration via response timing
> Raj Pastagiya | 17/11/2023

## Problem Statement

> This lab is vulnerable to username enumeration using its response times. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.
> Your credentials: `wiener:peter`

**HINT**: To add to the challenge, the lab also implements a form of IP-based brute-force protection. However, this can be easily bypassed by manipulating HTTP request headers.

### Summary

#### Looking at the site's response time on valid and invalid login 
- Before we start automating our enumeration, capture the login request in Burp-Suite to better see the response time on valid and invalid login requests.
- When trying different usernames and passwords:
	- A valid login attempt would take about 150-160 milliseconds and has 302 redirect response, while invalid login attempt takes around same time but has 200 OK response.
	- With valid username if the password length is about 30 characters than it takes around 400 milliseconds or more.
	- Also one-of the most important thing here is after 2-3 attempts of login it blocks us as it is also being told in HINT section.
		- To avoid this, if we use "X-Forwarded-For" key with different IP, then we are allowed. Ideally web-application allows this header and checks the header if the IP is in its block-list or not.
- Now that we know that after every 3 invalid request attempts we need to change the IP in "X-Forwarded-For" header, and also that for valid user and long enough password the response time is at least 400 milliseconds, we can automate our work.
- Since the complete script for changing the IP as well as enumerating users is to big to mention here, the sctip is available in scripts folder.

#### \[+] The script is available at [brute-force.py](./scripts/brute-force.py)





