'''Escreva um algoritmo que leia o número de litros vendidos e tipo decombustível (codificado da
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$
5,80 e o preço do litro do etanol é R$ 4,90.'''

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível. \n'G' para Gasolina e 'E' para Etanol: ")

if tipo == "G" or tipo == "g":
    valor = litros*5.80
    print(f"O valor será de {valor}")
elif tipo == "E" or tipo == "e":
    valor = litros*4.90
    print(f"O valor será de {valor}")
else:
    print("Os dados informados não estão corretos.\n"
          "Selecione o tipo de combustível correto.")