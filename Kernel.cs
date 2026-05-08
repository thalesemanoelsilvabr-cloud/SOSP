using System;
using System.Collections.Generic;
using Cosmos.System.FileSystem; // Integração com o sistema de arquivos
using Aura.APM;   // Seu Gerenciador de Pacotes Independente
using Aura.Utils; // Onde residem LST e KV

namespace AuraOS
{
    public class Kernel : Cosmos.System.Kernel
    {
        // Declaração do Sistema de Arquivos da Aura
        private CosmosVFS _vfs;
        private PackageManager _apm;
        private DebianBridge _debBridge;

        protected override void BeforeRun()
        {
            // Inicializando o sistema de arquivos (Base para estabilidade)
            _vfs = new CosmosVFS();
            Cosmos.System.FileSystem.VFS.VFSManager.RegisterVFS(_vfs);

            // Inicializando módulos de rede e pacotes
            _apm = new PackageManager();
            _debBridge = new DebianBridge();

            Console.Clear();
            
            // LST: Logo Screen Time - Tela de Boas-Vindas
            LST.Display();
            
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("AuraOS v1.0 (QuanticS) carregado com sucesso.");
            Console.WriteLine("Sistema operando sob diretrizes da Aura Inc.");
            Console.ResetColor();
            Console.WriteLine("Digite 'help' para ver os comandos disponíveis.");
            Console.WriteLine();
        }

        protected override void Run()
        {
            // Prompt estilizado indicando o Aura Super User (ASU)
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.Write("Aura@root:~$ ");
            Console.ResetColor();

            var input = Console.ReadLine();
            if (string.IsNullOrWhiteSpace(input)) return;

            ProcessCommand(input.Trim());
        }

        private void ProcessCommand(string input)
        {
            var args = input.Split(' ');
            var cmd = args[0].ToLower();

            switch (cmd)
            {
                case "lst":
                    LST.Display(); // Chama o Neofetch da Aura
                    break;

                case "kv":
                    KVTool.ShowVersion(); // Versão do Star/Aura Kernel
                    break;

                case "apm":
                    HandleAPM(args); // Gerenciador de pacotes
                    break;

                case "cls":
                case "clear":
                    Console.Clear();
                    break;

                case "help":
                    ShowHelp();
                    break;

                case "about":
                    Console.WriteLine("AuraOS: Um projeto de soberania digital.");
                    Console.WriteLine("Fundadores: Thales, Matheus, Vitor e Gabriel.");
                    Console.WriteLine("Missão: Mostrar que 4 crianças podem superar 100 adultos.");
                    break;

                default:
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"Erro: Comando '{cmd}' não encontrado no QuanticS.");
                    Console.ResetColor();
                    break;
            }
        }

        private void HandleAPM(string[] args)
        {
            if (args.Length < 2)
            {
                Console.WriteLine("Uso: apm [install / update / list]");
                return;
            }

            string action = args[1].ToLower();

            if (action == "update")
            {
                // Sincroniza com os repositórios HTTP do Debian
                _debBridge.SyncDebianPackages().Wait();
            }
            else if (action == "install" && args.Length == 3)
            {
                string package = args[2];
                // Verifica se é para baixar do Debian ou repositório Aura
                if (package.EndsWith(".deb")) {
                    _debBridge.InstallDeb(package);
                } else {
                    _apm.Install(package);
                }
            }
            else
            {
                Console.WriteLine("Comando APM inválido ou parâmetros ausentes.");
            }
        }

        private void ShowHelp()
        {
            Console.WriteLine("\n--- Comandos Disponíveis ---");
            Console.WriteLine("lst         - Exibe a logo e informações do sistema (Aura Neofetch)");
            Console.WriteLine("kv          - Mostra a versão do Kernel e build QuanticS");
            Console.WriteLine("apm         - Gerencia pacotes (ex: apm update ou apm install [nome])");
            Console.WriteLine("cls/clear   - Limpa o terminal");
            Console.WriteLine("about       - Sobre os fundadores e a Aura Inc.");
            Console.WriteLine("help        - Lista todos os comandos");
            Console.WriteLine("---------------------------\n");
        }
    }
}
