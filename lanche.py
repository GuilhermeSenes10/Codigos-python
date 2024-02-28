print("CARDAPIO")
print("100 Cachorro quente: R$12,99")
print("101 Bauru simples: R$7,99")
print("102 Bauru com ovo: R$8,99")
print("103 Hamburguer: R$10,90")
print("104 Cheeseburger: R$12,99")
print("105 Refrigerante: R$5,00")

codigo = int(input("DIGITE O CODIGO SO SEU PEDIDO: "))

if codigo == 100:
    print("O cachorro quente esta pronto!!!! Valor a ser pago: R$12,99")
else:    
    if codigo == 101:
        print("Essa comida estranha ta pronta!! Valor a ser pago: R$7,99")
    else: 
        if codigo == 102:
            print("Comida estranha elaborada esta pronta!!! Valor a ser pago: R$8,99")
        else:
            if codigo == 103:  
                print("Hamburguer está pronto!!! Valor a ser pago: R$10,90")
            else:   
                if codigo == 104:
                    print("Cheeseburger esta pronto!!! Valor a ser pago: R$12,99")
                else:    
                    if codigo == 105:
                        print("Coquinha gelada ta na mão!!! Valor a ser pago: R$5,00")
    
