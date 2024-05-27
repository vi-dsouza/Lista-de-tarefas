#Lista vazia que receberá as tarefas
lista_tarefas = []

#Função de menu
def menu():
    print("\n_____TO DO LIST_____")
    print("\n1- Adicionar tarefa")
    print("2- Listar tarefas")
    print("3- Marcar como concluída")
    print("4- Remover tarefa")
    print("5- Sair") 
    return int(input("\nO que deseja fazer? "))

#Função para adicionar tarefa 
def adiciona_tarefa(lista):
    tarefa = input("\nInforme a tarefa: ")
    lista.append({"tarefa": tarefa, "concluida": False})

#Função para listar todas as tarefas
def lista_tarefa(lista):
    for i, tarefa in enumerate(lista):
        status = "Concluida" if tarefa["concluida"] else "Não concluida"
        print(f"\n{i}- {tarefa['tarefa']} - {status}")
    if not lista:
        print("\nA lista está vazia!")

#Função que marca uma tarefa como concluida
def marcar_concluida(lista):
    numero = int(input("\nInforme o número da tarefa para concluir: "))
    if 0 <= numero < len(lista):
        lista[numero]["concluida"] = True
    else:
        print("\nÍndice inválido!")

#Função que remove uma tarefa da lista
def remove_tarefa(lista):
    numero = int(input("\nInforme o número da tarefa a ser removida: "))
    if 0 <= numero < len(lista):
        lista.pop(numero)
    else:
        print("\nÍndice inválido!")


while True:

    opcao = menu()

    if opcao == 1:
        adiciona_tarefa(lista_tarefas)
    elif opcao == 2:
        lista_tarefa(lista_tarefas)
    elif opcao == 3:
        marcar_concluida(lista_tarefas)
    elif opcao == 4:
        remove_tarefa(lista_tarefas)
    elif opcao == 5:
        print("Você escolheu sair...")
        break
    else:
        print("\nOção inválida!")
