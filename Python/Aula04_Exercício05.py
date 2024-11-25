'''Receber um número do usuário e mostrar todos os números
ímpares do intervalo de 1 até o número digitado'''

num = int(input("Digite um valor:"))
for x in range(1, num, 2):
    print(x)