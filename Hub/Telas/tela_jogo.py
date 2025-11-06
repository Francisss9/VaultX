import customtkinter as ctk
from Funções.funcoes_jogos import sair_do_jogo


class Tela_jogo(ctk.CTkFrame):
    def __init__(self, controller, nome_jogador, jogo_selecionado):
        super().__init__(controller, fg_color = '#2f2f2f')
        self.controller = controller
        self.nome_jogador = nome_jogador
        self.titulo = jogo_selecionado

        titulo = ctk.CTkLabel(
            self,                  
            text=self.titulo, 
            font=ctk.CTkFont(family='Lato', size= 22, weight='bold'),
            text_color = '#A3A3A3',
        )
        titulo.pack(pady=(30))

        self.terminal = ctk.CTkTextbox(self, width= 400, height= 300)
        self.terminal.pack(padx= 20, pady= 20)

        self.terminal.insert('end', f"Bem vindo {self.nome_jogador}\n")

        footer_frame = ctk.CTkFrame(self, fg_color='transparent')
        footer_frame.pack(side='bottom', fill='x', pady= 5)

        footer_frame.columnconfigure((0,1), weight=1)

        nome_jogador_label = ctk.CTkLabel(footer_frame, fg_color='transparent')
        nome_jogador_label.grid(row= 0, column= 0, sticky= 'nsw', padx= 10)
        nome_jogador_label.configure(
            text=f'Player: {nome_jogador}',
            font= ctk.CTkFont(size =11),
        )

        footer_brand = ctk.CTkLabel(
            footer_frame,
            text="2025 UNMADE DEVELOPER",
            font=ctk.CTkFont(family="Segoe UI", size=10, slant='italic'),
            fg_color='transparent',
            text_color="#A3A3A3",
        )
        footer_brand.grid(row= 0, column= 1, sticky= 'nse', padx= 10)

        button_voltar = ctk.CTkButton(self)
        button_voltar.configure(
            text='Voltar',
            fg_color='grey',
            hover_color= '#202020',
            command= lambda: sair_do_jogo(controller),
        )
        button_voltar.pack(side='bottom', pady= 20)
