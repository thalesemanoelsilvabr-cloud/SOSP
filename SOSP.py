import subprocess
import os

class SOSP_Interface:
    def __init__(self):
        self.log_prefix = "🌟 [SOSP-SYSTEM]"

    def log(self, mensagem):
        print(f"{self.log_prefix} {mensagem}")

    def conectar_wifi(self, ssid, senha):
        self.log(f"A tentar conectar à rede: {ssid}...")
        try:
            # Uso do nmcli para gestão de rede profissional
            subprocess.run(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', senha], check=True)
            self.log("✅ Conectado com sucesso!")
        except subprocess.CalledProcessError:
            self.log("❌ Erro: Não foi possível conectar. Verifique a password.")

    def gerenciar_impressora(self):
        self.log("🖨️ A configurar impressora via protocolo IPP...")
        # Configuração automática do servidor CUPS
        subprocess.run(['lpadmin', '-p', 'SOSP_Printer', '-E', '-v', 'ipp://localhost:631/printers/SOSP'], check=True)
        self.log("✅ Impressora pronta a imprimir.")

    def instalar_pacote(self, caminho_arquivo):
        """Instalador universal: .deb, .rpm (via alien)"""
        extensao = os.path.splitext(caminho_arquivo)[1].lower()
        self.log(f"📦 A processar pacote: {caminho_arquivo}")
        
        try:
            if extensao == ".deb":
                subprocess.run(['sudo', 'dpkg', '-i', caminho_arquivo], check=True)
            elif extensao == ".rpm":
                self.log("🔄 Conversão de .rpm para .deb em curso...")
                subprocess.run(['sudo', 'alien', '-i', caminho_arquivo], check=True)
            else:
                self.log("❌ Formato não suportado nativamente.")
                return
            
            # Corrige dependências automaticamente após a instalação
            subprocess.run(['sudo', 'apt', '-f', 'install', '-y'], check=True)
            self.log("🚀 Instalação concluída com sucesso!")
        except Exception as e:
            self.log(f"❌ Erro crítico: {e}")

    def status_sistema(self):
        """Retorna o estado do processador e memória (Kids-Friendly)"""
        memoria = os.popen("free -m").readlines()[1].split()[2]
        self.log(f"🧠 Memória usada: {memoria}MB")
