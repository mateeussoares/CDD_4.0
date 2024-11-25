''''Ler o número de alunos existentes em uma turma e, após isto, ler
as notas destes alunos, calcular e escrever a média aritmética dessas
notas lidas'''

cont = 1
soma = 0
alunos = int(input("Digite a quantidade de alunos:"))
for i in range(alunos):
    notas = int(input(f"Digite a nota do {i+1} aluno:"))
    soma = soma + notas
media = soma/alunos
print(f"A média da turma é: {media}")
