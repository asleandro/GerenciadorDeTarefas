from Tarefa import Tarefa

# Encapsulamento: Os atributos são protegidos usando um "_" como prefixo
# Herança - TarefaImportante herda atributos e métodos da classe Tarefa

class TarefaImportante(Tarefa):
    
    def __init__(self, titulo, descricao, prioridade):
        super().__init__(titulo, descricao)
        self._prioridade = prioridade
        
    # Polimorfismo - Comportamento de TarefaImportante tem uma funcionalidade estendida
    def __str__(self):
        status = "Concluida" if self._concluida else "Pendente"
        return f"{self._titulo} ({self._descricao}) - Prioridade: {self._prioridade} - {status}"