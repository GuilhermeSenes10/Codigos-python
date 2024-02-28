print("Menu\n")
print("Bem vindo ao programa de consulta de multas!\n")


print("1) Dirigir sem atenção ou sem os cuidados indispensáveis à segurança;")
print("2) Estacionar nos acostamentos.")
print("3) Parar sobre faixa destinada a pedestres.")
print("4) Usar buzina em locais e horários proibidos sinalização.")
print("5) Deixar de atualizar o cadastro de registro do veículo.")

print("\nPara mostrar mais itens digite '+' para ir para o proximo menu digite '1'")
navmenu = input("Digite aqui: \n") #entrada de dados para interagir com o menu 

if (navmenu == '+'): #condição para mostrar a proxima parte do menu caso a variavel navmenu receba +
  print("6) Usar o veículo para arremessar sobre os pedestres água ou detritos.")
  print("7) Ter seu veículo imobilizado na via por falta de combustível.")
  print("8) Estacionar nas esquinas e a menos de 5m do alinhamento da via transversal.")
  print("9) estacionar em local/horário proibido especificamente pela sinalização;")
  print("10) parar sobre faixa de pedestres na mudança de sinal luminoso;")

  print("\nPara mostrar mais itens digite '+' para ir para o proximo menu digite '1'")
  navmenu = input("Digite aqui: ") #entrada de dados para interagir com o menu 

if (navmenu == '+'): #condição para mostrar a proxima parte do menu caso a variavel navmenu receba +
  print("11) parar na contramão de direção.")
  print("12) o condutor deixar de usar o cinto segurança;")
  print("13) estacionar sobre faixa destinada a pedestre;")
  print("14) conduzir veículo sem ter sido submetido à inspeção veicular, quando obrigatória;")
  print("15) conduzir o veículo sem equipamento obrigatório;")

  print("\nPara mostrar mais itens digite '+' para ir para o proximo menu digite '1'")
  navmenu = input("Digite aqui: ") #entrada de dados que indica se mostrara mais uma parte da lista ou ira para a proxima parte do programa

if (navmenu == '+'): #condição para mostrar a proxima parte do menu caso a variavel navmenu receba +
  print("16) conduzir pessoas nas partes externas do veículo.")
  print("17) dirigir veículo sem ter CNH/PPD/ACC;")
  print("18) dirigir veículo com validade de CNH/PPD vencida há mais de 30 dias (CNH provisória é permitida);")
  print("19) transportar criança sem observância das normas de segurança estabelecidas pelo CTB; ")
  print("20) transitar com o veículo em calçadas, passeios; ")

  print("\nPara mostrar mais itens digite '+' para ir para o proximo menu digite '1'")
  navmenu = input("Digite aqui: ") #entrada de dados para interagir com o menu 

if (navmenu == '+'): #condição para mostrar a proxima parte do menu caso a variavel navmenu receba +
  print("21) ultrapassar pelo acostamento. ")
  print("22) dirigir sob a influência de álcool; ")
  print("23) dirigir sob influência de qualquer outra substância que determine dependência; ")
  print("24) disputar corrida; ")
  print("25) dirigir ameaçando os pedestres que estejam atravessando a via pública. ")

valormulta = 0.0 #variavel responsavel por armazenar o valor da multa 
pontcarteira = 0.0 #variavel responsavel por armazenar o numero de pontos 
grave = 'Infrações autossuspensivas' #variavel responsavel por armazenar uma string de quando a multa for grava e não tem pontos 

navmenu = input("Digite 1 para entrar no menu que fara o calculo das multas para voê\nDigite aqui: ") #entrada de dados para interagir com o menu 
i = 0
if navmenu == '1':  
  print("\n\nDigite o numero da multa.\n Ou d1igite '0' para sair")
  #Este while tem como parametro a variavel i comparada com o numero 5, cada vez que o while é executado o i ganha mais 1, então a condição sera verdadeira ate quando o i valer 5 apos isso sera falsso então não 
  #ira executa o while 
  while i<5:
    i = i +1 #Adiciona mais 1 na variavel i
    codmulta = int(input("\nDigite aqui: "))
    #condições que armazenam o valor e os pontos de cada multa 
    
    if codmulta == 0: #Condição que sera executada para finalizar o programa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta ) #Mostra os resultados finais qçuando o programa for finalizado usando o comando 0
      i = i+10 #Adiciona 10 na variavel i, assim fazendo com que ele não entre mais no while pois ele é maior que 5

    if codmulta == 1:
      valormulta = valormulta + 88.38 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 3 #soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 2:
      valormulta = valormulta + 88.38 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 3 #soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 3:
      valormulta = valormulta + 88.38 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 3 #soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 4:
      valormulta = valormulta + 88.38 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 3 #soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 5:  
      valormulta = valormulta + 88.38 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 3 #soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 6:
      valormulta = valormulta + 130.16 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 4 #soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 7:
      valormulta = valormulta + 130.16 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 4 #soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 8:
      valormulta = valormulta + 130.16#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 4#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 9:
      valormulta = valormulta + 130.16#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 4#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 10:  
      valormulta = valormulta + 130.16#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 4#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 11:
      valormulta = valormulta + 130.16#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 4#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 12:
      valormulta = valormulta + 195.23#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 5#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 13:
      valormulta = valormulta + 195.23#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 5#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 14:
      valormulta = valormulta + 195.23#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 5#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 15:  
      valormulta = valormulta + 195.23#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 5#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 16:
      valormulta = valormulta + 195.23#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 5#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 17:
      valormulta = valormulta + 880.41#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 7#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 18:
      valormulta = valormulta + 880.41#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 7#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 19:
      valormulta = valormulta + 880.41#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 7#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )

    if codmulta == 20:  
      valormulta = valormulta + 880.41#soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 7#soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta )#print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 21:
      valormulta = valormulta + 880.41 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa 
      pontcarteira = pontcarteira + 7 #soma o valor dos pontos de cada multa com os que ja estavam na variavel, de acordo com o numero da multa 
      print("pontos na carteira: ",pontcarteira, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 22:
      valormulta = valormulta + 2934.70 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa      
      print("pontos na carteira: -- " 'Multa muito grave: ',grave, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input  

    if codmulta == 23:
      valormulta = valormulta + 2934.70 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa      
      print("pontos na carteira: -- " 'Multa muito grave: ',grave, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input 

    if codmulta == 24:
      valormulta = valormulta + 2934.70 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa      
      print("pontos na carteira: -- " 'Multa muito grave: ',grave, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input  

    if codmulta == 25:  
      valormulta = valormulta + 2934.70 #soma o valor da multa que ja estava armazenado na variavel com o valor, de acordo com o numero da multa      
      print("pontos na carteira: -- " 'Multa muito grave: ',grave, "\nValor a pagar: ",valormulta ) #print que mostra os resultados dos do valor e dos pontos depois de cada input 

print("O programa finalizou!!!!")#Acabou  
