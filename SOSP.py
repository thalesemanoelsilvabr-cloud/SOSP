import subprocess

class SOSP_Interface:
    def conectar_wifi(self, ssid, senha):
        print(f"📡 SOSP: Conectando a {ssid}...")
        subprocess.run(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', senha])

    def gerenciar_impressora(self):
        print("🖨️ SOSP: Buscando impressoras na rede...")
        subprocess.run(['lpadmin', '-p', 'Default_Printer', '-E', '-v', 'ipp://...'])

    def bluetooth_scan(self):
        print("🎧 SOSP: Procurando dispositivos Bluetooth...")
        subprocess.run(['bluetoothctl', 'scan', 'on'])

    def instalar_deb(self, arquivo_deb):
        print(f"📦 SOSP: Instalando {arquivo_deb}...")
        subprocess.run(['sudo', 'dpkg', '-i', arquivo_deb])
        subprocess.run(['sudo', 'apt', '-f', 'install', '-y']) # Resolve dependências
