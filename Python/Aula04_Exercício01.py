#Receba do usário um número de um a 12 e mostre na tela o mês correspondente.
#Caso o mês não exista, mostrar na tela "Valor inválido". Obs: use If/Else/Elif.

num = int(input("Digite um número de 1 a 12:"))
if num == 1:
    print("Janeiro.")
elif num == 2:
    print("Fevereiro.")
elif num == 3:
    print("Março.")
elif num == 4:
    print("Abril")
elif num == 5:
    print("Maio.")
elif num == 6:
    print("Junho.")
elif num == 7:
    print("Julho.")
elif num == 8:
    print("Agosto.")
elif num == 9:
    print("Setembro.")
elif num == 10:
    print("Outubro.")
elif num == 11:
    print("Novembro.")
elif num == 12:
    print("Dezembro.")
else:
    print("Valor Inválido.")