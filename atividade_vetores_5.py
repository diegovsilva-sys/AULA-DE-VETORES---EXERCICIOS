import os
import time
os.system("cls")

while True:
    # Limpar o terminal.
    os.system("cls")
    for i in range(1):

      os.system("cls")

    #Criando um vetor
    vetor_pratos = []
    QUANTIDADE_pratos = 0
    preco_total = 0
    pratos_solicitados = 0

    print("\nExibindo os pedidos informados.")
    print("""
          === MENU ===
          1   Picanha          R$ 25,00
          2   Lasanha          R$ 20,00
          3   Strogonoff       R$ 18,00
          4   Bife acebolado   R$ 15,00
          5   Pão com ovo      R$ 15,00
           """)
    for i in range(2):
     opcao = float(input(f"Qual seu pedido {i+1}ª : "))
    mais_pedidos = input("Deseja fazer um novo pedido? \nUse S ou N: ").lower()
    
    match opcao:
        case 1:
             prato = "Picanha" 
             preco = 25
        case 2:
             prato = "Lasanha"
             preco = 20
        case 3:
             prato = "Strogonoff"
             preco = 18
        case 4:
             prato = "Bife acebolado"
             preco = 15
        case 5:
             prato = "Pão com ovo"
             preco = 15
        case _:
             prato = ""   
             preco = 0

    if mais_pedidos == "s/n":
             preco_total += preco
             pratos_solicitados += ", " + prato if pratos_solicitados else prato
             break
print("\n=== Nota Fiscal ===")
print(f"Pratos solicitados: {pratos_solicitados}")
print(f"Mais pedidos: {mais_pedidos}")
print(f"Total da compra: R$ {preco_total}")