import customtkinter as ctk

def on_focus_in(event):
    widget = event.widget
    texto_atual = widget.get()
    if texto_atual == "Insira o nome":
        widget.delete(0, ctk.END)

def on_focus_out(event):
    widget = event.widget
    texto_atual = widget.get()
    if texto_atual == '':
        widget.insert(0, 'Insira o nome')

def mostrar_erro(mensagem):
    erro_window = ctk.CTkToplevel()
    erro_window.geometry("300x120")
    erro_window.title("Erro")
    erro_window.resizable(False, False)
    erro_window.grab_set()
    erro_window.focus_force()
    erro_window.bind("<Escape>", lambda e: erro_window.destroy())

    label = ctk.CTkLabel(erro_window, text=mensagem, text_color="white", font=ctk.CTkFont(size=14))
    label.pack(pady=20, padx=10)

    botao_ok = ctk.CTkButton(erro_window, text="OK", command= erro_window.destroy)
    botao_ok.pack(pady=10)
    
    erro_window.mainloop()

def processar_nome(entry_widget, controller, event=None):
    nome = entry_widget.get().strip()
    
    if nome == '' or nome == 'Insira o nome':
        mostrar_erro('Nome inválido! Por favor, insira outro nome.')
    else:
        controller.criar_lista_jogos(nome)
