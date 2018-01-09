# Status: generates private key

from bit import Key, PrivateKey, PrivateKeyTestnet
key = Key()

# Print PrivateKey
print (key)
# Print public point using one way Elliptic key Function
print (key.public_point)
# Print public Key
print (key.public_key)
# Print Sharable Bitcoin address
print (key.address)
# Print export Wallet Import Format Private key
print (key.to_wif())
# Print export private key in hex format
print (key.to_hex())
# Print to be exported private key in integer Format
print (key.to_int())
# Print to be exported private key
print (key.to_pem())
