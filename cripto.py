from cryptography.fernet import Fernet

# Chave de criptografia (essa chave deve ficar em segurança)
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Simulando um cadastro de funcionários
funcionarios = {
    "Vitoria": {
        "senha": "python",
        "nivel_acesso": "Senior"
    },
    "Matheus": {
        "senha": "pythonpl",
        "nivel_acesso": "Pleno"
    },
    
    "Felipe": {
        "senha": "pythonjr",
        "nivel_acesso": "Junior"
    },

     "Jair": {
        "senha": "pythonjr1",
        "nivel_acesso": "Junior"
    },

     "Kauan": {
        "senha": "pythonjr2",
        "nivel_acesso": "Junior"
    }
}

def criptografar_dados(dados):
    return cipher_suite.encrypt(dados.encode())

def descriptografar_dados(dados):
    return cipher_suite.decrypt(dados).decode()

def verificar_autorizacao(funcionario, senha):
    if funcionario in funcionarios:
        if funcionarios[funcionario]["senha"] == senha:
            return funcionarios[funcionario]["nivel_acesso"]
    return None

# Simulação de um funcionário tentando acessar a área
while True:
    funcionario = input("Nome do funcionário: ")
    senha = input("Senha: ")

    nivel_acesso = verificar_autorizacao(funcionario, senha)

    if nivel_acesso:
        if nivel_acesso == "Senior":
            print("Acesso autorizado. Você pode entrar na área contaminada com trajes especiais.")
        elif nivel_acesso == "Junior":
            print("Acesso autorizado. Você pode entrar na área contaminada, mas com medidas de segurança e acompanhamento.")
        elif nivel_acesso == "Pleno":
            print("Acesso autorizado. Você pode entrar na área contaminada, mas com medidas de segurança, porém sem necessidade de acompanhamento.")
        
        break
    else:
        print("Acesso negado. Credenciais inválidas. Tente novamente.")
