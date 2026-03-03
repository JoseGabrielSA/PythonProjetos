# Código para cadastrar produtos em um sistema de empresa 

# Passo a passo do código:
# Passo 1: entrar no sistema da empresa -> ABRIR NAVEGADOR
# Passo 2: fazer login
# Passo 3: abrir a base de dados
# Passo 4: cadastrar um produto
# Passo 5; repetir o passo 4 até acabar os produtos
# Bibliotecas = pacotes de códigos prontos para serem usados
# pyautogui = biblioteca para automação de tarefas no computador 
    #->code/terminal: pip install pyautogui
# time = biblioteca para controle de tempo  

#importar biblioteca:

import pyautogui
    # pyautogui.click -> clicar em um local da tela
    # pyautogui.write -> escrever um texto
    # pyautogui.press -> pressionar uma tecla
    # pyautogui.hotkey -> pressionar uma combinação de teclas
import time

#Passo 1:
pyautogui.PAUSE = 0.5 # tempo de espera entre cada comando
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')
# pausa maior para o site carregar:
time.sleep(5)

# Passo 2:
pyautogui.click(x=914, y=366) # clicar no campo de email
pyautogui.write('seu.email@gmail.com')
# para ir para o campo de senha, podemos usar o comando tab ou clicar diretamente no campo de senha:
pyautogui.press('tab') 
pyautogui.write('senha.contas')
#                               OU
    # pyautogui.click(x=914, y=430) # clicar no campo de senha
    # pyautogui.write('jg14.contas')

pyautogui.press('tab') # para ir para o botão de logar
pyautogui.press('enter') # para clicar no botão de logar
# fazer uma pausa maior para o site carregar após o login:
time.sleep(5)

# Passo 3:
import pandas as pd
# biblioteca para manipulação de dados
    #-> code/terminal: pip install pandas

    #pandas openpyxl 
    #->biblioteca para ler arquivos do excel
    #--> code/terminal: pip install openpyxl

# Para baixar tudo de uma vez: pip install pandas openpyxl
    #-> para ler um arquivo do excel, usamos o comando pd.read_excel
    #--> para ler um arquivo do csv, usamos o comando pd.read_csv
#   EX: tabela = pd.read_excel('produtos.xlsx')

tabela = pd.read_csv(r"C:\Users\Pichau\OneDrive\Desktop\Documentos\PythonFiles\cursoJornadaHASHIGTON\produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=678, y=252)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

#Passo 5: O passo 5 já está sendo executado dentro do passo 4, pois o comando "for" faz com que o processo de cadastro seja repetido para cada linha da tabela.
