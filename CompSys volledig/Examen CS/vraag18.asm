%include "gt.asm"
section .data
min_operand EQU 2547892
deel_operand dd 4
een dd 1

section .bss
help resd 1

section .text
global _start
_start:
        inv[help]
        mov eax, [help]
        inv[help]
        add eax, [help]
        inv[help]
        add eax, [help]
        mov [help], eax
        uit[help]
        sub eax, min_operand
        mov [help], eax
        uit[help]
        imul dword [een]; ervoor zorgen dat EDX ofwel gelijk is aan FFFFFFFF bij een negatief getal in EAX ofwel met 00000000 bij een positief getal in EAX
        idiv dword [deel_operand]
        mov [help], eax
        uit[help]

        mov eax, 1; System call number (sys_exit)
        int 0x80; Perform System Call