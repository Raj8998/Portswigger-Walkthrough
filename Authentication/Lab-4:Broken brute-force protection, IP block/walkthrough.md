# Lab-4: Broken brute-force protection, IP block
> Raj Pastagiya | 17/11/2023

## Problem Statement

> This lab is vulnerable due to a logic flaw in its password brute-force protection. To solve the lab, brute-force the victim's password, then log in and access their account page.
> Your credentials: `wiener:peter`
> Victim's username: `carlos`

**HINT**: Advanced users may want to solve this lab by using a macro or the Turbo Intruder extension. However, it is possible to solve the lab without using these advanced features.

### Looking at the site's response time on valid and invalid login 
- Looking at the problem statement, we have password brute-force protection with some number of maximum attempt and then when we login using valid username and password the maximum attempt resets.
- I we try to identify how many maximum attempt we can make, we find that atleast 3 attempts can be made.
- The same script we used for Lab-3 can be used, and this time instead of changing X-Forwarded-For, we can login with `wiener:peter` and reset the count.

#### \[+] The script is available at [brute-force.py](./scripts/brute-force.py)





