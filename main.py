
import Adotante
import Adotante_Endereço
import animal
import Formulário
import os


def consulta_animal():
    print('====================================== CONSULTAR DADOS DO ANIMAL ======================================================')
    pesquisa = animal.Animal
    print('DIGITE O INDECE DO ANIMAL QUE DESEJA FAZER A PESQUISA')
    indice_animal=int(input('digite:'))
    pesquisa.consulta_animal(indice_animal)

def cadastrando_adotante():
    print("\n================ Dados Pessoais ================")
    id_adotante = input("\nID do Adotante: ")
    usuario = input("\nNome de Usuário (Limite de 25 dígitos): ")
    senha = input("\nSenha (Limite de 8 dígitos): ")
    nome = input("\nNome Completo: ")
    nascimento = input("\nData de Nascimento AA-MM-DD: ")
    telefone1 = input("\nNúmero de Telefone: ")
    escolha = input("\nAdicionar número de telefone opcional? s/n ")
    if (escolha == "s") or (escolha == "S"):
        telefone2 = input("\nNúmero de Telefone Opcional: ")
    else:
        telefone2 = None
    email = input("\nE-mail: ")
    print("\n================ Dados de Endereço ================")
    id_endereco = input("\nID do Endereço: ")
    logradouro = input("\nLogradouro: ")
    numero = input("\nNúmero da Residência: ")
    bairro = input("\nBairro: ")
    cidade = input("\nCidade: ")
    uf = input("\nUF: ")
    cep = input("\nCEP: ")
    dados_end = Adotante_Endereço.endereco(id_endereco, logradouro, numero, bairro, cidade, uf, cep, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
    dados_ad = Adotante.adotante(id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
    confirmar = input("\nConfirmar cadastro? s/n ")
    if (confirmar == "s") or (confirmar == "S"):
        dados_end.cadastro_endereco(id_endereco, id_adotante, logradouro, numero, bairro, cidade, uf, cep)
        dados_ad.cadastro_adotante(id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
    else:
        print("\n===================== Os dados não foram salvos =====================")

def consultando_adotantes():
    print("\n================ Dados Pessoais dos Adotantes ================\n")
    selecionar_adotantes = Adotante.adotante.consultar_adotantes()
    print("\n================ Dados de Endereço dos Adotantes ================\n")
    selecionar_enderecos = Adotante_Endereço.endereco.consultar_enderecos()

def alterar_adotantes_pessoais():
    consultando_adotantes()
    id_adotante = int(input("\nDigite o índice do adotante: "))
    alterar = Adotante.adotante.selecionar_adotantes(id_adotante)
    print("\nUsuário de ID", id_adotante, "selecionado")
    nome = input("\nNovo nome: ")
    nascimento = input("\nNova data de nascimento: ")
    telefone1 = input("\nNovo telefone: ")
    escolha = input("\nDeseja alterar/adicionar número de telefone opcional? s/n ")
    if (escolha == "s") or (escolha == "S"):
        telefone2 = input("\nNúmero de telefone opcional: ")
    else:
        telefone2 = None
    email = input("\nNovo e-mail: ")
    usuario = input("\nNovo nome de usuário: ")
    senha = input("\nNova senha: ")
    confirmar_dad = input("\nConfirmar alterações? s/n ")
    if (confirmar_dad == "s") or (confirmar_dad == "S"):
        alterar.atualizar_adotantes(id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
    else:
        print("\n===================== Os dados não foram alterados =====================\n")

def alterar_adotantes_enderecos():
    consultando_adotantes()
    id_endereco = int(input("\nDigite o índice de endereço do adotante: "))
    alterar_endereco = Adotante_Endereço.endereco
    print("\nUsuário do ID de endereço", id_endereco, "selecionado")
    logradouro = input("\nNovo logradouro: ")
    numero = input("\nNovo número de residência: ")
    bairro = input("\nNovo bairro: ")
    cidade = input("\nNova cidade: ")
    uf = input("\nNovo UF: ")
    cep = input("\nNovo CEP: ")
    confirmar_end = input("\nConfirmar alterações? s/n ")
    if (confirmar_end == "s") or (confirmar_end == "S"):
        alterar_endereco.atualizar_enderecos(id_endereco, id_endereco, logradouro, numero, bairro, cidade, uf, cep)
    else:
        print("\n===================== Os dados não foram alterados =====================")

def excluir_adotantes():
    consultando_adotantes()
    id_adotante = int(input("\nDigite o índice do usuário a ser deletado: "))
    deletar = Adotante.adotante.selecionar_adotantes(id_adotante)
    deletar_end = Adotante_Endereço.endereco
    print("\nTem certeza que deseja deletar o usuário de ID", id_adotante, "? s/n ")
    confirmar = input("> ")
    if (confirmar == "s") or (confirmar == "S"):
        deletar.deletar_adotantes(id_adotante)
        deletar_end.deletar_enderecos(id_adotante)
    else:
        print("\n===================== Os dados não foram excluídos =====================")

def cadastroanimal():

    print('========================================= CADASTRE OS DADOS DO ANIMAL ================================================================')
    print('')


    # n sei ara q serve esse id exame
    print('digite o exame valor a enserir terar de ser inteiro')
    id_exame = int(input('digite:'))

    print('')


    # nome do animal se tiver
    print('o animal possui nome? s/n')
    verino = input('digite:')

    if (verino == 's') or (verino == 'S'):
        print('digite o nome que esta na coleira:')
        nomeanimal = input('digite:')

    elif (verino == 'n') or (verino == 'N'):
        nomeanimal='N'


    else:
        print('ERRO')
        print('NENHUMA DAS OPÇÕES FOI SELECINADAS')
        print('volte ao menu com a tecla ()')
    print('')


    # cor do animal
    print('digite a cor do animal')
    cor =input("digite:")
    print('')


    # porte do animal
    print(' porte do animal:\n piqueno porte digite: (P)\n medio porte digite: (M)\n auto porte digite (A)')
    veriporte = input('digite:')

    if (veriporte == 'p') or (veriporte == 'P'):

        porte = 'P'

    elif (veriporte == 'm') or (veriporte == 'M'):

        porte = 'M'

    elif (veriporte == 'a') or (veriporte == 'A'):

        porte = 'A'


    else:
        print('ERRO')
        print('NENHUMA DAS OPÇÕES FOI SELECINADAS')
        print('volte ao menu com a tecla ()')

    print('')

    # RAÇA DO ANIMAL
    print('digite a raça/especie do animal')
    raca = input('digite:')
    print('')


    # idade estimada do animal
    print('idade estimada do animal')
    idade =input('digite:')
    print('')


    # DISPONIVEL PARA DOAÇAO

    print('disponivel para a doeção? S/N')
    veridis=input('digite:')

    if (veridis == 's') or (veridis == 'S'):
        disponivel = 'S'


    elif (veridis == 'n') or (veridis == 'N'):

        disponivel = 'N'


    else:
        print('ERRO')
        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')



# adotado?
    print('o animal ja foi adotado? S/N')
    adotado = input('digite:')
    print('')


    # deficincia

    print('o animal possui alguma deficiencia fisica? s/n')
    veridef = input('digite:')

    if (veridef == 's') or (veridef == 'S'):

        deficiente ='S'

    elif (veridef == 'n') or (veridef == 'N'):
        deficiente = 'N'

    else:
        print('ERRO')

        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')


    # animal castardo
    print('animal é castrado? S/N')
    castrado =input ('digite:')
    print('')


    #  exameas animal
    print('o animal a fez algum exame? S/N')
    veriex = input('digite:')

    if (veriex == 's') or (veriex == 'S'):
        print('quantos?')
        exames = int(input(('digite:')))

    elif (veriex == 'n') or (veriex == 'N'):
        exames = 0

    else:
        print('ERRO')
        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')


    # local que o animal foi encotrado
    print('qual foi o local que o animal foi encontrado/resgatado')
    local_encontro = input('digite:')
    print('')


    # data que o animal foi encontrado

    print('data que o animal foi encotrado')
    data_encontro =input('digite:')
    print('')
    infor_animal = animal.Animal(id_exame, nomeanimal, cor, porte, raca,idade, disponivel, adotado, deficiente,castrado, exames, local_encontro, data_encontro)

    print('deseja salva? S/N')
    veriseiv=input('digite:')
    if(veriseiv=='s') or (veriseiv=='S'):

        infor_animal.cadastrar(id_exame,nomeanimal,cor,porte,raca,idade,disponivel,adotado,deficiente,castrado,exames,local_encontro,data_encontro)
        print('CADASTRO C0NCLUIDO COM SUCESSO !!')

    else:
        print("\n===================== Os dados não foram salvos =====================")

def excluir_animal():
    print('================================================= EXCLUIR CADASTRO DE ANIMAL ================================================================')
    print('digite o indece do animal que deseja excluir')
    id_animal=int(input('digite'))
    obj_excluir=animal.Animal.deletar_aninal(id_animal)
    obj_excluir=animal.Animal
    print('TEM CERTEZA QUE DESEJA (EXCLUIR0) ESSE DADOS? S/N')
    verideletar=input('digite:')

    if (verideletar=='s') or (verideletar=='S'):
        obj_excluir.deletar_aninal(id_animal)
        print("=====================  DADOS EXCLUIDOS COM SUCESSO  =====================")


    elif (verideletar == 'n') or (verideletar == 'N'):
        print("===================== OS DADOS NÃO FORAM EXCLUIDOS =====================")
    else:
        print('ERRO')
        print('NENHUMA DAS OPÇÕES INDICADAS FOI RESPEITADAS')

def atualizaranimais():
    atualizar = animal.Animal
    print('========================================== ATUALIZAR OS DADOS DO ANIMAL ================================================================')
    print('')

    print('digite o indece do animal que pretende fazer a modificação')
    id_animal=int(input('digite:'))
    print('')
    print('FAÇA AS MODIFCAÇÕES A SEGUIR')
    # print(' modificar (ID_EXAME) - (PRECIONE 1)\n modifcar (NOME) - (PRECINE 2 )\n modificar (COR) - (PRECIONE 3)\n modifcar (PORTE) - (PRECIONE 4)\n modificar (RAÇA) - (precione 5)\n modificar (IDADE ESTIMADA) - (PRECIONE 6)\n modicar (DESPONIVEL PARA ADOÇÃO) - (PRECIONE 7)\n modificar (ADOTADO) - (PRECIONE 8)\n modificar (DEFICENTE FISICO) - (PRECIONE 9)\n modificar (CASTRADO) - (PRECIONE 10)\n modicar (QUANTIDADE DE EXAMES) - (PRECIONE 11)\n modifcar (LOCAL ENCONTRADO) - (PRECIONE 12)\n modificar (DATA ENCONTRADO) - (PRECIONE 13) ')
    print('')

    # n sei ara q serve esse id exame
    print('digite o exame valor a enserir terar de ser inteiro')
    id_exame = int(input('digite:'))

    print('')

    # nome do animal se tiver
    print('o animal possui nome? s/n')
    verino = input('digite:')

    if (verino == 's') or (verino == 'S'):
        print('digite o nome que esta na coleira:')
        nomeanimal = input('digite:')

    elif (verino == 'n') or (verino == 'N'):
        nomeanimal = 'N'


    else:
        print('ERRO')
        print('NENHUMA DAS OPÇÕES FOI SELECINADAS')
        print('volte ao menu com a tecla ()')
    print('')

    # cor do animal
    print('digite a cor do animal')
    cor = input("digite:")
    print('')

    # porte do animal
    print(' porte do animal:\n piqueno porte digite: (P)\n medio porte digite: (M)\n auto porte digite (A)')
    veriporte = input('digite:')

    if (veriporte == 'p') or (veriporte == 'P'):

        porte = 'P'

    elif (veriporte == 'm') or (veriporte == 'M'):

        porte = 'M'

    elif (veriporte == 'a') or (veriporte == 'A'):

        porte = 'A'


    else:
        print('ERRO')
        print('NENHUMA DAS OPÇÕES FOI SELECINADAS')
        print('volte ao menu com a tecla ()')

    print('')

    # RAÇA DO ANIMAL
    print('digite a raça/especie do animal')
    raca = input('digite:')
    print('')

    # idade estimada do animal
    print('idade estimada do animal')
    idade = input('digite:')
    print('')

    # DISPONIVEL PARA DOAÇAO

    print('disponivel para a doeção? S/N')
    veridis = input('digite:')

    if (veridis == 's') or (veridis == 'S'):
        disponivel = 'S'


    elif (veridis == 'n') or (veridis == 'N'):

        disponivel = 'N'


    else:
        print('ERRO')
        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')
    # adotado?
    print('o animal ja foi adotado? S/N')
    adotado = input('digite:')
    print('')
    # deficincia
    print('o animal possui alguma deficiencia fisica? s/n')
    veridef = input('digite:')
    if (veridef == 's') or (veridef == 'S'):
        deficiente = 'S'
    elif (veridef == 'n') or (veridef == 'N'):
        deficiente = 'N'
    else:
        print('ERRO')

        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')
    # animal castardo
    print('animal é castrado? S/N')
    castrado = input('digite:')
    print('')
    #  exameas animal
    print('o animal a fez algum exame? S/N')
    veriex = input('digite:')
    if (veriex == 's') or (veriex == 'S'):
        print('quantos?')
        exames = int(input(('digite:')))
    elif (veriex == 'n') or (veriex == 'N'):
        exames = 0
    else:
        print('ERRO')
        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')
    # local que o animal foi encotrado
    print('qual foi o local que o animal foi encontrado/resgatado')
    local_encontro = input('digite:')
    print('')
    # data que o animal foi encontrado
    print('data que o animal foi encotrado')
    data_encontro = input('digite:')
    print('')
    print('DESEJA CONFIRMAR ATUALIZAÇÃO ? S/N')
    vericonfime=input('digite:')
    if (vericonfime=='s') or (vericonfime=='S'):
        atualizar.atualizardadosanimais(id_animal,id_exame, nomeanimal,cor,porte,raca,idade,disponivel,adotado,deficiente,castrado,exames,local_encontro,data_encontro)
        print('')
        print('================================================= ATUALIZAÇÃO SALVA COM SUCESSO  ================================================================')
    else:
        print('================================================= ATUALIZAÇÃO DESCARTADA ================================================================')

    # PARA ATUALIR S DATOS DO ANIMAL VOU FAZER UM MENU E PEDIR PARA O USURARRIO DIGITAR O USUARIO DIGITAR OPÇAO 1 PARA MUDAR O NOME, DOIS PARA MDAR A COR ....,
    # DEPOIS VOU PERGUTAR SE ELE DESEJA FAZER OUTRA MODIFICAÇAO ELE VAI VOUTAR PARA ESSE MENU DAS OPÇOES DE ESCOLHA DA COLUNA E ELE VAI ESCOLHER OUTRA A PUTRA COLUNA QUE E LE QUE
    # MODIFCAR , E SE ELE NAO QUISER MODIFICAR MAIS NADA VAI PERGUNTAR SE ELE DESEJA FAZER O SALVAMENTO DA ATUALIZAÇAO FEITA DPS EU VOU FAZER A REFERENCIA DAAS VARIAVEIS A MINHA
    # FUNÇAO DA CLASSE ANIMAL

def logar():
    print("\n===================== Tela de Login =====================")
    usuario = input("\nUsuário: ")
    senha = input("\nSenha: ")
    Adotante.adotante.login(usuario, senha)

def preenchimento_formulario():
    print("\n================ Formulário de Adoção ================")
    moradores = input("\nCom quem você mora? ")
    motivo = input("\nPor que quer adotar um animal? ")
    verificar_animais = input("\nPossui outros animais? s/n ")
    if (verificar_animais == "s") or (verificar_animais == "S"):
        possui_animais = "S"
        animais = input("Quais? ")
    else:
        possui_animais = "N"
        animais = "Nenhum"
    profissao = input("\nO que faz/Com o que trabalha? ")
    moradia = input("\nMora em casa ou apartamento? ")
    favor_adocao = input("\nTodo em casa estão a favor da adoção? s/n ")
    verificar_despesas = input("\nAcha que terá condição de viabilizar todas as despesas necessárias para garantir o bem estar do animal?\n(Vacinas. castração, cuidados médicos em caso de doença...) s/n ")
    if (verificar_despesas == "s") or (verificar_despesas == "S"):
        despesas = "S"
    else:
        despesas = "N"
    rotina = input("\nQual sua rotina? ")
    tempo_fora = input("\nQuanto tempo você fica fora de casa? ")
    confirmar = input("\nDeseja enviar as respostas? s/n ")
    if (confirmar == "s") or (confirmar == "S"):
        Formulário.formulario.formulario_perguntas(moradores, motivo, possui_animais, animais, profissao, moradia, favor_adocao, despesas, rotina, tempo_fora)
    else:
        print("\n===================== O formulário não foi enviado =====================")


def menu_funcionarioLI():
    print("Deseja realizar qual das opções abaixo? ")
    print("1 = Adicionar um novo cliente")
    print("2 = Consultar dados de clientes cadastrados")
    print("3 = Alterar dados de clientes")
    print("4 = Deseja Deletar Usuários?")
    print("5 = Sair do Programa")
    print("6 = Voltar")


def menu_adotanteLI():
    print("Deseja realizar qual das opções abaixo? ")
    print("")
    print("1 = Consultar seus dados?")
    print("2 = Alterar seus dados?")
    print("3 = Acessar Questionário")
    print("4 = Sair do Programa")
    print("5 = Voltar")


def menu_animal():
    print("Deseja realizar qual das opções abaixo?")
    print('')
    print("1 = Adicionar um novo Animal")
    print("2 = Consultar dados de Animais Cadastrados")
    print("3 = Alterar dados de Animais")
    print("4 = Sair do Programa")


def menu_parte_animal():
    print("Deseja realizar qual das opções abaixo?")
    print('')
    print("2 = Consultar dados de Animais Cadastrados")
    print("3 = Sair do Programa")
    print("")
    print("===========Alerta=========")
    print("NO MOMENTO VOCÊ PODE FAZER SOMENTE UMA OPÇÃO")


def Menu_principal():
    print("========================================================")
    print('============== MENU=============')
    print('\n')
    print("MENU DE CLIENTE: Digite 1")
    print("MENU DE ANIMAL: Digite 2")
    print("0 = Volte ao Sistema de Login")


def Menu():
    print("========================================================")
    print('============== SISTEMAS LOGINS =============')
    print('\n')
    print("SISTEMA LOGIN DE FUNCIONÁRIO: DIGITE 1 ")
    print("SISTEMA LOGIN DE CLIENTE: DIGITE 2 ")

dnv_login = 100
abri_menu = 0
abri_funcionario = 70
abri_cliente = 50
while abri_menu == 0:

    Menu()
    direcao = int(input("> "))
    while dnv_login == 100:
        if (direcao == 1):
            login1 = input("Digite o email:")
            senha1 = input('Digite a senha')
            if (login1 == 'empresa@gmail.com' and senha1 == '123456'):
                while abri_funcionario == 70:
                    os.system("cls")
                    print("=============Olá Funcionário=============")
                    Menu_principal()
                    escolha = int(input("> "))
                    if (escolha == 1):
                        os.system("cls")
                        menu_funcionarioLI()
                        opcao1 = int(input(">"))

                        if (opcao1 == 1):
                            os.system("cls")
                            cadastrando_adotante()
                            abri_funcionario = 70

                        elif (opcao1 == 2):
                            os.system("cls")
                            consultando_adotantes()
                            os.system("pause")
                            abri_funcionario = 70

                        elif (opcao1 == 3):
                            os.system("cls")
                            print('====Sistemas de Alteração de Dados=====')
                            print('')
                            print('Qual das duas opções?')
                            print("")
                            print("Atualizar Dados Pessoais de Adotante: Digite 1")
                            print('Atualizar somente o Endereço: Digite qualquer número')
                            Resposta = input("Resposta: ")
                            while Resposta != 1 or Resposta != 2:
                                if (Resposta == 1):
                                    alterarando_adotantes_pessoais()
                                    abri_funcionario = 70

                                elif (Resposta == 2):
                                    alterarando_adotantes_enderecos()
                                    abri_funcionario = 70

                        elif (opcao1 == 4):
                            os.system("cls")
                            excluindo_adotantes()
                            abri_funcionario = 70
                        elif (opcao1 == 5):
                            exit()

                    elif (escolha == 2):
                        os.system("cls")
                        menu_animal()
                        opcao2 = int(input("Digite:"))

                        if (opcao2 == 1):
                            os.system("cls")
                            cadastroanimal()
                            print('')
                            input("Digite 1 : Para Voltar ao Menu")

                        elif (opcao2 == 2):
                            os.system("cls")
                            print("sem informações ainda")

                        elif (opcao2 == 3):
                            os.system("cls")
                            print("sem informações ainda")
                        elif (opcao1 == 4):
                            exit()

                if (escolha == 0):
                    print("voltando...")
                    os.system("pause")
                    abri_menu == 0


            elif (login1 != 'empresa@gmail.com' and senha1 != '123456'):
                dnv_login = 100
                os.system("cls")

        elif (direcao == 2):
            os.system("cls")
            logar()
            while abri_cliente == 50:
                print("=============Olá Cliente=============")
                # coloque aqui a função de login de cliente
                Menu_principal()
                caso = int(input("> "))
                if (caso == 1):
                    os.system("cls")
                    while abri_cliente == 50:
                        menu_adotanteLI()
                        x = int(input("> "))
                        if (x == 1):
                            input("esta aqui:")
                            abri_cliente = 50

                        elif (x == 2):
                            input("ta aqui então")
                            abri_cliente = 50

                        elif (x == 3):
                            preenchimento_formulario()
                            abri_cliente = 50

                        elif (x == 4):
                            exit()

                elif (caso == 2):
                    os.system("cls")
                    menu_parte_animal()  # DÊ UMA OLHADA LÁ NO MENU DESTA PARTE
                    z = int(input(">  "))
                    if (z == 1):
                        print("acrescentar")
                        # colocar consulta de dados de animais aqui
                        abri_cliente = 50

                    elif (z == 2):
                        print("acrescentar")
                        # colocar adoção de animais aqui
                        abri_cliente = 50
                    elif (z == 3):
                        exit()