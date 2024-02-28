altura = input("Qual sua altura? ")

genero = input("Qual seu genero? m / f. ")

ideal = 0

if genero == 'm':
    ideal = (72.7 * float(altura)) - 58
    
    print("Seu peso ideal é: ", ideal)
else:
    ideal = (62.1 * float(altura)) - 44.7
    print("Seu peso ideal é: ", ideal)
