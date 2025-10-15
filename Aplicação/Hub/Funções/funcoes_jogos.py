from importlib.resources import Anchor
from textwrap import fill
import customtkinter as ctk
import os
import re

def obter_nomes_disponiveis():
    caminho_pasta = 'Jogos'
    nomes = []

    for nome_jogo in os.listdir(caminho_pasta):
        if nome_jogo.endswith('.py'):
            with open(os.path.join(caminho_pasta, nome_jogo), 'r', encoding='utf-8') as f:
                primeira_linha = f.readline()
                match = re.match(r'nome_jogo\s*=\s*[\'"](.+)[\'"]', primeira_linha)
                if match:
                    nomes.append(match.group(1))
    return nomes

def sair_do_jogo(controller):

    mensagem = 'Pretende mesmo sair do jogo?'
    sair_do_jogo = ctk.CTkToplevel()
    sair_do_jogo.geometry("320x120")
    sair_do_jogo.title("Sair do jogo")
    sair_do_jogo.resizable(False, False)
    sair_do_jogo.grab_set()
    sair_do_jogo.focus_force()
    sair_do_jogo.bind("<Escape>", lambda e: sair_do_jogo.destroy())

    label = ctk.CTkLabel(sair_do_jogo, text= mensagem, text_color="white", font=ctk.CTkFont(size=14))
    label.pack(pady=20, padx=10)

    def confirmar_saida():
        controller.mostrar_frame('ListaJogos')
        sair_do_jogo.destroy()


    botao_sim = ctk.CTkButton(sair_do_jogo, text= 'Sim', text_color= "white", font= ctk.CTkFont(size= 12), command= confirmar_saida)
    botao_sim.pack(side= 'left', padx= 10, expand = True)

    botao_nao = ctk.CTkButton(sair_do_jogo, text= 'Não', text_color= "white", font=ctk.CTkFont(size =12), command= sair_do_jogo.destroy)
    botao_nao.pack(side= 'right', padx= 10, expand = True)

    sair_do_jogo.mainloop()