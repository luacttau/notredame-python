from listas import lista_unidades, lista_lembretes, lista_remedios, lista_consultas, lista_notas


# FUNÇÃO "EMERGÊNCIA": escolha do endereço para a solicitação de uma emergência.
def emergencia():
    print("\n=== EMERGÊNCIA ===\n")
    print("1. Localização atual")
    print("2. Endereço padrão")
    print("3. Novo endereço\n")
    opcao_emergencia = int(input("\nSelecione uma das opções acima: "))

    if opcao_emergencia == 1 or opcao_emergencia == 2:
                print("\nConcluído. Estamos a caminho.")
    elif opcao_emergencia == 3:
                novo_endereco = input("Informe o novo endereço: ")
                print("Concluído. Estamos a caminho.")
    else:
        print("ERRO")


# FUNÇÃO "DIÁRIO": para que o paciente mantenha controle das próprias informações.
def diario():
    print("\n=== DIÁRIO ===\n")
    print("1. Lembretes")
    print("2. Remédios")
    print("3. Consultas")
    print("4. Anotações\n")
    opcao_diario = int(input("Selecione uma das opções acima: \n"))

    if opcao_diario == 1:
        print("1. Meus lembretes")
        print("2. Adicionar lembrete")
        opcao_lembretes = int(input("Selecione uma das opções acima: \n"))

        if opcao_lembretes == 1:
            print(lista_lembretes)
        elif opcao_lembretes == 2:
            novo_lembrete = input("Novo lembrete: ")
        else:
            print("Opção inválida")

    if opcao_diario == 2:
        print("1. Meus remédios")
        print("2. Cadastrar novo remédio")
        opcao_remedios = int(input("Selecione uma das opções acima: \n"))

        if opcao_remedios == 1:
            print(lista_remedios)
        elif opcao_remedios == 2:
            novo_remedio = input("Novo remédio: ")
        else:
            print("Opção inválida")

    if opcao_diario == 3:
        print("1. Minhas consultas")
        print("2. Agendar nova consulta")
        opcao_consultas = int(input("Selecione uma das opções acima: \n"))

        if opcao_consultas == 1:
                print(lista_consultas)
        elif opcao_consultas == 2:
                nova_consulta = input("Nova consulta: ")
        else:
                print("Opção inválida")

    if opcao_diario == 4:
        print("1. Minhas anotações")
        print("2. Nova nota")
        opcao_notas = int(input("Selecione uma das opções acima: \n"))

        if opcao_notas == 1:
                print(lista_notas)
        elif opcao_notas == 2:
                nova_nota = input("Nova nota: ")
        else:
                print("Opção inválida")
    else:
        print("ERRO")


# FUNÇÃO "TRIAGEM": benefício para atendimento mais rápido no pronto-socorro
def triagem():
    print("\n=== PRONTO-SOCORRO ===\n")
    print("Deseja prosseguir com a triagem?")
    opcao_triagem = input("    SIM | NÃO    \n").upper()

    if opcao_triagem == "SIM":
        print("Selecione uma das unidades abaixo: \n")
        print(lista_unidades)
        unidade_triagem = input("")
        sintomas = input("Descreva o que está sentindo: ")
        print("\nEncaminhado para a unidade selecionada.\n")


# MENU GERAL

while True:
    print("\n=== DASHBOARD ===\n")
    print("1. Emergência")
    print("2. Diário")
    print("3. Pronto Socorro")
    print("4. Sair")
    acesso = int(input("Digite a opção desejada: "))

    if acesso == 1:
        while True:
            emergencia()
            sair = input("\nVoltar ao menu principal?\n [SIM/NAO] ").upper()
            if sair != "NAO":
                break

    elif acesso == 2:
        while True:
            diario()
            sair = input("\nVoltar ao menu principal?\n [SIM/NAO] ").upper()
            if sair != "NAO":
                break

    elif acesso == 3:
        while True:
            triagem()
            sair = input("\nVoltar ao menu principal?\n [SIM/NAO] ").upper()
            if sair != "NAO":
                break

    elif acesso == 4:
        break

    else:
        print("Opção inválida")