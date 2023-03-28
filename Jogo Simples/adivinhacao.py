import random

print("Bem-vindo ao jogo de adivinhação!")
numero_secreto = random.randint(1, 100)

while True:
    tentativa = int(input("Digite um número entre 1 e 100: "))
    if tentativa == numero_secreto:
        print("Parabéns, você acertou!")
        
    elif tentativa > numero_secreto:
        print("O número é menor, tente novamente.")
    else:
        print("O número é maior, tente novamente.")
        
       