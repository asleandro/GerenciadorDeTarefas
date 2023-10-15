from queue import Empty
from ListaDeTarefas import ListaDeTarefas
from Tarefa import Tarefa
from TarefaImportante import TarefaImportante
            
if __name__ == "__main__":
    listaDeTarefas = ListaDeTarefas()
    
    while True:
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")
    
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da Tarefa: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (Baixa / Média / Alta): ")
            tarefa = TarefaImportante(titulo, descricao, prioridade)
            listaDeTarefas.adicionar_tarefa(tarefa)
        elif opcao == "2":
            listaDeTarefas.listar_tarefas()
        elif opcao == "3":
            listaDeTarefas.listar_tarefas()
            index_tarefa = int(input("Informe o número da tarefa concluída: "))
            listaDeTarefas.completar_tarefa(index_tarefa)
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
