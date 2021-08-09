import hashlib, sys, os

salt = os.urandom(16)
password_enc = hashlib.pbkdf2_hmac('sha512', sys.argv[1].encode(), salt, 200000)

print (password_enc.hex())

