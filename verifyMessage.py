# pip install pycryptodome
# https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples
import os
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA384

import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-i", "--input", required=True,
   help="The filename to verify")

ap.add_argument("-k", "--keys", required=False,
   help="The filename of the keys file without extension (Optional. If not given, assume the name 'key_pen')")

ap.add_argument("-s", "--signature", required=False,
   help="The signature name (stored in \"signatures\" folder)")

args = vars(ap.parse_args())

keys_file_name = args['keys'] or "key_pen"
signatures = [args['signature']] if args['signature'] != None else []

for filename in os.listdir('signatures'):
    if( ".sign" in filename ):
        signatures.append( filename.replace('.sign', '') )

# ----------------------------------------------------------

try:
    # Open the message
    with open( args['input'], 'rb') as m:
        message = m.read()

    with open(f'.keys/{ keys_file_name }.pub', 'rb') as pub_key:
        pubKey = RSA.import_key( pub_key.read() )

except Exception as e:
    print('ERROR 1:', e)
    exit()

hash = SHA384.new( message )
verifier = PKCS1_v1_5.new( pubKey )

try:
    
    for signature in signatures:
        # Verify valid PKCS#1 v1.5 signature (RSAVP1)
        with open(f'signatures/{ signature }.sign', 'rb') as sign_key:
            sign = sign_key.read()

        if( verifier.verify( hash, sign ) ):
            print("Everything is ok!")
            print(f"Verified with { signature }.sign file\n")
            exit()


    print()
    print("##############################################")
    print("#           |                                #")
    print("#           | The message has been modified, #")
    print("#  Caution! | or there is no signature for   #")
    print("#           | this file.                     #")
    print("#           |                                #")
    print("##############################################\n")

except Exception as e:
    print('ERROR 2:', e)
