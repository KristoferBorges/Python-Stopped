from tkinter import *
import random

user_choice = ""


def escolha_pedra():
    global user_choice
    user_choice = "pedra"


def escolha_papel():
    global user_choice
    user_choice = "papel"


def escolha_tesoura():
    global user_choice
    user_choice = "tesoura"


def start():
    possible_choices = ['pedra', 'papel', 'tesoura']
    computer_choice = random.choice(possible_choices)

    if user_choice == computer_choice:
        text_jogo.config(fg="blue", text='EMPATE \n Usuário: {} \n Computador: {}'.format(user_choice, computer_choice))
    elif user_choice == 'tesoura' and computer_choice == 'papel':
        text_jogo.config(fg="green",
                         text='VENCEDOR \n Usuário: {} \n Computador: {}'.format(user_choice, computer_choice))
    elif user_choice == 'tesoura' and computer_choice == 'pedra':
        text_jogo.config(fg="red",
                         text='PERDEDOR \n Usuário: {} \n Computador: {}'.format(user_choice, computer_choice))
    elif user_choice == 'papel' and computer_choice == 'pedra':
        text_jogo.config(fg="green",
                         text='VENCEDOR \n Usuário: {} \n Computador: {}'.format(user_choice, computer_choice))
    elif user_choice == 'papel' and computer_choice == 'tesoura':
        text_jogo.config(fg="red",
                         text='PERDEDOR \n Usuário: {} \n Computador: {}'.format(user_choice, computer_choice))
    elif user_choice == 'pedra' and computer_choice == 'tesoura':
        text_jogo.config(fg="green",
                         text='VENCEDOR \n Usuário: {} \n Computador: {}'.format(user_choice, computer_choice))
    elif user_choice == 'pedra' and computer_choice == 'papel':
        text_jogo.config(fg="red",
                         text='PERDEDOR \n Usuário: {} \n Computador: {}'.format(user_choice, computer_choice))
    else:
        text_jogo.config(fg="red", text='Error')


janela_Inicial = Tk()
janela_Inicial.title('JOGO  -  JOKENPO')
janela_Inicial.geometry("300x370")

texto_inicio = Label(janela_Inicial, text='Usuário x Máquina')
texto_inicio.grid(column=0, row=1)

text_escolha = Label(janela_Inicial, font=("Helvetica", 24, "bold"), text='Faça sua escolha e \nclique em (START)')
text_escolha.grid(column=0, row=1)

botao_iniciar = Button(janela_Inicial, font=("Helvetica", 24, "bold"), pady=5, padx=5, text='START', background="green",
                       command=start)
botao_iniciar.grid(column=0, row=2)

botao_escolha_pedra = Button(janela_Inicial, font=("Helvetica", 14, "bold"), text='PEDRA', background="cyan", pady=5,
                             padx=5, command=escolha_pedra)
botao_escolha_pedra.grid(column=0, row=4)

botao_escolha_papel = Button(janela_Inicial, font=("Helvetica", 14, "bold"), text='PAPEL', background="cyan", pady=5,
                             padx=5, command=escolha_papel)
botao_escolha_papel.grid(column=0, row=6)

botao_escolha_tesoura = Button(janela_Inicial, font=("Helvetica", 14, "bold"), text='TESOURA', background="cyan",
                               pady=5, padx=5, command=escolha_tesoura)
botao_escolha_tesoura.grid(column=0, row=8)

text_jogo = Label(janela_Inicial, font=("Helvetica", 9, "italic"), text='')
text_jogo.grid(column=0, row=3)

janela_Inicial.mainloop()
