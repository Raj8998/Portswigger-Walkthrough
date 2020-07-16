# Insecure Deserialization
## What is serialization?

**Serialization** is the process of converting complex data structure, such as objects and their fields, into a "flatter" format that can be sent and received as a sequential stream of bytes [1](https://portswigger.net/web-security/deserialization).

## Decerialization

**Deserialization** is the process of stroing this byte stream to a fully functional replica of the original object, in the exact state as when it was serialized.

## What is insecure deserialization?

**Insecure Deserialization** is when user-controllable data is deserialized by a website which potentially enables an attacker to manipulate serialized objects in order to pass harmful data into the application code.

For more reference for insecure deserialization [refer this](https://portswigger.net/web-security/deserialization) and to know exploit techniques [refer this](https://portswigger.net/web-security/deserialization/exploiting).
