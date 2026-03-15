# Makefile Mestre para SOSP
CC=gcc
NASM=nasm
JAVAC=javac

all: build_kernel build_apps

build_kernel:
	@echo "Compilando Kernel..."
	$(NASM) -f bin boot/boot.asm -o bin/boot.bin
	$(CC) -c core/Kernel.c -o bin/kernel.o -ffreestanding

build_apps:
	@echo "Preparando Apps..."
	$(JAVAC) apps/Apploader.java -d bin/

clean:
	rm -rf bin/*
