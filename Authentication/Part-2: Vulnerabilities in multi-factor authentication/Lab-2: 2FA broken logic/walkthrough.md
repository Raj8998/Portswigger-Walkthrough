# Lab-1: 2FA simple bypass
> Raj Pastagiya | 22/10/2023

> - This lab's two-factor authentication can be bypassed. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, access Carlos's account page.
> 	- Your credentials: `wiener:peter`
> 	- Victim's username `carlos`

## Summary
- Here when you login with given credentials, The application asks for 4 didgit security code for 2FA.
- Since we do not have any email access, we firstly try to attempt to got to the home page without providing 4 digit code and then go to accounts page.
- Because of poorely written code, you are essentially logged in and can go to the logged in user's accounts page without supplying any 4 digit security code.