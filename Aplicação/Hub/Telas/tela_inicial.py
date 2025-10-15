import customtkinter as ctk
from Funções.funcoes_interface import on_focus_in, on_focus_out, processar_nome

class TelaInicial(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller, fg_color="#2f2f2f")
        self.controller = controller

        titulo_label = ctk.CTkLabel(
            self,
            text="Centro de Jogos",
            font=ctk.CTkFont(family="Lato", size=22, weight="bold"),
            fg_color='transparent',
            text_color="#A3A3A3"
        )
        titulo_label.pack(pady=(30))

        footer_brand = ctk.CTkFrame(self, fg_color='transparent')
        footer_brand.pack(side= 'bottom', fill='x', pady= 5)

        brand_label = ctk.CTkLabel(
            footer_brand,
            text="2025 UNMADE DEVELOPER",
            font=ctk.CTkFont(family="Segoe UI", size=10, slant='italic'),
            fg_color='transparent',
            text_color="#A3A3A3",
        )
        brand_label.pack(side='right', padx=10)

        tela_inicial_ct = ctk.CTkFrame(self, fg_color="#2f2f2f", corner_radius=0)
        tela_inicial_ct.pack(pady=150)

        caixa_texto = ctk.CTkEntry(tela_inicial_ct, placeholder_text="Insira o nome")
        caixa_texto.bind('<FocusIn>', on_focus_in)
        caixa_texto.bind('<FocusOut>', on_focus_out)
        caixa_texto.bind('<Return>', lambda event: processar_nome(caixa_texto, self.controller))
        caixa_texto.pack(pady=20)

        botao_enter = ctk.CTkButton(
            tela_inicial_ct,
            text="Entrar",
            command=lambda: processar_nome(caixa_texto, self.controller),
            fg_color="grey",
            hover_color="#202020"
        )
        botao_enter.pack()
