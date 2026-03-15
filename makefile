# Makefile para SOSP
all: build_kernel build_apps

build_kernel:
	nasm -f bin boot/boot.asm -o bin/boot.bin
	gcc -c core/Kernel.c -o bin/kernel.o -ffreestanding

build_apps:
	javac apps/Apploader.java -d bin/

clean:
	rm -rf bin/*
