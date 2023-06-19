import tkinter
from tkinter import *
from tkinter import ttk

co0 = "#FFFFFF"
co1 = "#333333"  
co2 = "#fcc058"  
co3 = "#38576b"  
co4 = "#3297a8"   
co5 = "#fff873"  
co6 = "#fcc058"  
co7 = "#e85151"  
co8 = co4 
co10 ="#fcfbf7"
fundo = "#3b3b3b" 

janela = Tk()
janela.title('Jogo da Velha')
janela.geometry('300x370')
janela.configure(bg=fundo)

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

jogador_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
jogador_x.place(x=25, y=10)

jogador_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 8 bold'), bg=co1, fg=co0)
jogador_x.place(x=17, y=70)

jogador_x_pontuacao = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
jogador_x_pontuacao.place(x=80, y=20)

separador_pontuacao = Label(frame_cima, text='-', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
separador_pontuacao.place(x=110, y=20)

jogador_0 = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
jogador_0.place(x=170, y=10)

jogador_0 = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 8 bold'), bg=co1, fg=co0)
jogador_0.place(x=165, y=70)

jogador_0_pontuacao = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
jogador_0_pontuacao.place(x=130, y=20)



# Criando o jogo
jogador_1 = "X"
jogador_2  = "0"

pontuacao_1 = 0
pontuacao_2 = 0

tabuleiro = [['1','2','3'], ['4','5','6'], ['7','8','9']]

jogando = 'X'
joga = ''
contador = '0' 

def iniciar():
    def controlar(v):
        global jogando
        global contador
        global jogar

        #Comparando o valor recebido
        if v == 1:

            if botao_0['text'] =='':

                if jogando == 'X':
                    cor = co7
                if jogando == '0':
                    cor = co8


                botao_0['fg'] = cor
                botao_0['text'] = jogando 
                tabuleiro[[0][0]] = jogando

            if jogando == 'X':
                jogando = '0'
                joga = 'Jogador 1'
            else:
                jogando == 'X'
                joga = 'Jogador 2'

            contador += 1


            if contador >= 5:
                if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] !=

    def vencedor():
        pass

    def terminar_jogo():
        pass


    #linhas verticais
    jogador_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    jogador_.place(x=90, y=15)

    jogador_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    jogador_.place(x=157, y=15)

    #linhas horizontais
    jogador_ = Label(frame_baixo, text='', width=46, relief='flat', pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    jogador_.place(x=30, y=63)

    jogador_ = Label(frame_baixo, text='', width=46, relief='flat', pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    jogador_.place(x=30, y=127)

    #linha 0
    botao_0 = Button(frame_baixo, command=lambda:controlar('1'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    botao_0.place(x=30, y=15)

    botao_1 = Button(frame_baixo, command=lambda:controlar('2'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    botao_1.place(x=95, y=15)

    botao_2 = Button(frame_baixo, command=lambda:controlar('3'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    botao_2.place(x=163, y=15)

    #linha 1
    botao_3 = Button(frame_baixo, command=lambda:controlar('4'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    botao_3.place(x=30, y=75)

    botao_4 = Button(frame_baixo, command=lambda:controlar('5'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    botao_4.place(x=96, y=75)

    botao_5 = Button(frame_baixo, command=lambda:controlar('6'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    botao_5.place(x=163, y=75)

    #linha 2
    botao_6 = Button(frame_baixo, command=lambda:controlar('7'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    botao_6.place(x=30, y=135)

    botao_7 = Button(frame_baixo, command=lambda:controlar('8'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    botao_7.place(x=96, y=135)

    botao_8 = Button(frame_baixo, command=lambda:controlar('9'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    botao_8.place(x=163, y=135)

#botão de jogar
botao_jogar = Button(frame_baixo, command=iniciar, text='Jogar', width=10, height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
botao_jogar.place(x=85, y=210)

janela.mainloop()

