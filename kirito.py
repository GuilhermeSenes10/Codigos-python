# -*- coding: utf-8 -*-
"""Kirito.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NXYCtI-_pT8V2HkyanTr4YSOItt0AppX
"""

class Sao:
  #construtor
  def __init__(self,vida:float,fome:float,stamina:float,classe:str,nivel:int):
    self.vida = vida
    self.fome = fome
    self.stamina = stamina
    self.classe = classe
    self.nivel = nivel

  #métodos
  def upar(self):
    self.vida = self.vida + 5.0
    self.nivel = self.nivel + 1
    self.stamina = self.stamina + 5.0
    print(f'Você acaba de upar')

  def treinar(self):
    self.stamina = self.stamina - 5.0
    self.fome = self.fome + 3.0
    print(f'foi um ótimo treino')

  def guerreiro(self):
    self.classe = self.classe = 'guerreiro'
    print(f'Parabéns, você é da classe guerreiro')

  def arqueiro(self):
    self.classe = self.classe = 'arqueiro'
    print(f'Parabéns, você é da classe arqueiro')

  def assassino(self):
    self.classe = self.classe = 'assassino'
    print(f'Parabéns, você é da classe assassino')

  def paladino(self):
    self.classe = self.classe = 'paladino'
    print(f'Parabéns, você é da classe paladino')

  def lutar(self):
    self.vida = self.vida - 4.0
    self.stamina = self.stamina - 5.0
    self.fome = self.fome + 3.0
    print(f'Vamos para a luta')

  def dormir(self):
    self.vida = self.vida + 5.0
    self.stamina = self.stamina + 5.0
    self.fome = self.fome - 2.0
    print(f'Que sonin, vou mimir')

  def comer(self):
    self.vida = self.vida + 2.0
    self.fome = self.fome - 3.0
    print(f'Que fominha, vamos memer')

  def status(self):
    if self.vida<1:
      print(f'você morreu')
    print(f'Vida: {self.vida}')
    print(f'Fome: {self.fome}')
    print(f'Stamina: {self.stamina}')
    print(f'Classe: {self.classe}')
    print(f'Nível: {self.nivel}')
    print(f'----------------------')

 

  #instância
Kirito = Sao(vida=10.0,fome=0.0,stamina=10.0,classe='Nenhuma',nivel=0)
Kirito.status()
Kirito.treinar()
Kirito.status()
Kirito.upar()
Kirito.status()
Kirito.lutar()
Kirito.status()
Kirito.dormir()
Kirito.status()
Kirito.comer()
Kirito.status()
Kirito.guerreiro()
Kirito.status()
Kirito.arqueiro()
Kirito.status()
Kirito.assassino()
Kirito.status()
Kirito.paladino()
Kirito.status()