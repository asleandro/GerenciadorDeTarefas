class Tarefa:
    def __init__(self, titulo, descricao):
        
        # Encapsulamento: Os atributos são protegidos usando um "_" como prefixo
        self._titulo = titulo
        self._descricao = descricao
        self._concluida = False
        
    def concluir(self):
        self._concluida = True
    
    def __str__(self):
        status = "Concluida" if self._concluida else "Pendente"
        return f"{self._titulo} ({self._descricao}) - {status}"
       