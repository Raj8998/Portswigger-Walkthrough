# Lab 2

## Modifying Serialized data types

### Question Description:

We have user access as wiener:peter but the lab is vulnerable to authentication bypass as it deserializes insecurely the object we pass. Get the Administrator access and then delete Carlos's account.

### Tools Used:

- Burp Suite

#### Step 1 [ Intercept and decode phase ]:

After logging in as wiener intercept the home page and send it to burp repeater ( Check lab 1 if you don't know how to do it. ) and notice the cookie section. Generally our object is encoded with base64 and then encoded with URL encoding which in our case looks like below.

> Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjY6IndpZW5lciI7czoxMjoiYWNjZXNzX3Rva2VuIjtzOjMyOiJyazhoSWhvWkZuVER4S1FQMDE1VGVzeWQ3dVlxVTh5NiI7fQ%3d%3d

First decode it with URL Encoding and then with base64. The decoded object will look like below.

> O:4:"User":2:{s:8:"username";s:6:"wiener";s:12:"access_token";s:32:"rk8hIhoZFnTDxKQP015Tesyd7uYqU8y6";}

#### Step 2 [ Modify and forward serialized object ]:

The point of interest here is the access_token as in theory description on the site [ Exploiting Insecure Deserialization ](https://portswigger.net/web-security/deserialization/exploiting) explained if we change the serialized object's data type and value of `s:32:"rk8hIhoZFnTDxKQP015Tesyd7uYqU8y6"` to `i:0` and if this goes unchecked the user access is given without any password and we need `administrator` authentication thus we also need to change the value of username. The modified object will look like below.

