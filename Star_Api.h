#ifndef SOSP_API_H
#define SOSP_API_H

// Funções que o Kernel expõe para o sistema
extern void SOSP_Print(const char* message);
extern void SOSP_MemoryAllocate(unsigned int size);

typedef enum { SOSP_OK = 0, SOSP_ERROR = 1 } SOSP_Status;

#endif
