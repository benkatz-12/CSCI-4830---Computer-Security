#encrypting cyphertext based on key
import sys
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = "UVWXYZ"
key_len = len(key)
cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
def get_cipher(c, i):
    new = ((ord(c)-65) + (ord(key[i % key_len])-65)) % 26
    return alphabet[new]

encoded_cipher = ""
for i in range(0, len(cipher)):
    encoded_cipher = encoded_cipher + get_cipher(cipher[i], i)

print(encoded_cipher)