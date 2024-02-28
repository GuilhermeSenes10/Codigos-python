from Animal import *
class Burro(Animal):
    def __init__(self,nome="",idade=""):
        self.nome = nome
        self.idade = idade
        self.tipo = "Burro"                                                                 
    def setTipo(self,tipo):
        print("Desculpe, {0} nunca será um(a) {1}".format(self.nome,self.tipo))
    def fazerBarulho(self):
        print("{0} fala já chegamos?".format(self.nome))
