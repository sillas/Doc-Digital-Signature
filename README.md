## How to sign a message using python and Crypto

# Install Dependencies

I'm using Python 3.7+ here.
```
$ pip3 install pycryptodome
```
# 1 - Generate the Public and Private keys first
- keys filename without extension
```
$ python3 generateKeypair.py [ -p passphrase ] [ -o output ]
```
- -p \[--passphrase\]: The passphrase for the keys (Optional).
- -o \[--output \]: The name of the keys (If not given, assume the name "key_pen").

Output:
```
> Keypair Generated in .keys/{ filename }.*
```

# 2 - Sign the message in a file
- keys filename without extension
```
$ python3 signTheMessage.py -i filename.ext  [ -p passphrase ] [ -k keys ]
```
- -i \[--input\]: File to be signed.
- -p \[--passphrase\]: The passphrase of the keys (If provided when keys were generated).
- -k \[--keys\]: The name of the keys, if provided when keys were generated. If not given, assume the name "key_pen".

Output:
```
> The message has SIGNED and de signature key is created on .keys/{ keys }.sign
```

# 3 - Verify the message
- signature filename without extension
```
$ python3 verifyMessage.py -i filename.ext [ -o output ]
```
- -i \[--input\]: File to be verified.
- -o \[--output \]: The name of the signing key (If not given, assume the name "key_pen")

Output:
```
> The message is signed correctly
or
> Caution! The message has been modified
```
