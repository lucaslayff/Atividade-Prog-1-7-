saque = float(input('Digite o valor de saque: '))
if saque <= 0:
    print('Informe somente o valor disponível para saque! ')
else:
    nota100  = saque // 100
    saque = saque %  100

    nota50  = saque //  50
    saque = saque %  50

    nota20  = saque // 20
    saque = saque %  20

    nota10  = saque // 10
    saque = saque %  10
    
    nota5  = saque // 5
    saque = saque %  5

    nota2  = saque // 2
    saque = saque %  2

#MOEDAS

    moeda1 = saque // 1
    saque  = saque % 1

    moeda0_50 = saque // 0.50
    saque  = round(saque % 0.50, 2)

    moeda0_25 = saque // 0.25
    saque  = round(saque % 0.25, 2)

    moeda0_10 = saque // 0.10
    saque  = round(saque % 0.10, 2)

    moeda0_05 = saque // 0.05
    saque  = round(saque % 0.10, 2)

    moeda0_01 = round(saque / 0.01) 

print('Notas de R$100,00: ', int(nota100))
print('Notas de R$50,00: ', int(nota50))
print('Notas de R$20,00: ', int(nota20))
print('Notas de R$10,00: ', int(nota10))
print('Notas de R$5,00: ', int(nota5))
print('Notas de R$2,00: ', int(nota2))
print('Moedas de R$1,00: ', int(moeda1))
print('Moedas de R$0,50: ', int(moeda0_50))
print('Moedas de R$0,25: ', int(moeda0_25))
print('Moedas de R$0,10: ', int(moeda0_10))
print('Moedas de R$0,05: ', int(moeda0_05))
print('Moedas de R$0,01: ', int(moeda0_01))
    


