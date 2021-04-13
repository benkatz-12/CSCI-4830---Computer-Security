#Q7
import hashlib
m = "Hello, world"
c = hashlib.sha3_256()
c.update(b"Hello, world")
print(c.hexdigest())


#Q8
from Crypto.Cipher import AES
asciitext = ""
for i in range(256):
    if i < 16:
        key_hex = "0000000000000000000000000000000" + hex(i)[2:]
    else:
        key_hex = "000000000000000000000000000000" + hex(i)[2:]
    key = bytes.fromhex(key_hex)
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(bytes.fromhex("5beed72ac6c91e16e5a705cbb4cf4417"))

    try:
        asciitext =  plaintext.decode("ASCII")
        print(asciitext)
    except UnicodeDecodeError:
        #print("Not valid unicode")
        continue