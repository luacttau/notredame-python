from listas import lista_unidades, lista_lembretes, lista_remedios, lista_consultas, lista_notas


# FUNÇÃO "EMERGÊNCIA": escolha do endereço para a solicitação de uma emergência.

def emergencia():
    while True:
        try:
            print("\n=== EMERGÊNCIA ===\n")
            print("1. Localização atual")
            print("2. Endereço padrão")
            print("3. Novo endereço")
            print("4. Voltar\n")

            opcao_emergencia = int(input("Selecione uma das opções acima: "))

            if opcao_emergencia == 1 or opcao_emergencia == 2:
                print("\nConcluído. Estamos a caminho.")
                break

            elif opcao_emergencia == 3:
                novo_endereco = input("Informe o novo endereço: ")
                print("\nConcluído. Estamos a caminho.")
                break

            elif opcao_emergencia == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Opção inválida, digite um número de 1 à 4")



# FUNÇÃO "DIÁRIO": para que o paciente mantenha controle das próprias informações.

def diario():
    while True:
        try:
            print("\n=== DIÁRIO ===\n")
            print("1. Lembretes")
            print("2. Remédios")
            print("3. Consultas")
            print("4. Anotações")
            print("5. Voltar\n")

            opcao_diario = int(input("Selecione uma das opções acima: \n"))

            if opcao_diario == 1:
                while True:
                    try:

                        print("1. Meus lembretes")
                        print("2. Adicionar lembrete")
                        print("3. Voltar\n")
                        opcao_lembretes = int(input("Selecione uma das opções acima: \n"))

                        if opcao_lembretes == 1:
                            if not lista_lembretes:
                                print("\nNão há lembretes.")
                                break

                            else:
                                print(lista_lembretes)
                                break

                        elif opcao_lembretes == 2:
                            novo_lembrete = input("Novo lembrete: ")
                            lista_lembretes.append(novo_lembrete)
                            print("\nLembrete adicionado com sucesso!")
                            break

                        elif opcao_lembretes == 3:
                            break

                        else:
                            raise ValueError
                    except ValueError:
                        print("Opção inválida, digite um número de 1 à 3")

            elif opcao_diario == 2:
                while True:
                    try:
                        print("1. Meus remédios")
                        print("2. Cadastrar novo remédio")
                        print("3. Voltar\n")

                        opcao_remedios = int(input("Selecione uma das opções acima: \n"))

                        if opcao_remedios == 1:
                            if not lista_remedios:
                                print("\nNão há remédios cadastrados")
                                break

                            else:
                                print(lista_remedios)
                                break

                        elif opcao_remedios == 2:
                            novo_remedio = input("\nNovo remédio: ")
                            lista_remedios.append(novo_remedio)
                            print(f'\nAdicionado um novo remédio. ({novo_remedio})')
                            break

                        elif opcao_remedios == 3:
                            break

                        else:
                            raise ValueError
                    except ValueError:
                        print("Opção inválida, digite um número de 1 à 3")

            elif opcao_diario == 3:
                while True:
                    try:
                        print("1. Minhas consultas")
                        print("2. Agendar nova consulta")
                        print("3. Voltar\n")

                        opcao_consultas = int(input("Selecione uma das opções acima: \n"))

                        if opcao_consultas == 1:
                            if not lista_consultas:
                                print("\nNão há consultas marcadas")
                                break

                            else:
                                print(lista_consultas)
                                break

                        elif opcao_consultas == 2:
                                nova_consulta = input("\nNova consulta: ")
                                lista_consultas.append(nova_consulta)
                                print("\nConsulta agendada com sucesso!")
                                break

                        elif opcao_consultas == 3:
                            break

                        else:
                            raise ValueError

                    except ValueError:
                        print("Opção inválida, digite um número de 1 à 3")

            elif opcao_diario == 4:
                while True:
                    try:
                        print("1. Minhas anotações")
                        print("2. Nova nota")
                        print("3. Voltar\n")

                        opcao_notas = int(input("Selecione uma das opções acima: \n"))

                        if opcao_notas == 1:
                            if not lista_notas:
                                print("\nNão há anotações.")
                                break

                            else:
                                print(lista_notas)
                                break

                        elif opcao_notas == 2:
                                nova_nota = input("Nova nota: ")
                                lista_notas.append(nova_nota)
                                print("\nAnotação salva com sucesso!")
                                break

                        elif opcao_notas == 3:
                            break

                        else:
                            raise ValueError
                    except ValueError:
                        print("Digite um número de 1 à 3")
            elif  opcao_diario == 5:
                break
            else:
                raise ValueError
        except ValueError:
                print("Digite um número de 1 à 5")




# FUNÇÃO "TRIAGEM": benefício para atendimento mais rápido no pronto-socorro

def triagem():
    while True:
        try:
            print("\n=== PRONTO-SOCORRO ===\n")

            print("Deseja prosseguir com a triagem?")

            opcao_triagem = input("    SIM | NÃO    \n").upper()

            if opcao_triagem == "SIM" or opcao_triagem == "S":
                while True:
                    try:
                        print("Selecione uma das unidades abaixo: \n")
                        for i in range(len(lista_unidades)):
                            print(i, lista_unidades[i])

                        unidade_triagem = int(input(""))
                        if unidade_triagem < 0 or unidade_triagem > 5:
                            raise ValueError
                        sintomas = input("Descreva o que está sentindo: ")
                        print("\nEncaminhado para a unidade selecionada.\n")
                        break

                    except ValueError:
                        print("Opção inválida, digite um número de 0 à 5")
                break
            elif opcao_triagem == "NAO" or opcao_triagem == "N" or opcao_triagem == "NÃO":
                break
            else:
                raise TypeError
        except TypeError:
            print("Digite 'SIM ou 'NAO'")




# MENU GERAL

while True:
    try:
        print("\n=== DASHBOARD ===\n")
        print("1. Emergência")
        print("2. Diário")
        print("3. Pronto Socorro")
        print("4. Sair\n")
        acesso = int(input("Digite a opção desejada: "))


        if acesso == 1:
            emergencia()
        elif acesso == 2:
            diario()
        elif acesso == 3:
            triagem()
        elif acesso == 4:
            break

        else:
            raise ValueError
    except ValueError:
        print("Opção inválida, digite um número de 1 à 4")
