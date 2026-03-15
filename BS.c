// bootscreen.c - A "cara" do Star OS durante o boot
#include "sosp_api.h"

void desenhar_barra_progresso(int progresso) {
    char *vga = (char*) 0xB8000;
    // Lógica simples para desenhar blocos coloridos na tela VGA
    for(int i = 0; i < progresso; i++) {
        vga[i * 2 + 160] = '#'; // Linha abaixo do texto principal
        vga[i * 2 + 161] = 0x0A; // Cor verde para o "sucesso"
    }
}

void mostrar_boot_screen() {
    SOSP_ClearScreen();
    SOSP_Print("Carregando Star Kernel (SOSP)...");
    desenhar_barra_progresso(20); // Inicializando drivers
    desenhar_barra_progresso(50); // Montando sistema de ficheiros
    desenhar_barra_progresso(100); // Pronto!
}
