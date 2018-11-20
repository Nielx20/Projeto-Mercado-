'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Janiel NIcacio da Silva (jns3)
E-mail: jns3@cin.ufpe.br
Data: 2018-04-21

Copyright(c) 2018 Janiel NIcacio da Silva
'''
from tkinter import *
from tkinter import messagebox
from datetime import *

#==========================# JANELAS #==========================#
def janelaLogin():

    ''' Janela referente a tela de Login'''

    janela = Tk()

    lb0 = Label(janela, text = 'Tela de Login', bg = 'Red', height = 5)
    lb1 = Label(janela, text = 'Login:', bg = 'white', font = '20')
    lb2 = Label(janela, text = 'Senha:', bg = 'White', font = '20')

    edLogin = Entry(janela, )
    edSenha = Entry(janela, show = '*' )

    bt = Button(janela, width = 10, text = 'Entrar')
    bt['command'] = lambda: btClickLogin(dicionarioDeUsuarios, edLogin, edSenha)

    lb0.pack(side = TOP, fill = BOTH)
    lb1.place(x = 300, y = 250)
    lb2.place(x = 297, y = 285)

    edLogin.place(x = 353, y = 253)
    edSenha.place(x = 353, y =287)

    bt.place(x = 360, y = 315)

    janela.geometry('800x500+100+15')

    janela.mainloop()

def janelaNivel1(usuario):

    ''' Janela referênte ao usuário Administrador '''

    nivel1 = Tk()

    lb0 = Label(nivel1, text = 'BEM VINDO', bg = 'red', height = 5)
    lb1 = Label(nivel1, text = '' , bg = 'Yellow', width = 29)
    lb2 = Label(nivel1, text = 'FUNÇÕES', bg = 'White', font = 20)

    bt1 = Button(nivel1, width = 25, height = 2, text = 'Cadastrar Usuario', command = lambda: frameFunCadUsua(nivel1,usuario))
    bt2 = Button(nivel1, width = 25, height = 2, text = 'Remover Usuário', command = lambda: frameFunRemUsua(nivel1,usuario))
    bt3 = Button(nivel1, width = 25, height = 2, text = 'Alterar Nivel de usuário', command = lambda: frameAlterarNivel(nivel1,usuario))
    bt4 = Button(nivel1, width = 25, height = 2, text = 'Cadastrar Produto', command = lambda: frameFunCadProd(nivel1,usuario))
    bt5 = Button(nivel1, width = 25, height = 2, text = 'Remover Produto', command = lambda: frameFunRemProd(nivel1,usuario))
    bt6 = Button(nivel1, width = 25, height = 2, text = 'Buscar Produto', command = lambda: frameFunBuscarProd(nivel1,usuario))
    bt7 = Button(nivel1, width = 25, height = 2, text = 'Atualizar Produto', command = lambda: frameFunAtualizarProd(nivel1,usuario))
    bt8 = Button(nivel1, width = 25, height = 2, text = 'Gravar Arquivo', command = lambda: btGravarArquivos(dicionarioDeProdutos,dicionarioDeUsuarios,usuario))
    bt9 = Button(nivel1, width = 25, height = 2, text = 'Sair', command = lambda: btClickFunFrameVoltar(nivel1,usuario))
    bt10 = Button(nivel1, width = 25, height = 2, text = 'elem. Ordenados', command = lambda:escreverArquivoOrdenado(dicionarioDeProdutos,usuario))
    bt11 = Button(nivel1, width = 25, height = 2, text = 'Criptografar', command = lambda:criptografarDicionario(dicionarioDeUsuarios,usuario))
    lb0.pack(side = TOP, fill = BOTH)
    lb1.pack (anchor = NW, fill = Y, expand = 1)
    lb2.place (x = 55, y= 100)

    bt1.place(x = 10, y = 135)
    bt2.place(x = 10, y = 180)
    bt3.place(x = 10, y = 225)
    bt4.place(x = 10, y = 270)
    bt5.place(x = 10, y = 315)
    bt6.place(x = 10, y = 360)
    bt7.place(x = 10, y = 405)
    bt8.place(x = 10, y = 450)
    bt9.place(x = 600, y = 450)
    bt10.place(x = 600, y = 405)
    bt11.place(x = 600, y = 360)

    nivel1.geometry('800x500+100+15')

    nivel1.mainloop()
def janelaNivel2(usuario):

    ''' Janela referente a usuários Nível 2, possui ... funções  '''

    nivel2 = Tk()

    lb0 = Label(nivel2, text = 'BEM VINDO', bg = 'red', height = 5)
    lb1 = Label(nivel2, text = '' , bg = 'Yellow', width = 29)
    lb2 = Label(nivel2, text = 'FUNÇÕES', bg = 'White', font = 20)


    bt4 = Button(nivel2, width = 25, height = 2, text = 'Cadastrar Produto',command = lambda: frameFunCadProd(nivel2,usuario))
    bt5 = Button(nivel2, width = 25, height = 2, text = 'Remover Produto',command = lambda: frameFunRemProd(nivel2,usuario))
    bt6 = Button(nivel2, width = 25, height = 2, text = 'Buscar Produto',command = lambda: frameFunBuscarProd(nivel2,usuario))
    bt7 = Button(nivel2, width = 25, height = 2, text = 'Atualizar Produto',command = lambda: frameFunAtualizarProd(nivel2,usuario))
    bt8 = Button(nivel2, width = 25, height = 2, text = 'Gravar Arquivo',command = lambda: btClickFunFrameVoltar(nivel2,usuario))
    bt10 = Button(nivel2, width = 25, height = 2, text = 'elem. Ordenados', command = lambda:escreverArquivoOrdenado(dicionarioDeProdutos,usuario))
    bt9 = Button(nivel2, width = 25, height = 2, text = 'Sair', command = lambda: btClickFunFrameVoltar(nivel2,usuario))

    lb0.pack(side = TOP, fill = BOTH)
    lb1.pack (anchor = NW, fill = Y, expand = 1)
    lb2.place (x = 55, y= 100)


    bt4.place(x = 10, y = 135)
    bt5.place(x = 10, y = 180)
    bt6.place(x = 10, y = 225)
    bt7.place(x = 10, y = 270)
    bt8.place(x = 10, y = 315)
    bt10.place(x = 10, y = 360)
    bt9.place(x = 10, y = 405)

    nivel2.geometry('800x500+100+15')

    nivel2.mainloop()

def janelaNivel3(usuario):

    ''' janiela referente a usuários de Nível 3'''

    nivel3 = Tk()

    lb0 = Label(nivel3, text = 'BEM VINDO', bg = 'red', height = 5)
    lb1 = Label(nivel3, text = '' , bg = 'Yellow', width = 29)
    lb2 = Label(nivel3, text = 'FUNÇÕES', bg = 'White', font = 20)

    bt6 = Button(nivel3, width = 25, height = 2, text = 'Buscar Produto', command = lambda: frameFunBuscarProd(nivel3,usuario))
    bt7 = Button(nivel3, width = 25, height = 2, text = 'elem. Ordenados', command = lambda: escreverArquivoOrdenado(dicionarioDeProdutos,usuario))
    bt8 = Button(nivel3, width = 25, height = 2, text = 'sair',command = lambda: btClickFunFrameVoltar(nivel3,usuario))

    lb0.pack(side = TOP, fill = BOTH)
    lb1.pack (anchor = NW, fill = Y, expand = 1)
    lb2.place (x = 55, y= 100)


    bt6.place(x = 10, y = 135)
    bt7.place(x = 10, y = 180)
    bt8.place(x = 10, y = 225)

    nivel3.geometry('800x500+100+15')

    nivel3.mainloop()

#==========================# FRAMES #==========================#

def frameFunCadUsua(janela,usuario):

    frameCadastrar = Frame(janela, bg = 'Green', width = 590, height = 420)

    titulo = Label(frameCadastrar, text = 'Cadastrar Usuário', bg = 'gray', width = 90,  height = 5 )


    lb3 = Label(frameCadastrar, text = 'Login:', width = 10)
    lb4 = Label(frameCadastrar, text = 'Senha:', width = 10)
    lb6 = Label(frameCadastrar, text = 'Insira as informações ao lado', width = 40, height = 10)

    ed3 = Entry(frameCadastrar)
    ed4 = Entry(frameCadastrar)


    bt1 = Button(frameCadastrar, text = 'Cadastrar')
    bt1['command'] = lambda: btCadastrarFrameCadUsua(dicionarioDeUsuarios, ed3, ed4, lb6, usuario)
    bt2 = Button(frameCadastrar, text = 'Voltar', command = lambda: btClickFunFrameVoltar(frameCadastrar, usuario))

    lb3.place(x = 20, y = 160)
    lb4.place(x = 20, y = 190)

    lb6.place(x = 240, y = 110)

    ed3.place(x = 98, y = 160)
    ed4.place(x = 98, y = 190)


    bt1.place(x = 50, y = 280)
    bt2.place(x = 120, y = 280)

    titulo.place(x = 0, y = 0)

    frameCadastrar.place(x = 210, y = 80)

    log = 'Abriu função de Cadastrar Usuários'
    salvarLog(usuario,log)

def frameFunRemUsua(janela,usuario):

    ''' Frame responsavel ligado a função de remover usuário, que possui a janela associada como parametro '''

    frameRemover = Frame(janela, bg = 'Green', width = 590, height = 420)

    titulo = Label(frameRemover, text = 'Remover Usuário', bg = 'gray', width = 90,  height = 5 )

    lb1 = Label(frameRemover, text = 'Login:', width = 10)
    lb2 = Label(frameRemover, text = 'Informações Aqui', width = 40, height = 10)

    ed1 = Entry(frameRemover)

    bt1 = Button(frameRemover, text = 'Remover', command = lambda: btRemoverFrameRemUsua(dicionarioDeUsuarios, ed1, lb2,usuario))
    bt2 = Button(frameRemover, text = 'Voltar', command = lambda: btClickFunFrameVoltar(frameRemover,usuario))

    lb1.place(x = 20, y = 190)
    lb2.place(x = 240, y = 110)

    ed1.place(x = 98, y = 190)

    bt1.place(x = 50, y = 280)
    bt2.place(x = 120, y = 280)

    titulo.place(x = 0, y = 0)

    log = 'Abriu função de Remover Usuário'
    salvarLog(usuario,log)

    frameRemover.place(x = 210, y = 80)

def frameAlterarNivel(janela,usuario):

    ''' Frame responsavel ligado a função de Alterar Nível de Usuário, que recebe a janela associada como parametro '''

    frameAlterar = Frame(janela, bg = 'Green', width = 590, height = 420)

    titulo = Label(frameAlterar, text = 'Alterar Nível de Usuário', bg = 'gray', width = 90,  height = 5 )


    lb1 = Label(frameAlterar, text = 'Login:', width = 10)
    lb2 = Label(frameAlterar, text = 'Nível:', width = 10)
    lb3 = Label(frameAlterar, width = 40, height = 10)
    lb3['text'] = 'Digite o Login a ser alterado o nível'

    ed1 = Entry(frameAlterar)
    ed2 = Entry(frameAlterar)


    btAlterar = Button(frameAlterar, text = 'Alterar')
    btAlterar['command'] = lambda: btAlterarFrameAltUsua(dicionarioDeUsuarios, ed1, ed2, lb3,usuario)
    btVoltar = Button(frameAlterar, text = 'Voltar')
    btVoltar['command'] = lambda: btClickFunFrameVoltar(frameAlterar,usuario)

    lb1.place(x = 20, y = 160)
    lb2.place(x = 20, y = 190)
    lb3.place(x = 240, y = 110)

    ed1.place(x = 98, y = 160)
    ed2.place(x = 98, y = 190)


    btAlterar.place(x = 50, y = 280)
    btVoltar.place(x = 120, y = 280)
    btVoltar['command'] = lambda: btClickFunFrameVoltar(frameAlterar,usuario)

    titulo.place(x = 0, y = 0)

    log = 'Abriu função de Alterar Nível'
    salvarLog(usuario,log)

    frameAlterar.place(x = 210, y = 80)

def frameFunCadProd(janela,usuario):

    ''' Frame ligado a função de Cadastrar Produto, que recebe a janela associada como parametro '''

    frameCadastrar = Frame(janela, bg = 'light Green', width = 590, height = 420)

    titulo = Label(frameCadastrar, text = 'Cadastrar Produto', bg = 'light blue', width = 90,  height = 5 )

    lb1 = Label(frameCadastrar, text = 'Codigo:', width = 10)
    lb2 = Label(frameCadastrar, text = 'Nome:', width = 10)
    lb3 = Label(frameCadastrar, text = 'Marca:', width = 10)
    lb4 = Label(frameCadastrar, text = 'Validade:', width = 10)
    lb5 = Label(frameCadastrar, text = 'Preço:', width = 10)
    lb6 = Label(frameCadastrar, text = 'Quantidade:', width = 10)
    lb7 = Label(frameCadastrar, text = 'Codigo de 3 digitos', width = 40, height = 10)

    edCodigo = Entry(frameCadastrar)
    edNome = Entry(frameCadastrar)
    edMarca = Entry(frameCadastrar)
    edValidade = Entry(frameCadastrar)
    edPreco = Entry(frameCadastrar)
    edQuantidade = Entry(frameCadastrar)

    btCadastrar = Button(frameCadastrar, text = 'Cadastrar')


    btVoltar = Button(frameCadastrar, text = 'Voltar')
    btVoltar['command'] = lambda: btClickFunFrameVoltar(frameCadastrar,usuario)

    lb1.place(x = 20, y = 100)
    lb2.place(x = 20, y = 130)
    lb3.place(x = 20, y = 160)
    lb4.place(x = 20, y = 190)
    lb5.place(x = 20, y = 220)
    lb6.place(x = 20, y = 250)
    lb7.place(x = 240, y = 110)

    edCodigo.place(x = 98, y = 100)
    edNome.place(x = 98, y = 130)
    edMarca.place(x = 98, y = 160)
    edValidade.place(x = 98, y = 190)
    edPreco.place(x = 98, y = 220)
    edQuantidade.place(x = 98, y = 250)

    btCadastrar.place(x = 50, y = 280)
    btVoltar.place(x = 120, y = 280)

    titulo.place(x = 0, y = 0)

    frameCadastrar.place(x = 210, y = 80)

    codigo = edCodigo.get()
    nome = edNome.get()
    marca = edMarca.get()
    validade = edValidade.get()
    preco = edPreco.get()
    quantidade = edQuantidade.get()

    btCadastrar.place(x = 50, y = 280)
    btVoltar.place(x = 120, y = 280)

    btCadastrar['command'] = lambda: btCadastrarFunFrameCadProd(dicionarioDeProdutos, lb7, edCodigo, edNome, edMarca, edValidade, edPreco, edQuantidade,usuario)

    log = 'Abriu função de Cadastrar Produto'
    salvarLog(usuario,log)

def frameFunRemProd(janela,usuario):

    ''' Frame ligado a função de Remover Produto, que recebe a janela associada como parametro '''

    frameRemover = Frame(janela, bg = 'Green', width = 590, height = 420)

    titulo = Label(frameRemover, text = 'Remover Produto', bg = 'gray', width = 90,  height = 5 )

    lb1 = Label(frameRemover, text = 'Codigo:', width = 10)
    lb2 = Label(frameRemover, text = 'Nome:', width = 10)
    lb3 = Label(frameRemover, width = 40, height = 10)
    lb3['text'] = 'Escolha umas das variaveis\npara verifiacar o produto'
    lb4 = Label(frameRemover, text = 'Função remover disponivel apenas com codigo')
    edCodigo = Entry(frameRemover)
    edNome = Entry(frameRemover)

    btRemover = Button(frameRemover, text = 'Remover')
    btVoltar = Button(frameRemover, text = 'Voltar')
    btVerificar = Button(frameRemover, text = 'Verificar')
    btVoltar['command'] = lambda: btClickFunFrameVoltar(frameRemover,usuario)
    btRemover['command']= lambda: btRemoverFrameRem(dicionarioDeProdutos, edCodigo, lb4,usuario)


    lb1.place(x = 20, y = 160)
    lb2.place(x = 20, y = 190)
    lb3.place(x = 240, y = 110)
    lb4.place(x = 250, y = 230)

    edCodigo.place(x = 98, y = 160)
    edNome.place(x = 98, y = 190)

    btRemover.place(x = 20, y = 280)
    btVoltar.place(x = 95, y = 280)
    btVerificar.place(x = 150, y = 280)

    titulo.place(x = 0, y = 0)

    frameRemover.place(x = 210, y = 80)

    btVerificar['command'] = lambda: btVerificarFrameAtualizar(frameRemover, dicionarioDeProdutos, edCodigo, edNome, lb3,usuario)

    log = 'Abriu função Remover Produto'
    salvarLog(usuario,log)

def frameFunBuscarProd(janela,usuario):

    ''' Frame ligado a função de Buscar Produto, que recebe a janela associada como parametro '''

    frameBuscar = Frame(janela, bg = 'Green', width = 590, height = 420)

    titulo = Label(frameBuscar, text = 'Buscar Produto', bg = 'gray', width = 90,  height = 5 )

    lb1 = Label(frameBuscar, text = 'Codigo:', width = 10)
    lb2 = Label(frameBuscar, text = 'Nome:', width = 10)
    lb3 = Label(frameBuscar, width = 40, height = 10)
    lb3['text'] = 'Escolha umas das variaveis\npara verificar o produto'
    lb4 = Label(frameBuscar, text = '')

    edCodigo = Entry(frameBuscar)
    edNome = Entry(frameBuscar)

    btVerificar = Button(frameBuscar, text = 'Buscar')
    btVoltar = Button(frameBuscar, text = 'Voltar')
    btVoltar['command'] = lambda: btClickFunFrameVoltar(frameBuscar,usuario)


    lb1.place(x = 20, y = 160)
    lb2.place(x = 20, y = 190)
    lb3.place(x = 240, y = 110)
    lb4.place(x = 250, y = 230)

    edCodigo.place(x = 98, y = 160)
    edNome.place(x = 98, y = 190)

    btVerificar.place(x = 20, y = 280)
    btVoltar.place(x = 95, y = 280)

    titulo.place(x = 0, y = 0)

    frameBuscar.place(x = 210, y = 80)

    btVerificar['command'] = lambda: btVerificarFrameAtualizar(frameBuscar, dicionarioDeProdutos, edCodigo, edNome, lb3,usuario)

    log = 'Abriu função de Buscar Produto'
    salvarLog(usuario,log)

def frameFunAtualizarProd(janela,usuario):

    ''' Frame ligado a função de Atualizar Produto, que recebe a janela associada como parametro '''

    frameAtualizar = Frame(janela, bg = 'Green', width = 590, height = 420)

    titulo = Label(frameAtualizar, text = 'Atualizar Produto', bg = 'gray', width = 90,  height = 5 )

    lb1 = Label(frameAtualizar, text = 'Codigo:', width = 10)
    lb2 = Label(frameAtualizar, text = 'Nome:', width = 10)
    lb3 = Label(frameAtualizar, text = 'Marca:', width = 10)
    lb4 = Label(frameAtualizar, text = 'Validade:', width = 10)
    lb5 = Label(frameAtualizar, text = 'Preço:', width = 10)
    lb6 = Label(frameAtualizar, text = 'Quantidade:', width = 10)
    lb7 = Label(frameAtualizar, text = 'Codigo de 3 digitos', width = 40, height = 10)

    edCodigo = Entry(frameAtualizar)
    edNome = Entry(frameAtualizar)
    edMarca = Entry(frameAtualizar)
    edValidade = Entry(frameAtualizar)
    edPreco = Entry(frameAtualizar)
    edQuantidade = Entry(frameAtualizar)

    btAtualizar = Button(frameAtualizar, text = 'Atualizar')
    btAtualizar['command'] = lambda: btAtualizarFrameAtualProd(dicionarioDeProdutos, edCodigo, edNome, edMarca, edValidade, edPreco, edQuantidade, lb7,usuario)
    btVoltar = Button(frameAtualizar, text = 'Voltar')
    btVoltar['command'] = lambda: btClickFunFrameVoltar(frameAtualizar,usuario)
    btVerificar = Button(frameAtualizar, text = 'Verificar')
    btVerificar['command'] = lambda: btVerificarFrameRem(dicionarioDeProdutos, edCodigo,lb2,lb3,lb4,lb5,lb6,lb7,edNome,edMarca,edValidade,edPreco,edQuantidade,usuario)

    lb1.place(x = 20, y = 100)
    edCodigo.place(x = 98, y = 100)
    lb7.place(x = 240, y = 110)

    btAtualizar.place(x = 20, y = 280)
    btVoltar.place(x = 95, y = 280)
    btVerificar.place(x = 150, y = 280)

    log = 'Abriu função de Atualizar Produto'
    salvarLog(usuario,log)
    titulo.place(x = 0, y = 0)

    frameAtualizar.place(x = 210, y = 80)

#==========================# BOTÕES #==========================#

def btClickLogin(dicionario, login, senha):

    ''' Botão ligado a Tela de Login, recebe o dicionario, login e senha como paramentro
    para verificar o usuário que deseja logar no sistema '''

    nivelUsuario = ''
    achei = False
    login = login.get()
    senha = senha.get()

    for chave in dicionario:
        if chave == login and dicionario[chave][0] == senha:
            nivelUsuario = dicionario[chave][1]
            achei = True
            loginDoLog = login
            log = 'Logou'
            salvarLog(login, log )

            messagebox.showinfo('Login Bem Sucedido!', 'Press Okay to continue')
    if achei == False:
        log = 'Tentou logar'
        salvarLog(login, log)
        loginDoLog = login
        messagebox.showerror('Dados Incorretos!', 'Try Again')
    else:
        if nivelUsuario == '1':
            janelaNivel1(loginDoLog)

        elif nivelUsuario == '2':
            janelaNivel2(loginDoLog)

        elif nivelUsuario == '3':
            janelaNivel3(loginDoLog)

def btCadastrarFrameCadUsua(dicionario, login, senha, info,usuario):

    '''Botão Cadastrar referente ao Frame de Cadastrar Usuário, recebe dicionario,login,senha e
    um rótulo de informações onde será mostrado o processo realizado'''

    login = login.get()
    senha = senha.get()
    nivel = 1
    adicionar = True

    for elemento in dicionario:
        if elemento == login:
            adicionar = False

    if adicionar == True:
        dicionario[login] = senha, nivel

        log = 'Cadastrou um usuario'
        salvarLog(usuario,log)

        info['text'] = 'Usuário Cadastrado!'
    else:
        log = 'Tentou cadastrar usuário existente'
        salvarLog(usuario,log)

        info['text'] = 'Login já existente'

def btRemoverFrameRemUsua(dicionario, login, info, usuario):

    ''' Botão de Remover refente ao Frame de Remover Usuários, recebe dicionario,login,senha e
    um rótulo de informações onde será mostrado o processo realizado '''

    login = login.get()
    deletar = False
    for elemento in dicionario:
        if login == elemento:
            deletar = True
    if deletar == True:
        del dicionario[login]

        log = 'Removeu usuario'
        salvarLog(usuario,log)

        info['text'] = 'Login Removido'

    else:

        info['text'] = 'Login não encontrado'

        log = 'Tentou removeu usuário inexistente'
        salvarLog(usuario,log)

def btAlterarFrameAltUsua(dicionario, login, nivel, info,usuario):

    ''' Botão de Alterar Nível de Usuário referente ao Frame de Alterar Nível de Usuários, recebe dicionario,login,nivel e
    um rótulo de informações onde será mostrado o processo realizado '''

    login = login.get()
    nivel = nivel.get()
    achei = False

    for chave in dicionario:
        if chave == login:
            senha = dicionario[login][0]
            achei = True

    if achei == True:
        lista = [senha,nivel]
        dicionario[login] = tuple(lista)
        info['text'] = 'Nivel Alterado'

        log = 'Alterou Nivel de Usuário'
        salvarLog(login, log )

    else:
        info['text'] = 'Login não encontrado'

        log = 'Tentou alterar Nível de Usuário'
        salvarLog(usuario,log)

def btCadastrarFunFrameCadProd(dicionario,lb7, c, n, m, v, p, q, usuario):

    ''' Botão de Cadastrar refente ao Frame de Cadastrar Produtos, recebe dicionario,
    todas as informações do produto e um rótudo para mostrar o processo realizado '''


    codigo = c.get()
    nome = n.get()
    marca = m.get()
    validade = v.get()
    preco = p.get()
    quantidade = q.get()
    adiciona = False
    achei = True

    while achei == True:
        if dicionario == {}:
            achei = False
        else:
            for elemento in dicionario:
                if elemento == codigo:

                    log = 'Tentou cadastrar produto já existente'
                    salvarLog(usuario,log
                              )
                    lb7['text'] = 'Codigo Inválido, digite outro codigo'
                    achei = False
            if achei == True:
                adiciona = True
                achei = False

    if adiciona == True:
        dicionario[codigo] = nome, marca, validade, preco, quantidade

        log = 'Cadastrou um novo produto'
        salvarLog(usuario,log)

        lb7['text'] = 'PRODUTO CADASTRADO'

def btRemoverFrameRem(dicionario, codigo, info,usuario):

    ''' Botão de Remover refente ao Frame de Remover Produtos , recebe dicionario, código e
    um rótulo de informações onde será mostrado o processo realizado '''

    codigo = codigo.get()
    deletar = False

    if codigo == '':
        info['text'] = 'REMOVER APENAS COM O CÓDIGO'
    else:
        for produto in dicionario:
            if produto == codigo:
                deletar = True
        if deletar == True:
            del dicionario[codigo]

            log = 'removeu produto'
            salvarLog(usuario,log)

            info['text'] = 'PRODUTO REMOVIDO'
        else:
            info['text'] = 'PRODUTO NÃO ENONTRADO'

            log = 'Tentou remover produto'
            salvarLog(usuario,log)

def btVerificarFrameRem(dicionario, codigo,lb2,lb3,lb4,lb5,lb6,lb7,edNome,edMarca,edValidade,edPreco,edQuantidade,usuario):

    ''' Botão de Verificar Produto refente ao Frame de Atualizar Produtos, recebe dicionario,codigo e
    todos os rótulos de informações onde será mostrado as informações do produto '''

    codigo = codigo.get()

    if codigo in dicionario:

        lb2.place(x = 20, y = 130)
        lb3.place(x = 20, y = 160)
        lb4.place(x = 20, y = 190)
        lb5.place(x = 20, y = 220)
        lb6.place(x = 20, y = 250)
        lb7.place(x = 240, y = 110)

        edNome.place(x = 98, y = 130)
        edMarca.place(x = 98, y = 160)
        edValidade.place(x = 98, y = 190)
        edPreco.place(x = 98, y = 220)
        edQuantidade.place(x = 98, y = 250)
    else:
        lb7['text'] = 'Nenhum Produto Encontrado'

    log = 'Verificou um produto'
    salvarLog(usuario,log)

def btVerificarFrameAtualizar(frame, dicionario, codigo, nome, info,usuario):

    ''' Botão de Verificar refente ao Frame de Atualizar Produto, recebe dicionario, código e
    um rótulo de informações como paramentros, onde será mostrado o processo realizado '''

    lb1 = Label(frame, width = 17, bg = 'Red')
    lb2 = Label(frame, width = 17, bg = 'Red')
    lb3 = Label(frame, width = 17, bg = 'Red')
    lb4 = Label(frame, width = 17, bg = 'Red')
    lb5 = Label(frame, width = 17, bg = 'Red')


    codigo = codigo.get()
    nome = nome.get()
    mostrar = False
    auxiliar = ''

    if nome == '':
        for produto in dicionario:
            if produto == codigo:

                lb1['text'] = dicionario[codigo][0]
                lb2['text'] = dicionario[codigo][1]
                lb3['text'] = dicionario[codigo][2]
                lb4['text'] = dicionario[codigo][3]
                lb5['text'] = dicionario[codigo][4]
                mostrar = True


    elif codigo == '':
        for chave in dicionario:
            if nome == dicionario[chave][0]:
                lb1['text'] = chave
                lb2['text'] = dicionario[chave][1]
                lb3['text'] = dicionario[chave][2]
                lb4['text'] = dicionario[chave][3]
                lb5['text'] = dicionario[chave][4]
                auxiliar = chave
                mostrar = True



    if mostrar == True:

        lb1.place(x = 250, y = 140)
        lb2.place(x = 390, y = 140)
        lb3.place(x = 250, y = 170)
        lb4.place(x = 390, y = 170)
        lb5.place(x = 250, y = 200)
        info['text'] = ''
    else:
        info['text'] = 'NENHUM PRODUTO ENCONTRADO'

    log = 'Verificou o produto'
    salvarLog(usuario,log)

def btAtualizarFrameAtualProd(dicionario, codigo, nome, marca, validade, preco, quantidade, info,usuario):

    ''' Botão de Atualizar Produto refente ao Frame de Atualizar Produtos, recebe dicionario,
    rótulo de informações todas as novas informações referentes ao produto '''

    codigo = codigo.get()
    nome = nome.get()
    marca = marca.get()
    validade = validade.get()
    preco = preco.get()
    quantidade = quantidade.get()


    dicionario[codigo] = nome, marca, validade, preco, quantidade
    info['text'] = 'PRODUTO ATUALIZADO'

    log = 'Atualizou um produto'
    salvarLog(usuario,log)

def btClickFunFrameVoltar(frame,usuario):

    ''' Botão de voltar de qualquer função, seu principal objetivo é destruir
    as telas caso o botão seja clicado '''

    frame.destroy()

    log = 'Retornou a tela anterior'
    salvarLog(usuario,log)

def btGravarArquivos(dicionario, dicionario2, usuario):
    escreverArquivoProdutos(dicionario)
    escreverArquivoUsuario(dicionario2)

    log = 'Salvou as informações no arquivo'
    salvarLog(usuario,log)

#==========================# SEGUNDO PLANO #==========================#

def lerArquivoProdutos():

    dicionarioDeProdutos = {}
    palavra = ''
    listaLinha = []
    chave = ''
    arq = open('dadosProdutos.txt','r')
    ler = arq.readline()
    while ler != '':
        ler = arq.readline()
        for caractere in ler:
            if caractere == ';':
                listaLinha.append(palavra)
                palavra = ''
            elif caractere != '\n':
                palavra += caractere

        while listaLinha != []:
            chave = listaLinha[0]
            del listaLinha[0]
            dicionarioDeProdutos[chave] = tuple(listaLinha)
            listaLinha = []
    arq.close()

    return dicionarioDeProdutos

def lerArquivoUsuarios():

    dicionarioDeUsuarios = {}
    palavra = ''
    listaLinha = []
    chave = ''
    arq = open('NiveisDeAcesso.txt','r')
    ler = arq.readline()
    while ler != '':
        ler = arq.readline()

        for caractere in ler:
            if caractere == ';':
                listaLinha.append(palavra)
                palavra = ''
            elif caractere != '\n':
                palavra += caractere


        while listaLinha != []:
            chave = listaLinha[0]
            del listaLinha[0]
            dicionarioDeUsuarios[chave] = tuple(listaLinha)
            listaLinha = []

    return dicionarioDeUsuarios

def escreverArquivoProdutos(dicionario):

    cont = 0
    arq = open('dadosProdutos.txt','w')
    arq.write('CODIGO;NOME;MARCA;VALIDADE;PREÇO;QUANTIDADE;\n')
    for chave in dicionario:
        arq.write(str(chave))
        arq.write(';')

        while cont < 5:
            arq.write(str(dicionario[chave][cont]))
            arq.write(';')
            cont += 1
        cont = 0
        arq.write('\n')
    arq.close()

def escreverArquivoUsuario(dicionario):

    cont = 0
    arq = open('NiveisDeAcesso.txt','w')
    arq.write('LOGIN;SENHA;NIVEL;\n')
    for chave in dicionario:
        arq.write(str(chave))
        arq.write(';')

        while cont < 2:
            arq.write(str(dicionario[chave][cont]))
            arq.write(';')
            cont += 1
        cont = 0
        arq.write('\n')
    arq.close()

def alterarNivelUsuario():
    nivel = ''
    dicionario = lerArquivoLogin()
    print(dicionario)
    question = input('Qual usuário deseja alterar o nivel: ')
    for chave in dicionario:
        if question == chave:
            print('\n\n1-dono\n2-gerente\n3-caixa\n\n')
            nivel = input('escolha o nivel: ')
            if nivel == '1':
                dicionario[chave][1] = nivel
            elif nivel == '2':
                dicionario[chave][1] = nivel
            elif nivel == '3':
                dicionario[chave][1] = nivel


    escreverArquivoUsuario(dicionario)

def escreverArquivoOrdenado(dicionario, usuario):

    arq = open('ArquivoOrdenado.txt','w')
    arq.write('CODIGO: NOME; MARCA; VALIDADE; PREÇO; QUANTIDADE;\n\n')

    for codigo in sorted(dicionario):
        arq.write(codigo+': ')
        for valor in dicionario[codigo]:
            arq.write(valor+'; ')
        arq.write('\n')

    arq.close()

    log = 'Salvou as informações em um arquivo Ordenado'
    salvarLog(usuario,log)

def salvarLog(login, string):

    ''' Função responsavel por escrever em um arquivo todas as ações realizadas
    por um usuario ao execultar o programa, em que recebe o nome do usuário e a
    ação como parametro '''

    data = str(datetime.now())
    arq = open('log.txt', 'a')

    arq.write(login+' '+string+' '+data+'\n\n')


def criptografaPalavra(string):

    e,n = lerNumeros('chavePrivada')
    e = int(e)
    n = int(n)
    palavraCriptografada = ''
    criptografia = ''
    for elemento in string:
        criptografia = ((ord(elemento)**e)%n)
        palavraCriptografada += str(criptografia)+'&'

    return palavraCriptografada

def lerNumeros(nome):
    n = 0
    e = 0
    stringAux = ''
    arq = open(nome+'.txt', 'r')
    leitura = arq.readline()
    for simbolo in leitura:
        if simbolo != ' ' and simbolo != '\n':
            stringAux += simbolo
        else:
            if e == 0:
                e = int(stringAux)
                stringAux = ''
            else:
                n = int(stringAux)
    return e,n

def criptografarDicionario(dicionario,usuario):

    arq = open('ArquivoCriptografado.txt','w')

    for chave in dicionario:
        criptografia = criptografaPalavra(chave)
        arq.write(criptografia+'!')
        criptografia = ''
        for valor in dicionario[chave]:
            criptografia = criptografaPalavra(valor)
            arq.write(criptografia+'!')
            criptografia = ''
        arq.write('\n')

    arq.close()

    log = 'criptografou o Dicionario de Usuários'
    salvarLog(usuario,log)

dicionarioDeProdutos = lerArquivoProdutos()
dicionarioDeUsuarios = lerArquivoUsuarios()
janelaLogin()

