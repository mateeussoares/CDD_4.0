"""Escreva um algoritmo para ler 10 números e ao final
da leitura escrever a soma total dos 10 números lidos."""

soma = 0
for x in range(10):
    num = int(input("Digite o valor para a soma:"))
    soma = soma + num

print(f"A soma de todos os valores digitados é: {soma}")