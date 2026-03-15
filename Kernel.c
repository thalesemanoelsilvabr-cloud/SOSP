// kernel.c - SOSP Kernel V0.1 (Base de Fundação)

void init_sosp_kernel() {
    // 1. Inicializar GDT (Global Descriptor Table)
    // 2. Inicializar IDT (Interrupt Descriptor Table)
    // 3. Inicializar Memory Manager
    // 4. Carregar os drivers base do SOSP
    
    const char *msg = "Star Kernel Iniciado - Modo Arquiteto Activo";
    char *vga = (char*) 0xB8000;
    for(int i = 0; msg[i] != '\0'; i++) {
        vga[i*2] = msg[i];
    }
}

void kernel_main() {
    init_sosp_kernel();
    // Aqui o SOSP entra em modo de espera por processos do "Star OS"
    while(1); 
}
