from pymd5 import md5, padding

#how to use
m = "Use HMAC, not hashes"
# h = md5()
# h.update(m)
# print(h.hexdigest()) #3ecc68efa1871751ea9b0b1a5b25004d
# print(len(padding(len(m)*8))) #44



#length extension attack on string m
length_of_m = len(m)
bits = (length_of_m + len(padding(length_of_m * 8))) * 8
h = md5(state=bytes.fromhex("3ecc68efa1871751ea9b0b1a5b25004d"), count=bits)

x = "Good advice"
h.update(x)
#print(h.hexdigest())
#print(md5(m.encode() + padding(len(m)*8) + x.encode()).hexdigest())