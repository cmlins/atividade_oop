from Aluno import Aluno

class Funcoes:

    def mostrar_opcoes(lista_opcoes, nome_login):
        print(f"Olá! Seja bem-vinde {nome_login}! Escolha uma opção:")
        for opcao in lista_opcoes:
            print(opcao)

    def mostrar_pessoas(lista_pessoas):
        for pessoa in lista_pessoas:
            print(f"{pessoa.nome} - {pessoa.matricula}")

    def incluir_aluno(lista_alunos):
        while True:
            nome_aluno = input("Digite o nome do Aluno\n")
            matricula_aluno = input("Digite a matrícula do Aluno\n")
            documento_aluno = input("Digite o número do documento\n")
            aluno = Aluno(nome=nome_aluno,documento=documento_aluno,matricula=matricula_aluno) #Incluindo o documento no momento do construtor
            lista_alunos.append(aluno) #Insere um aluno na lista
            print(f"O aluno {aluno.nome} foi inserido!")  #Mostra para o usuário que o append foi feito      
            
            #Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais um aluno? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "S" or controle_insert == "s":
                    if controle_insert.upper() == "N":
                        print("Saíndo da inclusão de alunos...")
                        break
                        

    def excluir_aluno(lista_alunos):
        while True:
            iterador_alunos = 0 
            max_alunos = len(lista_alunos)
            while iterador_alunos < max_alunos: #Outra forma de fazer loop em lista
                print(f"Índice - {iterador_alunos} - {lista_alunos[iterador_alunos].nome}")
                iterador_alunos += 1
            input_do_usuario = input("Digite um valor para a exclusão do aluno \n")
            
            if input_do_usuario.isnumeric():
                aluno_selecionado = int(input_do_usuario) #Solicite para o usuário o índice
                if aluno_selecionado in range(0, max_alunos):
                    aluno_excluido = lista_alunos.pop(aluno_selecionado) #pop para excluir o aluno e retornar o objeto excluído
                    print(f"O aluno {aluno_excluido.nome} foi excluído") #mostra para o usuário
                    #Solicitando a saída para o usuário    
                    controle_exclusao = input("Deseja sair da exclusão? (Digite 's' ou 'S' para sair) \n")
                    if len(controle_exclusao) == 1:
                        if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
                            if controle_exclusao.upper() == "S":
                                print("Saíndo da exclusão de alunos...")
                                break
                else:
                    print("Esse valor não existe")
            else:
                print("Esse valor deve ser um número")

    def detalhar_aluno(lista_alunos):
        while True:
            nome_aluno_pesquisado = input("Digite o nome do aluno a ser pesquisado \n")
            controle_iteracao = 0
            for aluno in lista_alunos:
                if nome_aluno_pesquisado.upper() in aluno.nome.upper():
                    print(f"O aluno {aluno.nome} com a {aluno.matricula} e o documento {aluno.documento} consta na lista.")
                    controle_iteracao += 1
            if controle_iteracao == 0:
                print("O aluno não foi encontrado")

            #Solicitando a saída para o usuário    
            controle_pesquisa = input("Deseja sair da pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa) == 1:
                if controle_pesquisa == "n" or controle_pesquisa == "N" or controle_pesquisa == "S" or controle_pesquisa == "s":
                    if controle_pesquisa.upper() == "S":
                        print("Saíndo da pesquisa de alunos...")
                        break

