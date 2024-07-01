import base64

s = "112064b8f5c32ef951c1c1f315eb7de669bca0fd98d9c62cb7ba32c604a78708"
authcode = s
user_key = bytes.fromhex(authcode)[:16]
code = bytes.fromhex(authcode)[16:]
P = b'HUSTCTFer!______'
A = b'AdminAdmin!_____'
user_key = bytes([a ^ b ^ c for a, b, c in zip(user_key, P, A)])
print(user_key.hex() + code.hex())

