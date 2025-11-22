import tkinter as tk
import random
import time

# Variáveis globais
pontuacao = 0
tempo_restante = 10
jogando = False

def iniciar_jogo():
    global jogando, pontuacao, tempo_restante
    if not jogando:
        jogando = True
        pontuacao = 0
        tempo_restante = 10
        lbl_pontuacao.config(text=f"Pontuação: {pontuacao}")
        lbl_tempo.config(text=f"Tempo: {tempo_restante}")
        btn_start.config(state="disabled")
        mover_botao()
        atualizar_tempo()

def clicar():
    global pontuacao
    if jogando:
        pontuacao += 1
        lbl_pontuacao.config(text=f"Pontuação: {pontuacao}")
        mover_botao()

def mover_botao():
    # Move o botão para uma posição aleatória na janela
    x = random.randint(50, 350)
    y = random.randint(80, 250)
    btn_click.place(x=x, y=y)

def atualizar_tempo():
    global tempo_restante, jogando
    if tempo_restante > 0:
        tempo_restante -= 1
        lbl_tempo.config(text=f"Tempo: {tempo_restante}")
        janela.after(1000, atualizar_tempo)
    else:
        jogando = False
        lbl_tempo.config(text="Tempo: 0")
        btn_start.config(state="normal")
        btn_click.place_forget()
        lbl_pontuacao.config(text=f"Fim de jogo! Pontuação final: {pontuacao}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("🎯 Jogo de Clique Rápido")
janela.geometry("400x300")
janela.resizable(False, False)

# Widgets
lbl_instrucao = tk.Label(janela, text="Clique no botão o máximo que puder em 10 segundos!", font=("Arial", 12))
lbl_instrucao.pack(pady=10)

lbl_pontuacao = tk.Label(janela, text="Pontuação: 0", font=("Arial", 14))
lbl_pontuacao.pack()

lbl_tempo = tk.Label(janela, text="Tempo: 10", font=("Arial", 14))
lbl_tempo.pack()

btn_start = tk.Button(janela, text="Iniciar", font=("Arial", 12), bg="lightgreen", command=iniciar_jogo)
btn_start.pack(pady=10)

btn_click = tk.Button(janela, text="Clique!", font=("Arial", 12), bg="lightblue", command=clicar)

# Inicia o loop principal
janela.mainloop()
