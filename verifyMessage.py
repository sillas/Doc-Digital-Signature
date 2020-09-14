# pip install pycryptodome
# https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA384

import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-f", "--filename", required=True,
   help="The passphrase (Optional)")

ap.add_argument("-k", "--keys", required=False,
   help="The filename of the keys file without extension (Optional. If not given, assume the name 'key_pen')")

args = vars(ap.parse_args())

keys_file_name = args['keys'] or "key_pen"

# ----------------------------------------------------------

try:
    # Open the message
    with open( args['filename'], 'rb') as m:
        message = m.read()

    # Verify valid PKCS#1 v1.5 signature (RSAVP1)
    with open(f'.keys/{ keys_file_name }.sign', 'rb') as sign_key:
        signature = sign_key.read()

    with open(f'.keys/{ keys_file_name }.pub', 'rb') as pub_key:
        pubKey = RSA.import_key( pub_key.read() )

except Exception as e:
    print('ERRO:', e)
    exit()

hash = SHA384.new( message )
verifier = PKCS1_v1_5.new( pubKey )

if( verifier.verify( hash, signature ) ):
    print("\nThe message is signed correctly\n")

else:
    print("\nCaution! The message has been modified\n")