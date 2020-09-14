from Crypto.PublicKey import RSA

import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-p", "--passphrase", required=False,
   help="The passphrase (Optional)")

ap.add_argument("-f", "--filename", required=False,
   help="The filename to export the keys (Optional. If not given, assume the name 'key_pen')")

args = vars(ap.parse_args())

# ----------------------------------------------------------

passphrase = args['passphrase']
key_name = args['filename'] or "key_pen"

# Generate 2024-bit RSA key pair (private + public key)
keyPair = RSA.generate( bits = 2024 ) # use 3072 for production
pubKey = keyPair.publickey()

with open(f'.keys/{ key_name }.pub', 'wb') as pub_key:
    pub_key.write( pubKey.export_key() )

with open(f'.keys/{ key_name }.prv', 'wb') as private_key:
    private_key.write( keyPair.export_key( passphrase = passphrase ) )

print(f"Kaypair Generated in .keys/{ key_name }.*")