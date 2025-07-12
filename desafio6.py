# Solicita a palavra ao usuário
palavra = input("Digite uma palavra: ")

# Inverte a palavra usando slicing
palavra_invertida = palavra[::-1]

# Verifica se é um palíndromo
if palavra == palavra_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")