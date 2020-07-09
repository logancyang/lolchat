## DoverChat

This is a private chat app based on Flask-SocketIO, vanilla JS and Bootstrap, and DynamoDB. An invite token is required to join.

The message object:

```py
{
    "username": str,
    "data": str, # The actual message
    "timestamp": time.time(), # float with 2 decimal places
    "to": str # Optional: the username this message is for, in format `@<username>`
    "ents": list # Optional: list of entities identified by NER
}
```

Where `timestamp` is unix epoch time the server produces. The client shows local time based on it.
