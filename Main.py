from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  # 
co11 = "#f2f4f2"

#janela
janela = Tk()
janela.title("")
janela.geometry("380x500")
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use('clam')

# frames
#barra de cima 
framecima = Frame(janela, width=380, height=50, bg=co1)
framecima.grid(row=0 , column=0, columnspan=2)

# barra do meio
frameresultado = Frame(janela, width=380, height=50, bg=co3)
frameresultado.grid(row=1 , column=0, pady=10)

framebaixo = Frame(janela, width=380, height=400, bg=co1)
framebaixo.grid(row=2 , column=0, pady=10)

#dividindo a coluna de baixo 
frameativo = Frame(framebaixo, width=180, height=370, bg=co9)
frameativo.grid(row=0 , column=0, pady=5)

framepassivo = Frame(framebaixo, width=180, height=370, bg=co9)
framepassivo.grid(row=0 , column=1)

#logo ---------------------------
from PIL import ImageTk

#abrir imagem
app_logo = Image.open("logo.png")
app_img = app_logo.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(framecima, image=app_img, width=900, compound=LEFT, padx=5, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=5, y=0)

app_ = Label(framecima, text="calculadora de patrimonio liquido", width=900, compound=LEFT, anchor=NW, font=("IVY", 12), bg=co1, fg=co4)
app_.place(x=80, y=10)

linha = Label(framecima, width=380, anchor=NW, font=("verdana", 12), bg=co3, fg=co1)
linha.place(x=0, y=47)



#funçao para calcular o patrimonio liquido
def calcular():
    casa = float(valor_casa.get())
    imoveis = float(valor_imoveis.get())
    veiculos = float(valor_veiculos.get())
    investimentos = float(valor_investimento.get())
    outros = float(valor_outros.get())
    #ativos = casa + imoveis + veiculos + investimentos + outros

    hipoteca = float(valor_hipoteca.get())
    carro = float(valor_carro.get())
    estudos = float(valor_estudos.get())
    dividas = float(valor_dividas.get())
    #passivos = hipoteca + carro + estudos + dividas
    
    if casa == "" or imoveis == "" or veiculos == "" or investimentos == "" or outros == "" or hipoteca == "" or carro == "" or estudos == "" or dividas == "":
        return
    
    
    #calculando ativos
    else: ativos = float(casa) + float(imoveis) + float(veiculos) + float(investimentos) + float(outros)
    
    #calculando passivos
    passivos = float(hipoteca) + float(carro) + float(estudos) + float(dividas)
    
    #calculando resultado
    resultado = ativos - passivos
    
    resultado1 ['text'] = "R${:,.2f}".format(resultado)   
    
    
        

    #resultado = ativos - passivos
    #resultado = "R${:,.2f}".format(resultado)
    #resultado = Label(frameresultado, text=resultado, padx=10, width=15, anchor=NE, font=("verdana 25 bold"), bg=co3, fg=co1)
    #resultado.place(x=0, y=7)















# adicionando ativos
nome = Label(frameativo, text="insira ativos", padx=10, width=35, height=1, anchor=NW, font=("verdana 11"), bg=co2, fg=co1)
nome.place(x=0, y=0)

#valor da casa-----------------------------------------------------------------------------------------
nome = Label(frameativo, text="Valor casa", anchor=E, font=("verdana 9"), bg=co9, fg=co0)
nome.place(x=10, y=40)
valor_casa = Entry(frameativo, width=10, font=("ivy 12"), justify=CENTER, relief='solid')
valor_casa.place(x=10, y=65)
#-------------------------------------------------------------------------------------------------------


#valor imoveis-----------------------------------------------------------------------------------------
nome = Label(frameativo, text="imoveis", anchor=E, font=("verdana 9"), bg=co9, fg=co0)
nome.place(x=10, y=105)
valor_imoveis = Entry(frameativo, width=10, font=("ivy 12"), justify=CENTER, relief='solid')
valor_imoveis.place(x=10, y=125)
#-----------------------------------------------------------------------------------------------------------


#valor veiculos-----------------------------------------------------------------------------------------
nome = Label(frameativo, text="Veiculos", anchor=E, font=("verdana 9"), bg=co9, fg=co0)
nome.place(x=10, y=165)
valor_veiculos = Entry(frameativo, width=10, font=("ivy 12"), justify=CENTER, relief='solid')
valor_veiculos.place(x=10, y=195)
#---------------------------------------------------------------------------------------------------------------------


#valor investimento---------------------------------------------------------------------------------------------------
nome = Label(frameativo, text="Investimentos", anchor=E, font=("verdana 9"), bg=co9, fg=co0)
nome.place(x=10, y=230)
valor_investimento = Entry(frameativo, width=10, font=("ivy 12"), justify=CENTER, relief='solid')
valor_investimento.place(x=10, y=255)
#--------------------------------------------------------------------------------------------------------------------


#outros ativos---------------------------------------------------------------------------------------------------------------
nome = Label(frameativo, text="Outros ativos", anchor=E, font=("verdana 9"), bg=co9, fg=co0)
nome.place(x=10, y=290)
valor_outros = Entry(frameativo, width=10, font=("ivy 12"), justify=CENTER, relief='solid')
valor_outros.place(x=10, y=315)
#----------------------------------------------------------------------------------------------------------------------













# adicionando passivos---------------------------------------------------------------------------------------------
nome = Label(framepassivo, text="insira passivos", padx=10, width=35, height=1, anchor=NW, font=("verdana 11"), bg=co5, fg=co1)
nome.place(x=0, y=0)

#valor da hipoteca-----------------------------------------------------------------------------------------
nome = Label(framepassivo, text="Valor da hipoteca", anchor=E, font=("verdana 9"), bg=co9, fg=co0)
nome.place(x=10, y=40)
valor_hipoteca = Entry(framepassivo, width=10, font=("ivy 12"), justify=CENTER, relief='solid')
valor_hipoteca.place(x=10, y=65)
#-------------------------------------------------------------------------------------------------------


#valor emprestimo de carro-----------------------------------------------------------------------------------------
nome = Label(framepassivo, text="emprestimo de carro", anchor=E, font=("verdana 9"), bg=co9, fg=co0)
nome.place(x=10, y=105)
valor_carro = Entry(framepassivo, width=10, font=("ivy 12"), justify=CENTER, relief='solid')
valor_carro.place(x=10, y=125)
#-----------------------------------------------------------------------------------------------------------


#valor estudos-----------------------------------------------------------------------------------------
nome = Label(framepassivo, text="Estudos", anchor=E, font=("verdana 9"), bg=co9, fg=co0)
nome.place(x=10, y=165)
valor_estudos = Entry(framepassivo, width=10, font=("ivy 12"), justify=CENTER, relief='solid')
valor_estudos.place(x=10, y=195)
#---------------------------------------------------------------------------------------------------------------------


#valor outroas dividas---------------------------------------------------------------------------------------------------
nome = Label(framepassivo, text="Outras dividas", anchor=E, font=("verdana 9"), bg=co9, fg=co0)
nome.place(x=10, y=230)
valor_dividas = Entry(framepassivo, width=10, font=("ivy 12"), justify=CENTER, relief='solid')
valor_dividas.place(x=10, y=255)
#--------------------------------------------------------------------------------------------------------------------


#resultado---------------------------------------------------------------------------------------------------------------

resultado1 = Label(frameresultado, text="R${:,.2f}".format(00),padx=10,width=15, anchor=NE, font=("verdana 25 bold"), bg=co3, fg=co1)
resultado1.place(x=0, y=7)

botão_calculo = Button(framepassivo,command=calcular ,text="Calcular".upper(),padx=10,width=12, anchor=CENTER, font=("ivy 9 bold"), bg=co1, fg=co0)
botão_calculo.place(x=10, y=310)







janela.mainloop()
