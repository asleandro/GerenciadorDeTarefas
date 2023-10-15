from tkinter import SEL_FIRST

# Encapsulamento: a lista de tarefas é um atributo protegido

class ListaDeTarefas:
    def __init__(self):
        # Encapsulamento
        self._tarefas = []
        
    def adicionar_tarefa(self, tarefa):
        self._tarefas.append(tarefa)
    
    def listar_tarefas(self):
        if len(self._tarefas) == 0:
            print("\nNão há tarefas na lista")
        else:
            for idx, tarefa in enumerate(self._tarefas, start=1):
                print(f"{idx}. {tarefa}")
        
    def completar_tarefa(self, index):
        if 0 < index <= len(self._tarefas):
            self._tarefas[index - 1].concluir()
        else:
            print("Índice de tarefa inválido.")
        