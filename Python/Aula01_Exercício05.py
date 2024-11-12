"""Duas variáveis (A e B) possuem valores distintos (A=5 e B= 10), Crie um algoritmo que armazene esses
dois valores nessas duas variáveis, e efetue a troca dos valores de forma que a variável A passe a possuir
o valor da variável B e que a variável B passe a possuir o valor da variável A. Por fim,
apresentar os valores trocados."""

A = 5
B = 10
print(f"Atuais variáveis: {A} e {B}")
X = A
A = B
B = X

print(f"A:{A} | B:{B}")
