// TerminalBasicSystem(TBM).cs - O Terminal Refinado
using System;
using Aura.Utils;

namespace Aura.Shell {
    public class TerminalBasicSystem(TBS) {
        public void Initialize() {
            Console.Clear();
            LST.Display(); // Neofetch da Aura
            RunLoop();
        }

        private void RunLoop() {
            while (true) {
                Console.ForegroundColor = ConsoleColor.Magenta;
                Console.Write("┌──(");
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.Write("Aura@ASU"); // Aura Super User
                Console.ForegroundColor = ConsoleColor.Magenta;
                Console.Write(")-[");
                Console.ForegroundColor = ConsoleColor.White;
                Console.Write("/");
                Console.ForegroundColor = ConsoleColor.Magenta;
                Console.Write("]\n└─$ ");
                Console.ResetColor();

                string input = Console.ReadLine()?.Trim();
                if (string.IsNullOrEmpty(input)) continue;

                Execute(input);
            }
        }

        private void Execute(string command) {
            // Lógica de comando aprimorada
            if (command == "lst") LST.Display();
            else if (command == "kv") KVTool.ShowVersion();
            else if (command.StartsWith("dl ")) DL.Process(command.Replace("dl ", ""));
            else Console.WriteLine($"[!] ash: Comando '{command}' desconhecido.");
          // ASH é o ZSH da aura
    }
}
