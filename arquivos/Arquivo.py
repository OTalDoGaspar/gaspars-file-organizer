class Arquivo:
    nome = ""
    extensao = ""

    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome    
    def setNome(self, nome):
        self.nome = nome

    def getExtensao(self):
        listaExtensao = self.nome.split(".")
        self.extensao =  listaExtensao[-1]
        return self.extensao
