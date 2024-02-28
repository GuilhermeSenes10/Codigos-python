nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3


if media > 10:
    print('Alguma nota declarada é maior que 10!!!!!!!!')
else:
    if media >= 7 and media < 10:
        print('Sua media foi:', media, 'Você foi aprovado!!!!!!')
    else:
        if media == 10:
            print('Sua media foi:', media, 'Você foi aprovado com distinção!!!!!!')
        else:
            if media < 7:
                print('Sua media foi:', media, 'Você foi Reprovado!!!!!!')
