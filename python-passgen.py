# Importa os módulos necessários
import random  # Módulo para gerar números aleatórios
import string  # Módulo para acessar constantes de strings como letras, dígitos e pontuação

# Função para gerar uma senha aleatória
def generate_password(lenght: int = 10):  # Define o comprimento padrão da senha como 10 caracteres
    # Combina letras (maiúsculas e minúsculas), dígitos e caracteres de pontuação em um único alfabeto
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha escolhendo aleatoriamente caracteres do alfabeto para o comprimento especificado
    password = ''.join(random.choice(alphabet) for i in range(lenght))
    
    return password  # Retorna a senha gerada

# Gera uma senha usando a função definida
password = generate_password()

# Exibe a senha gerada no console
print(f"Gere a senha: {password}")