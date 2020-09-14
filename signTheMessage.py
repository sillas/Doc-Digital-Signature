# pip install pycryptodome
# https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA384

import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-f", "--file", required=True,
   help="The file with a message to sign")

ap.add_argument("-p", "--passphrase", required=False,
   help="The passphrase (Optional)")

ap.add_argument("-k", "--keys", required=False,
   help="The filename of the keys file without extension (Optional. If not given, assume the name 'key_pen')")

args = vars(ap.parse_args())

# ----------------------------------------------------------

file_message = args['file']
passphrase = args['passphrase']
keys_file_name = args['keys'] or "key_pen"

try:
    with open( file_message, 'rb' ) as m:
        message = m.read()
    
    with open(f'.keys/{ keys_file_name }.prv', 'rb') as private_key:
        keyPair = RSA.import_key( private_key.read(), passphrase = passphrase )

except Exception as e:
    print('ERRO:', e)
    exit()

# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
hash = SHA384.new( message )
signer = PKCS1_v1_5.new( keyPair )
signature = signer.sign( hash )

with open(f'.keys/{ keys_file_name }.sign', 'wb') as sign_key:
    sign_key.write( signature )

print(f'The message has SIGNED and de signature key is created on .keys/{ keys_file_name }.sign')