#Receba 2 números do usuário e mostre eles em ordem crescente.
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

if num1 > num2:
    print(f"Os números na ordem crescente: {num2}, {num1}")
else:
    print(f"Os números na ordem crescente: {num1}, {num2}")
