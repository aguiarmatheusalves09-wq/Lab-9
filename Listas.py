# Questão 1

from random import *
from itertools import batched

valores = []

while True:
    numeros = input("Digite pelo menos 4 numeros, para parar, digite fim: ")

    if numeros.lower() == "fim":
        break

    valores.append(int(numeros))

if len(numeros) > 4:
    print("Tu é burro?")
else:
    print("Lista original:", valores)
    print("Os 3 primeiros elementos:", valores[:3])
    print("Os 2 últimos elementos:", valores[-2:])
    print("Lista invertida:", valores[::-1])
    print("Elementos de índice par:", valores[::2])
    print("Elementos de índice ímpar:", valores[1::2])

# Questão 2

geral = ['www.google.com', 'google', 'www.github.com', 'github', 'www.yutube.com', 'Yutube']
print(f"URLs: {geral[::2]}")
print(f"Dominios: [{geral[1]}, {geral[3]}, {geral[5]}]")

# Questão 3

valores = []
test = 0
media = 0
for i in range(10):
    valores.append(randint(-100, 100))
for i in valores:
    print(i)
    test += i
print(valores)
print(max(valores))
print(min(valores))
print(test)
media += test / 10
print(media)

# Questão 4

q1 = int(input("Digite a quantidade de elementos de Lista 1: "))
elementos = []
for i in range(q1):
    elementos = list(input(f"Digite os {q1} elementos da lista 1: "))

q2 = int(input("Digite a quantidade de elementos de Lista 2: "))
for i in range(q2):
    elementos2 = list(input(f"Digite os {q2} elementos da lista 2: "))

final = []

for i, x in zip(elementos, elementos2):
    final.append(i)
    final.append(x)
print(final)

# Questão 5

lista1 = []
lista2 = []

for i in range(20):
    lista1.append(randint(0, 50))
    lista2.append(randint(0, 50))
interseccao = list(set(lista1) & set(lista2))
print(lista1)
print(lista2)
print(interseccao)

# Questão 6

lista3 = []
for i in range(20):
    lista3.append(randint(0, 100))
divisoes = int(input("Tamanho das Sublistas: "))
sublistas = list(batched(lista3, divisoes))
print(f"Sublitas \n {sublistas}")

# Questão 7

lista = []
n = int(input("Digite o tamanho de n: "))
for i in range(0, n):
    lista.append(n)
print(lista * n)