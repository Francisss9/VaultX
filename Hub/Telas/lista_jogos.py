import customtkinter as ctk
from Funções.funcoes_jogos import obter_nomes_disponiveis
import importlib
import threading

class ListaJogos(ctk.CTkFrame):
    def __init__(self, controller, nome_jogador):
        super().__init__(controller, fg_color="#2f2f2f")
        self.controller = controller
        self.nome_jogador = nome_jogador

        titulo = ctk.CTkLabel(
            self,                  
            text="Jogos Armazenados", 
            font=ctk.CTkFont(family='Lato', size= 22, weight='bold'),
            text_color = '#A3A3A3',
        )
        titulo.pack(pady=(30))

        self.nomes_disponiveis = obter_nomes_disponiveis()
        self.jogo_selecionado = None
        self.frame_lista_jogos = ctk.CTkScrollableFrame(self, width=200, height=225)
        self.frame_lista_jogos.pack(pady=20)

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

        button_voltar = ctk.CTkButton(self, command= lambda: controller.mostrar_frame('TelaInicial'))
        button_voltar.configure(
            text='Voltar',
            fg_color='grey',
            hover_color= '#202020',
        )
        button_voltar.pack(side='bottom', pady= 20)

        self.button_jogar = ctk.CTkButton(self, fg_color='transparent')
        self.button_jogar.configure(
            text= 'Jogar',
            fg_color= 'grey',
            hover_color = '#202020',
            state= 'disabled',
            command= self.executar_jogo,
        )
        self.button_jogar.pack(pady=1)
        
        self.mostrar_lista_jogos()

    def mostrar_lista_jogos(self):
        for widget in self.frame_lista_jogos.winfo_children():
            widget.destroy()
        self.buttons_jogos = {}
        for nome_jogo in self.nomes_disponiveis:
            button = ctk.CTkButton(
                self.frame_lista_jogos,
                text = nome_jogo,
                cursor = 'hand2',
                fg_color= "grey",
                hover_color= "#474747",
            )
            button.pack(pady=1, padx=1, side= 'left')
            button.bind('<Button-1>', lambda e, n= nome_jogo: self.selecionar_jogo(n))
            self.buttons_jogos[nome_jogo] = button


    def selecionar_jogo(self, nome_visivel):
        self.jogo_selecionado = nome_visivel
        if self.jogo_selecionado == nome_visivel:
            self.button_jogar.configure(state= 'normal')
            print(f'Jogo selecionado: {nome_visivel} \n')
        else:
            print('Ainda não foi selecionado um jogo \n')
        

    def executar_jogo(self):
        if hasattr(self, 'jogo_selecionado') and self.jogo_selecionado:
            try:
                modulo = importlib.import_module(f'Jogos.{self.jogo_selecionado}')
                if hasattr(modulo, 'main'):
                    self.button_jogar.configure(state = 'disabled')
                    def run_game():
                        try:
                            modulo.main()
                        except Exception as e:
                            print(f"Erro ao correr o jogo: {e}")

                    threading.Thread(target=run_game, daemon=True).start()
                    self.controller.abrir_tela_jogo(self.nome_jogador, self.jogo_selecionado)

                else:
                    print(f'O jogo \"{self.jogo_selecionado}\" não tem uma função main().')
            except Exception as e:
                print(f'Erro ao executar o jogo \"{self.jogo_selecionado}\": {e}')
        else:
            print('Nenhum jogo foi selecionado.')
