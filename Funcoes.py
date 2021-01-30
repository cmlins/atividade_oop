from Professor import Professor
from Aluno import Aluno
from Curso import Curso

class Funcoes:

    def mostrar_opcoes(lista_opcoes, nome_login):
        print(f"Olá! Seja bem-vinde {nome_login}! Escolha uma opção:")
        for opcao in lista_opcoes:
            print(opcao)

# métodos para mostrar os elementos da lista

    def mostrar_alunos(lista_alunos):
        for aluno in lista_alunos:
            print(f"{aluno.nome} - {aluno.matricula}")

    def mostrar_professores(lista_professores):
        for professor in lista_professores:
            print(f"{professor.disciplina}")

    def mostrar_cursos(lista_cursos):
        for curso in lista_cursos:
            print(f"{curso.nome} - {curso.periodo}")

# métodos para incluir os elementos na lista

    def incluir_tipo(opcao, lista):
        while True:
            Funcoes.inserir_tipo(opcao, lista)
            
            #Solicitando a saída para o usuário    
            controle_insert = input("Deseja fazer mais uma inclusão? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "S" or controle_insert == "s":
                    if controle_insert.upper() == "N":
                        print("Saíndo da inclusão...")
                        break


# métodos para excluir os elementos na lista

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

    def excluir_curso(lista_cursos):
        while True:
            iterador_cursos = 0 
            max_cursos = len(lista_cursos)
            while iterador_cursos < max_cursos: #Outra forma de fazer loop em lista
                print(f"Índice - {iterador_cursos} - {lista_cursos[iterador_cursos].nome}")
                iterador_cursos += 1
            input_do_usuario = input("Digite um valor para a exclusão do curso \n")
            
            if input_do_usuario.isnumeric():
                curso_selecionado = int(input_do_usuario) #Solicite para o usuário o índice
                if curso_selecionado in range(0, max_cursos):
                    curso_excluido = lista_cursos.pop(curso_selecionado) #pop para excluir o curso e retornar o objeto excluído
                    print(f"O curso {curso_excluido.nome} foi excluído") #mostra para o usuário
                    #Solicitando a saída para o usuário    
                    controle_exclusao = input("Deseja sair da exclusão? (Digite 's' ou 'S' para sair) \n")
                    if len(controle_exclusao) == 1:
                        if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
                            if controle_exclusao.upper() == "S":
                                print("Saíndo da exclusão de cursos...")
                                break
                else:
                    print("Esse valor não existe")
            else:
                print("Esse valor deve ser um número")

    
    def excluir_professor(lista_professores):
        while True:
            iterador_professores = 0 
            max_professores = len(lista_professores)
            while iterador_professores < max_professores: #Outra forma de fazer loop em lista
                print(f"Índice - {iterador_professores} - {lista_professores[iterador_professores].disciplina}")
                iterador_professores += 1
            input_do_usuario = input("Digite um valor para a exclusão do professor \n")
            
            if input_do_usuario.isnumeric():
                professor_selecionado = int(input_do_usuario) #Solicite para o usuário o índice
                if professor_selecionado in range(0, max_professores):
                    professor_excluido = lista_professores.pop(professor_selecionado) #pop para excluir o professor e retornar o objeto excluído
                    print(f"O professor {professor_excluido.disciplina} foi excluído") #mostra para o usuário
                    #Solicitando a saída para o usuário    
                    controle_exclusao = input("Deseja sair da exclusão? (Digite 's' ou 'S' para sair) \n")
                    if len(controle_exclusao) == 1:
                        if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
                            if controle_exclusao.upper() == "S":
                                print("Saíndo da exclusão de professores...")
                                break
                else:
                    print("Esse valor não existe")
            else:
                print("Esse valor deve ser um número")


# métodos para detalhar os elementos na lista

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

    def detalhar_professor(lista_professores):
        while True:
            nome_professor_pesquisado = input("Digite o nome do professor a ser pesquisado \n")
            controle_iteracao = 0
            for professor in lista_professores:
                if nome_professor_pesquisado.upper() in professor.nome.upper():
                    print(f"O professor {professor.nome} com a {professor.matricula} e o documento {professor.documento} consta na lista.")
                    controle_iteracao += 1
            if controle_iteracao == 0:
                print("O professor não foi encontrado")

            #Solicitando a saída para o usuário    
            controle_pesquisa = input("Deseja sair da pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa) == 1:
                if controle_pesquisa == "n" or controle_pesquisa == "N" or controle_pesquisa == "S" or controle_pesquisa == "s":
                    if controle_pesquisa.upper() == "S":
                        print("Saíndo da pesquisa de professores...")
                        break

    def detalhar_curso(lista_cursos):
        while True:
            nome_curso_pesquisado = input("Digite o nome do curso a ser pesquisado: \n")
            controle_iteracao = 0
            for curso in lista_cursos:
                if nome_curso_pesquisado.upper() in curso.nome.upper():
                    print(f"O curso {curso.nome} do {curso.periodo}º período consta na lista.")
                    controle_iteracao += 1
            if controle_iteracao == 0:
                print("O curso não foi encontrado")

            #Solicitando a saída para o usuário    
            controle_pesquisa = input("Deseja sair da pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa) == 1:
                if controle_pesquisa == "n" or controle_pesquisa == "N" or controle_pesquisa == "S" or controle_pesquisa == "s":
                    if controle_pesquisa.upper() == "S":
                        print("Saíndo da pesquisa de cursos...")
                        break


# método para escolher o elemento que vai ser inserido lista

    def inserir_tipo(opcao, lista):
        if (opcao == 2):
            nome_aluno = input("Digite o nome do Aluno\n")
            matricula_aluno = input("Digite a matrícula do Aluno\n")
            documento_aluno = input("Digite o número do documento\n")
            aluno = Aluno(nome=nome_aluno,documento=documento_aluno,matricula=matricula_aluno) #Incluindo o documento no momento do construtor
            lista.append(aluno) #Insere um aluno na lista
            print(f"O aluno {aluno.nome} foi inserido!")  #Mostra para o usuário que o append foi feito
        elif (opcao == 6):
            disciplina_professor = input('Digite a disciplina dada pelo professor: \n')
            professor = Professor(disciplina_professor)
            lista.append(professor)
            print(f"A disciplina {professor.disciplina} foi inserida!")
        elif (opcao == 10):
            nome_curso = input('Insira o nome do curso: \n')
            periodo_curso = input('Insira o período do curso: \n')
            curso = Curso(nome_curso, periodo_curso)
            lista.append(curso)
            print(f"O curso {curso.nome} do período {curso.periodo} foi inserido!")