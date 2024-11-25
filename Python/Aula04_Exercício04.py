'''Ler uma variável de número inteiro e mostrar a
tabuada de multiplicação desse número (1-10).
Formato de saída: 1 X 5 = 5 | 2 X 5 = 10'''

valor = int(input("Digite um valor:"))
for i in range(valor):
    mult = i * valor
    print(f"{i}x{valor}={mult}")