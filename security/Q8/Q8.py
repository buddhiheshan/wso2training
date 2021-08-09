import hashlib, sys, os

salt = os.urandom(16)
password_enc = hashlib.sha512(salt + sys.argv[1].encode())

print (password_enc.hexdigest())

