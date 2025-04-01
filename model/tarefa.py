from model.database import Database
 
class Tarefa:
    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao
 
    def salvarTarefa(self):
        """Salva uma nova tarefa no banco de dados"""
        db = Database()
        db.conectar()
 
        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES(%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()
 
    @staticmethod
    def listarTarefas():
        """Retornar uma lista com todas as tarefas cadastradas."""
        db = Database()
        db.conectar()
 
        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []
 
    @staticmethod
    def apagarTarefa(idTarefa):
        """Apaga uma tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()
 
        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (idTarefa,)
        db.executar(sql, params)
        db.desconectar()
 
    @staticmethod
    def editarTarefa(idTarefa, titulo, data_conclusao):
        """Edita uma tarefa cadastrada no banco de dados."""
       
        db = Database()
        db.conectar()
 
        sql = 'UPDATE tarefa SET titulo = %s, data_conclusao = %s WHERE id = %s'
        params = (titulo, data_conclusao, idTarefa)
 
        db.executar(sql, params)
        db.desconectar()
 
@staticmethod
def buscarPorId(idTarefa):
    """Busca uma tarefa pelo ID"""
    db = Database()
    db.conectar()

    sql = "SELECT id, titulo, data_conclusao FROM tarefa WHERE id = %s"
    resultado = db.consultar(sql, (idTarefa,))

    db.desconectar()

    if resultado and len(resultado) > 0:
        return {
            'id': resultado[0][0],
            'titulo': resultado[0][1],
            'data_conclusao': resultado[0][2]
        }
    else:
        return None