texto = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
p2 = ''
posicoes = [i for i, letra in enumerate(texto) if letra in vogais]
p2 = posicoes
print(f"Indice de vogais: {p2}")
print(f"Total: {len(p2)}")