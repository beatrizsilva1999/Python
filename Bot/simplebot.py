import re

print("Olá! Eu sou um bot que ajuda a fazer cálculos simples.")

while True:
    mensagem = input("Digite sua equação ou 'sair' para sair: ")

    if mensagem == "sair":
        break

    # Use expressões regulares para extrair os números e o operador da mensagem
    numeros = re.findall(r'\d+', mensagem)
    operador = re.findall(r'[\+\-\*/]', mensagem)

    # Se nenhum número ou operador for encontrado, exiba uma mensagem de erro
    if not numeros or not operador:
        print("Equação inválida. Tente novamente.")
        continue

    # Converte os números em valores inteiros e executa a operação apropriada
    num1 = int(numeros[0])
    num2 = int(numeros[1])
    resultado = None

    if operador[0] == "+":
        resultado = num1 + num2
    elif operador[0] == "-":
        resultado = num1 - num2
    elif operador[0] == "*":
        resultado = num1 * num2
    elif operador[0] == "/":
        resultado = num1 / num2

    # Exibe o resultado da operação
    print(f"O resultado da equação é: {resultado}")