// kernel.c - O motor do SOSP
void kernel_main() {
    const char *msg = "SOSP Kernel Iniciado!";
    char *vga = (char*) 0xB8000; // Endereço da tela no modo VGA
    for(int i = 0; msg[i] != '\0'; i++) {
        vga[i*2] = msg[i];
    }
}
