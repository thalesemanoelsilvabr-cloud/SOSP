// sosp_api.h - A API de comunicação do Star Kernel
#ifndef SOSP_API_H
#define SOSP_API_H

// Funções de Gestão de Hardware que o Kernel oferece
extern void SOSP_Print(const char* message);
extern void SOSP_ClearScreen();
extern void SOSP_MemoryAllocate(unsigned int size);
extern void SOSP_EnableInterrupts();

// Definições de status para sistemas que usam o SOSP como base
typedef enum {
    SOSP_OK = 0,
    SOSP_ERROR_HW = 1,
    SOSP_ERROR_MEM = 2
} SOSP_Status;

#endif
