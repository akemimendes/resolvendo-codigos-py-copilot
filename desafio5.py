# Solicita as três notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média aritmética
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado
print("A média das notas é:", round(media, 1))