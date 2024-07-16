import os #Esse import permite com que limpe a tela do terminal quando chamado

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False}, {"nome":"Pizza Suprema", "categoria":"Pizza", "ativo":True},
                {"nome":"Cantina", "categoria":"Italiano", "ativo":False}]

def exibir_nome_programa():
    """ Essa função retorna o nome do programa"""
    print("Sabor express\n")

def exibir_opcoes():
    """ Nesta função é exibida as opções do programa"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    """ Função responsável para finalizar app e exibir mensagem """
    exibir_subtitulo("App finalizado")

def voltar_ao_menu():
    """ Nesta função é possível retornar ao menu de opções
    
    Input:
    - Voltar às opções
    
    """
    input("\nDigite uma tecla para voltar ao menu principal ")
    main()

def opcao_invalida():
    """ Caso seja inserido um valor inválido de acordo com requisitos da função exibir_opcoes, o programa volta ao início """
    print("Opção inválida!\n")
    voltar_ao_menu()

def exibir_subtitulo(texto):
    """ Nesta função existe o limpa tela e aparece a mensagem como parametro de texto
    
    Limpa tela: 
    - os.system("cls")

    """
    os.system("cls")
    linha = "-" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """ Função resposável para cadastrar novo restaurante
     
    Inputs: 
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante à lista de restaurantes

     """
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_restaurante = {"nome": nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu()

def listar_restaurantes():
    """ Nesta função é a exibição do programa e é verificado se o restaurante está como ativo ou não no looping FOR"""
    exibir_subtitulo("Listando os restaurantes\n")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(22)} | {"Status"}")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | - {categoria.ljust(20)} | - {ativo}")

    voltar_ao_menu()

def alternar_estado_restaurante():
    """ Nesta função é onde é possível alterar o status do restaurante

    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    """
    exibir_subtitulo("Alternando estado do restaurante ATIVO/DESATIVADO")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} não foi encotrado")

    voltar_ao_menu()

def escolher_opcao():
    """ Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    """
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """ Função principal que inicia o programa """
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()