import os

os.system("cls")

#Criando um vetor
vetor_notas = []

# Adicionando 3 notas .
for i in range(3):
    nota = float(input("Digite uma nota: "))
    vetor_notas.append(nota)

# Exibindo as notas informadas.
for i in range(3):
    print(f"Nota: {vetor_notas[i]}")