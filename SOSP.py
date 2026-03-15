import subprocess
import os

class SOSP_Manager:
    def __init__(self):
        self.sources_list = "/etc/apt/sources.list.d/aura.list"
        self.log_file = "/var/log/aura_system.log"

    # --- AUM: Gestão de Sistema (Base e HTTP) ---
    def configurar_repositorios(self, url):
        """Adiciona repositórios externos via HTTP para o AUM."""
        print(f"🌐 AUM: Configurando repositório {url}...")
        with open(self.sources_list, "a") as f:
            f.write(f"deb {url} main\n")
        subprocess.run(['sudo', 'apt', 'update'])

    def atualizar_sistema(self):
        """Upgrade do núcleo e base do sistema."""
        print("🌟 AUM: Atualizando Kernel e Sistema Base...")
        subprocess.run(['sudo', 'apt', 'dist-upgrade', '-y'])

    # --- APM: Gestão de Apps (Alien/Wine/Deb) ---
    def instalar_app(self, nome_pacote, tipo='deb'):
        """Instalação de apps via APM."""
        if tipo == 'wine':
            print(f"🍷 APM: Instalando {nome_pacote} via Wine...")
            subprocess.run(['wine', nome_pacote])
        elif tipo == 'alien':
            print(f"🔄 APM: Convertendo pacote via Alien...")
            subprocess.run(['sudo', 'alien', '-i', nome_pacote])
        else:
            print(f"📦 APM: Instalando {nome_pacote} nativamente...")
            subprocess.run(['sudo', 'apt', 'install', '-y', nome_pacote])

# Exemplo de uso pelo Arquiteto:
# manager = SOSP_Manager()
# manager.configurar_repositorios("http://repo.aura-os.org/debian")
# manager.instalar_app("meu_programa.rpm", tipo='alien')
