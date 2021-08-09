import hashlib, sys

password_enc = hashlib.pbkdf2_hmac('sha512', sys.argv[1].encode(), b'Km5d5ivMy8iexuHcZrsD', 200000)

print (password_enc.hex())

