; boot.asm - O ponto de partida do SOSP
[bits 32]
section .text
global _start
_start:
    mov eax, 0x1BADB002 ; Magic number do Multiboot
    ; Aqui começa a inicialização do processador
    jmp $ ; Loop infinito para teste
