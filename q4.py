numero = list(input("Digite o número: "))
numero.insert(0, '9')
numero.insert(5, '-')
test = ''
for i in numero:
    test += i
print(test)