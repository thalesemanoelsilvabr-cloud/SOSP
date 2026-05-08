using System;
using Aura.Utils; // Certifique-se de que LST e KV estão neste namespace
using Aura.APM;   // Namespace do seu Package Manager

namespace AuraOS {
    public class Kernel : Cosmos.System.Kernel {
        
        // Instância do APM para ele manter o estado durante a sessão
        private PackageManager _apm = new PackageManager();

        protected override void BeforeRun() {
            Console.Clear();
            // Mostra o LST (Logo Screen Time) logo na inicialização
            LST.Display(); 
            Console.WriteLine("AuraOS v1.0 carregado com sucesso.");
        }

        protected override void Run() {
            Console.Write($"{ConsoleColor.Cyan}Aura@User:~$ {ConsoleColor.White}");
            var input = Console.ReadLine().ToLower();

            if (string.IsNullOrEmpty(input)) return;

            // --- Sistema de Chamadas (Handlers) ---

            if (input == "lst") {
                LST.Display();
            }
            else if (input == "kv") {
                KVTool.ShowVersion();
            }
            else if (input.StartsWith("apm")) {
                ProcessarAPM(input);
            }
            else if (input == "help") {
                ExibirAjuda();
            }
            else {
                Console.WriteLine($"Comando '{input}' não reconhecido pelo QuanticS.");
            }
        }

        // Fazendo o APM funcionar com argumentos (ex: apm install sistema)
        private void ProcessarAPM(string input) {
            var parts = input.Split(' ');
            if (parts.Length < 2) {
                Console.WriteLine("Uso: apm [install/update/list] [pacote]");
                return;
            }

            string comando = parts[1];
            if (comando == "install" && parts.Length == 3) {
                _apm.Install(parts[2]);
            } else {
                Console.WriteLine("Comando APM inválido.");
            }
        }

        private void ExibirAjuda() {
            Console.WriteLine("Comandos disponíveis:");
            Console.WriteLine("- lst: Mostra a logo da Aura e infos do sistema");
            Console.WriteLine("- kv: Mostra a versão do Star/Aura Kernel");
            Console.WriteLine("- apm install [nome]: Instala pacotes via Aura PM");
        }
    }
}
