#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"";

void main()
{

    printf("Shellcode length: %d\n", strlen(code));

    int (*ret)() = (int(*)())code;

    ret();

}