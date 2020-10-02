from Crypto.PublicKey import RSA

import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-p", "--passphrase", required=False,
   help="The passphrase for the keys (Optional)")

ap.add_argument("-o", "--output", required=False,
   help="The name of the keys (Optional. If not given, assume the name 'key_pen')")

args = vars(ap.parse_args())

# ----------------------------------------------------------

passphrase = args['passphrase']
key_name = args['output'] or "key_pen"

# Generate 2024-bit RSA key pair (private + public key)
keyPair = RSA.generate( bits = 3072 ) # use 3072 for production
pubKey = keyPair.publickey()

with open(f'.keys/{ key_name }.pub', 'wb') as pub_key:
    pub_key.write( pubKey.export_key() )

with open(f'.keys/{ key_name }.prv', 'wb') as private_key:
    private_key.write( keyPair.export_key( passphrase = passphrase ) )

print(f"Kaypair Generated in .keys/{ key_name }.*")
