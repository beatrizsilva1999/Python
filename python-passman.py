# Importa os módulos necessários
import hashlib  # Módulo para funções de hash criptográfico
import getpass  # Módulo para entrada de senha sem exibição no console

# Dicionário para armazenar nomes de usuários e senhas criptografadas
password_manager = {}

def create_account():
    """
    Função para criar uma nova conta de usuário.
    Solicita ao usuário um nome de usuário e uma senha, criptografa a senha e a armazena no dicionário.
    """
    username = input("Escolha seu nome de usuário:")  # Solicita o nome de usuário
    password = getpass.getpass("Escolha a sua senha:")  # Solicita a senha sem exibi-la no console
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Criptografa a senha usando SHA-256
    password_manager[username] = hashed_password  # Armazena o nome de usuário e a senha criptografada
    print("Sua conta foi criada com sucesso!")  # Confirma a criação da conta

def login():
    """
    Função para realizar o login do usuário.
    Solicita o nome de usuário e a senha, criptografa a senha e verifica se corresponde à armazenada.
    """
    username = input("Entre com seu usuário: ")  # Solicita o nome de usuário
    password = getpass.getpass("Entre com sua senha:")  # Solicita a senha sem exibi-la no console
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Criptografa a senha usando SHA-256
    
    # Verifica se o nome de usuário está no dicionário e se a senha criptografada corresponde
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login realizado com sucesso")  # Mensagem de sucesso
    else:
        print("Login/senha inválido")  # Mensagem de erro para login inválido

def main():
    """
    Função principal que exibe um menu para o usuário criar uma conta, fazer login ou sair.
    """
    while True:
        choice = input("Digite 1 para criar uma conta, 2 para login ou 0 para sair:")  # Exibe o menu de opções
        if choice == "1":
            create_account()  # Chama a função para criar uma conta
        elif choice == "2":
            login()  # Chama a função para realizar o login
        elif choice == "0":
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida")  # Mensagem de erro para opção inválida

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
