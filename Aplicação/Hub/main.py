import customtkinter as ctk
from Telas.tela_inicial import TelaInicial
from Telas.lista_jogos import ListaJogos
from Telas.tela_jogo import Tela_jogo
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("470x550")
        self.title("Aplicação nº1")

        self.frames = {}
        self.nome_jogador = None

        frame = TelaInicial(self)
        self.frames['TelaInicial'] = frame
        frame.place(relwidth=1, relheight=1)
        
        self.mostrar_frame("TelaInicial")
    
    def mostrar_frame(self, nome_frame):
        for frame in self.frames.values():
            frame.place_forget()
        self.frames[nome_frame].place(relwidth=1, relheight=1)

    def criar_lista_jogos(self, nome_jogador):
        if 'ListaJogos' in self.frames:
            self.frames['ListaJogos'].destroy()

        self.nome_jogador = nome_jogador
        lista = ListaJogos(self, nome_jogador)
        self.frames['ListaJogos'] = lista
        lista.place(relwidth=1, relheight=1)
        self.mostrar_frame('ListaJogos')
    
    def abrir_tela_jogo(self, nome_jogador, jogo_selecionado):
        if 'Tela_jogo' in self.frames:
            self.frames['Tela_jogo'].destroy()

        tela_jogo = Tela_jogo(self, nome_jogador, jogo_selecionado)
        self.frames['Tela_jogo'] = tela_jogo
        tela_jogo.place(relwidth=1, relheight=1)
        self.mostrar_frame('Tela_jogo')

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = App()
    app.mainloop()
