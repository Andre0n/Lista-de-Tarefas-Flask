class Tarefa():

    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def get_titulo(self):
        return str(self.titulo)


    def get_descricao(self):
        return str(self.descricao)


    def set_titulo(self, novo_titulo):
        self.titulo = novo_titulo


    def set_descricao(self, nova_descricao):
        self.descricao = nova_descricao