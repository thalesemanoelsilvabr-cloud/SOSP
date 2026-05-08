import tkinter as tk
from tkinter import messagebox
import time

class AuraLiveCD:
    def __init__(self, root):
        self.root = root
        self.root.title("AuraOS 1.0 - LiveCD Mode")
        self.root.geometry("1024x600")
        self.root.configure(bg="#0a0a0a") # Fundo Deep Space

        # Barra de Tarefas Superior
        self.top_bar = tk.Frame(self.root, bg="#1a1a1a", height=30)
        self.top_bar.pack(side="top", fill="x")
        
        self.clock_label = tk.Label(self.top_bar, text="", fg="cyan", bg="#1a1a1a", font=("Consolas", 10))
        self.clock_label.pack(side="right", padx=10)
        self.update_clock()

        self.user_label = tk.Label(self.top_bar, text="Aura Super User (ASU)", fg="magenta", bg="#1a1a1a", font=("Consolas", 10, "bold"))
        self.user_label.pack(side="left", padx=10)

        # Área de Trabalho (Desktop)
        self.desktop = tk.Frame(self.root, bg="#0a0a0a")
        self.desktop.pack(expand=True, fill="both")

        # Ícones do Desktop
        self.create_icon("Aura MarketOS", "🛒", self.open_market)
        self.create_icon("Aura Games (AG)", "🎮", self.open_games)
        self.create_icon("Terminal (QuanticS)", "💻", self.open_terminal)
        self.create_icon("Instalar AuraOS", "💾", self.install_os)

        # Rodapé com a Missão da Aura Inc.
        self.footer = tk.Label(self.root, 
            text="Aura Inc. - Mostrando que 4 crianças podem ser mais do que se mostram.", 
            fg="#444", bg="#0a0a0a", font=("Arial", 8, "italic"))
        self.footer.pack(side="bottom", pady=5)

    def create_icon(self, text, symbol, command):
        frame = tk.Frame(self.desktop, bg="#0a0a0a")
        frame.pack(side="left", padx=30, pady=30)
        
        btn = tk.Button(frame, text=symbol, font=("Arial", 40), bg="#111", fg="cyan", 
                        activebackground="cyan", relief="flat", command=command)
        btn.pack()
        
        label = tk.Label(frame, text=text, fg="white", bg="#0a0a0a", font=("Consolas", 10))
        label.pack()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)

    # Funções dos Fundadores
    def open_market(self):
        messagebox.showinfo("Aura MarketOS", "Iniciando sistema de Matheus e Thales...")

    def open_games(self):
        messagebox.showinfo("Aura Games", "Iniciando Aura Games (Projeto de Vitor e Gabriel)...")

    def open_terminal(self):
        # Simulação do LST.cs e KV.cs
        top = tk.Toplevel(self.root)
        top.title("QuanticS Terminal")
        top.geometry("600x400")
        top.configure(bg="black")
        
        log = tk.Text(top, bg="black", fg="cyan", font=("Consolas", 10))
        log.pack(expand=True, fill="both")
        log.insert("end", "Aura@root:~$ lst\n")
        log.insert("end", "[INFO] AuraOS 1.0 (QuanticS System)\n")
        log.insert("end", "[INFO] Kernel: Star/Aura Kernel\n")
        log.insert("end", "Aura@root:~$ _")

    def install_os(self):
        res = messagebox.askyesno("Instalador", "Deseja instalar o AuraOS permanentemente no disco?")
        if res:
            messagebox.showinfo("Sucesso", "AuraOS está sendo gravado via Star Kernel...")

if __name__ == "__main__":
    root = tk.Tk()
    app = AuraLiveCD(root)
    root.mainloop()
