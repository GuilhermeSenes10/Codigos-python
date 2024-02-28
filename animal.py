#classes sempre iniciam com letra maiúscula
class Animal:

#construtor
    def __init__(self,nome="",idade="",tipo=""):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
#Getters (pegar)
    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getTipo(self):
        return self.__tipo
        
#Setter (alterar)
    def setNome(self,nome):
        self.__nome = nome
    def setIdade(self,idade):
        self.__idade = idade
    def setTipo(self,tipo):
        self.__tipo = tipo

#Meus métodos
    def __str__(self):
        return "{0} é um {1} de {2} anos".format(self.nome,self.tipo,self.idade)
        
class Burro(Animal):
    def __init__(self,nome="",idade=""):
        self.nome = nome
        self.idade = idade
        self.tipo = "Burro"
    def setTipo(self,tipo):
        print("Desculpe, {0} nunca será um(a) {1}".format(self.nome,self.tipo))
    def fazerBarulho(self):
        print("{0} fala já chegamos?".format(self.nome))
