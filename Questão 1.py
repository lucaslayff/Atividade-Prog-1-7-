# Questão 1:
#numero = input("Digite um número de até 4 dígitos: ")
#soma = sum(int(digito) for digito in numero)
#print("A soma dos algarismos é:", soma)


numero = int(input("Digite um número de até 4 dígitos: "))
soma = 0
if 0 <= numero <= 9999:
   
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10

    soma = milhar + centena + dezena + unidade
    print("A soma dos algarismos é:", soma)
else:
    print("Por favor, digite um número entre 0 e 9999.")



