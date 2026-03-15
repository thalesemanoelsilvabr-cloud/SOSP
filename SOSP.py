import subprocess
import sys

def setup_network(action):
    if action == "wifi":
        print("🌐 SOSP: Inicializando interface Wi-Fi...")
        subprocess.run(['sudo', 'wpa_supplicant', '-i', 'wlan0', '-c', '/etc/wpa_supplicant/aura.conf', '-B'])
    elif action == "bt":
        print("🔵 SOSP: Inicializando Bluetooth...")
        subprocess.run(['sudo', 'systemctl', 'start', 'bluetooth'])
    elif action == "cups":
        print("🖨️ SOSP: Inicializando servidor de impressão...")
        subprocess.run(['sudo', 'systemctl', 'start', 'cups'])

# Lógica de recebimento de comandos do ASU
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "net":
        setup_network(sys.argv[2])
