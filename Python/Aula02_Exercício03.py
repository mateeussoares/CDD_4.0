#Ler o nome de dois times e o número de gols marcados na partida.
# Caso não haja vencedor será mostrado empate na tela.

time1 = input("Digite o nome do primeiro time:\n")
time2 = input("Digite o nome do segundo time:\n")
gtime1 = int(input(f"Quantos gols o time {time1} fez?"))
gtime2 = int(input(f"Quantos gols o time {time2} fez?"))

if gtime1 ==  gtime2:
    print(f"Empate com {gtime1} gols cada!")
elif gtime1 > gtime2:
    print(f"Vitória de {time1}!")
else:
    print(f"Vitória de {gtime2}!")