# ASM x86 Shellcoding Linux

Objdump command to get all shellcode from a binary file :

       $ objdump -d ./ELF_BINARY|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'
