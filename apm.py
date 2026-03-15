def instalar_suporte_hardware():
    pacotes = [
        "wpasupplicant",        # WiFi
        "bluez", "bluez-tools",  # Bluetooth
        "cups", "printer-driver-all" # Impressão
    ]
    print("🛠️ APM: Instalando suporte a hardware via Debian Repo...")
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', '-y'] + pacotes)
    subprocess.run(['sudo', 'systemctl', 'enable', 'cups'])
    subprocess.run(['sudo', 'systemctl', 'start', 'cups'])
