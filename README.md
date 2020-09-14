## How to sign a message using python and Crypto

# Install Dependencies

I'm using Python 3.7+ here.
```
$ pip3 install pycryptodome
```
# 1 - Generate the Public and Private keys first
- keys filename without extension
```
$ python3 generateKeypair.py [ -p passphrase ] [ -f filename_to_store_the_keys ]

Output:
"Kaypair Generated in .keys/{ filename }.*"
```

# 2 - Sign the message in "message.txt"
- keys filename without extension
```
$ python3 signTheMessage.py -m message.txt  [ -p passphrase ] [ -f filename_of_the_keys ]

Output:
"The message has SIGNED and de signature key is created on .keys/{ filename }.sign"
```
# 3 - Verify the message
- signature filename without extension
```
$ python3 verifyMessage.py -m message.txt [ -k filename_of_the_signature_key ]

Output:
"The message is signed correctly"
or
"Caution! The message has been modified"
```
