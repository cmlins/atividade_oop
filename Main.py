#imports das classes de negócio
from Curso import Curso
from Aluno import Aluno
from Professor import Professor
from Funcoes import Funcoes
import sys

#inicialização de variáveis e objetos
lista_opcoes = [   "0-) Sair \n"
                  ,"1-) Ver lista de alunos"
                  ,"2-) Incluir um novo aluno"
                  ,"3-) Excluir um aluno existente"
                  ,"4-) Ver um aluno"
                  ,"5-) Ver lista de professor"
                  ,"6-) Incluir um novo professor"
                  ,"7-) Excluir um professor existente"
                  ,"8-) Ver um professor"
                  ,"9-) Ver lista de cursos"
                  ,"10-) Incluir um novo curso"
                  ,"11-) Excluir um curso existente"
                  ,"12-) Ver um curso"]

lista_professores = []
lista_alunos = []
lista_cursos = []

#Iteração com o usuário e dar as boas vindas
nome_login = input("Olá! Por favor entre com o nome de usuário: \n")

#Loop para manter na memória
while True:
    #Mostrar as boas vindas e as opções
    Funcoes.mostrar_opcoes(lista_opcoes, nome_login)

    opcao_selecionada = int(input("Escolha uma opção \n"))

    #condicionais para controlar a navegação do programa
    if opcao_selecionada == 0: #Sai do programa
        print("Você saiu do sistema.")
        sys.exit()

    elif opcao_selecionada == 1: #Ver lista de alunos
        Funcoes.mostrar_pessoas(lista_alunos)

    elif opcao_selecionada == 2: #Incluir um novo aluno
        Funcoes.incluir_aluno(lista_alunos)        
        
    elif opcao_selecionada == 3: #Excluir um aluno existente
        Funcoes.excluir_aluno(lista_alunos)
                    
    elif opcao_selecionada == 4: #Ver um aluno
        Funcoes.detalhar_aluno(lista_alunos)        
            
    elif opcao_selecionada == 5: #Ver lista de professor
        pass
    elif opcao_selecionada == 6: #Incluir um novo professor
        pass
    elif opcao_selecionada == 7: #Excluir um professor existente
        pass
    elif opcao_selecionada == 8: #Ver um professor
        pass
    elif opcao_selecionada == 9: #Ver lista de cursos
        pass
    elif opcao_selecionada == 10: #Incluir um novo curso
        pass
    elif opcao_selecionada == 11: #Excluir um curso existente
        pass
    elif opcao_selecionada == 12: #Ver um curso
        pass











