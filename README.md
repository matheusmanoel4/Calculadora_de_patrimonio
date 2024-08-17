# Calculadora de Patrimônio Líquido

## Descrição
A Calculadora de Patrimônio Líquido é uma aplicação desenvolvida em Python utilizando a biblioteca Tkinter para criar uma interface gráfica. A aplicação permite que os usuários insiram seus ativos e passivos para calcular seu patrimônio líquido.

## Pré-requisitos
- Python 3.11 ou superior
- Bibliotecas Python:
  - tkinter
  - Pillow

## Instalação
1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/calculadora-patrimonio.git

## Navegue até o diretório do projeto:
cd calculadora-patrimonio


### Instale as dependências necessárias:
pip install -r requirements.txt

### Uso
Execute o arquivo principal da aplicação:
python main.py

#### Documentação do Código 

#### Importa os módulos necessários do Tkinter e PIL para criar a interface gráfica e manipular imagens
main.py
Importações
from tkinter import Frame, Label, Entry, LEFT, NW, CENTER
from PIL import Image, ImageTk

#### Criação dos Frames
frameativo = Frame(framebaixo, width=180, height=370, bg=co9)
frameativo.grid(row=0, column=0, pady=5)

framepassivo = Frame(framebaixo, width=180, height=370, bg=co9)
framepassivo.grid(row=0, column=1)
##Cria frames para organizar os elementos da interface gráfica.


#### Logo
app_logo = Image.open("logo.png")
app_img = app_logo.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(framecima, image=app_img, width=900, compound=LEFT, padx=5, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=5, y=0)
Abre, redimensiona e adiciona a imagem do logo ao frame superior.

#### Título da Aplicação
app_ = Label(framecima, text="calculadora de patrimonio liquido", width=900, compound=LEFT, anchor=NW, font=("IVY", 12), bg=co1, fg=co4)
app_.place(x=80, y=10)
Adiciona o título da aplicação ao frame superior.

#### Linha Separadora
linha = Label(framecima, width=380, anchor=NW, font=("verdana", 12), bg=co3, fg=co1)
linha.place(x=0, y=47)
###Adiciona uma linha separadora ao frame superior para melhorar a organização visual

#### Função calcular
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

# Define a função calcular para calcular o patrimônio líquido com base nos valores inseridos nos campos de entrada.



### Contribuição
Faça um fork do projeto.

#### Crie uma nova branch para sua feature ou correção de bug:
git checkout -b minha-feature

### Faça commit das suas alterações
git commit -m 'Adiciona minha feature'

### Envie para o repositório remoto:
git push origin minha-feature

Abra um Pull Request.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

```

Explicação:
1 Título: calculadora de patrimonio 
2 Descrição: faz o calculo do seus patrimonios.
3 Pré-requisitos: Lista de requisitos necessários para executar o projeto.
4 Instalação: Passos para instalar e configurar o projeto.
5 Uso: Instruções de como usar a aplicação.
6 Documentação do Código: Explicação detalhada do código presente no arquivo main.py.
7 Contribuição: Guia de como contribuir para o projeto.
8 Licença: Informações sobre a licença do projeto.
