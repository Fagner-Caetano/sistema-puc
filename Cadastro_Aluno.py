lista = []  # aqui sera armazendo os dados dos alunos

opcao = 1
while opcao != 0:

    print(' ----- Menu Principal -----\n')

    print(' [1] Gerenciar estudantes')
    print(' [2] Gerenciar professores')
    print(' [3] Gerenciar disciplinas')
    print(' [4] Gerenciar turmas')
    print(' [5] Gerenciar matriculas')
    print(' [0] Sair do Sistema\n')
    opcao = int(input("Informe a opção desejada: "))
    print('----------------------------')

    if opcao == 1:
        print('\n===Estudantes===\n')
        print(' [1] Incluir')
        print(' [2] Listar')
        print(' [3] Excluir')
        print(' [4] Alterar')
        print(' [0] Voltar ao menu principal.\n')
        acao = int(input('Informe a ação desejada: '))

        if acao == 1:
            print('\n=== INCLUIR ===\n')

            nome = str(input('Informe o nome: '))  # coleta o nome do aluno

            lista.append(nome)  # adiciona o nome do aluno na lista

            print()

        elif acao == 2:
            print('\n=== Listar Nomes ===\n')
            if len(lista) == 0:
                print('A lista está vazia\n')
            else:
                for item in lista:  # FOR IN = para cada elementro dentro da lista, sistema vai rodar 1x
                    # Se a lista tiver o tamanho != de 0 ele vai pegar cada um dos estudantes cadastrados e listar na tela
                    print(item + '\n')

        elif acao == 3:
            print('\n=== Excluir ===\n')
            print('='*20)
            print('Em Desenvolvimento')
            print('='*20)

        elif acao == 4:
            print('\n=== Alterar ===\n')
            print('='*20)
            print('Em Desenvolvimento')
            print('='*20)
    elif opcao == 2:
        print('\nEM DESENVOLVIMENTO\n')
    elif opcao == 3:
        print('\nEM DESENVOLVIMENTO\n')
    elif opcao == 4:
        print('\nEM DESENVOLVIMENTO\n')
    elif opcao == 5:
        print('\nEM DESENVOLVIMENTO\n')
    elif opcao == 0:
        print('\nEM DESENVOLVIMENTO\n')
        break

print('Atendimento encerrado')
