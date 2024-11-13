#Faça um código que receba as 3 notas de um aluno e verifique se ele está aprovado ou reprovado.
#Considere que a média para aprovação é 7,0

nota1 = float(input("Digite primeira nota:"))
nota2 = float(input("Digite segunda nota:"))
nota3 = float(input("Digite terceira nota:"))
media = (nota1 + nota2 + nota3)/3
print(f"A média do aluno é: {media}")
if media >= 7:
    print("Aluno aprovado!")
else:
    if media > 4:
        print("Aluno em recuperação.")
    else:
        print("Aluno reprovado.")