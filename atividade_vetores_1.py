import os

os.system("cls")

#Criando um vetor
vetor_notas = []
QUANTIDADE_NOTAS = 2

print("Adicionando {QUANTIDADE_NOTAS} notas.")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota: "))
   # Adiciona nota no vetor
    vetor_notas.append(nota)

# sum(vetor) = soma todos os valores no vetor.
media = sum(vetor_notas / QUANTIDADE_NOTAS)

print("\nExibindo as notas informadas.")
# ForEach = percorre o vetor sem informar a quantidade.
# enumerate = através da variável i, numera a quantidade de repetições.
for uma_nota in enumerate(vetor_notas, start=1):
    print(f"{i}ª nota: {uma_nota}")

print(f"Media: {media}")