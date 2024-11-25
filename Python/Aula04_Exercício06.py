'''Receber 10 números do usuário e mostre a
soma de todos os números ímpares.'''

soma = 0
for x in range(10):
    num = int(input("Digite o valor para a soma:"))
    if num % 2 != 0:
        soma = soma + num
    else:
        print("O valor inserido é par.")
print(f"A soma de todos os valores é {soma}.")