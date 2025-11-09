from bd_vitoriasfestas import banco

def cadastro(banco):
    id_cliente = banco[-1]["ID"] +1
    nome_cliente = input("Digite seu nome: ")
    telefone_cliente = input("Digite seu telefone: ")
    email_cliente = input("Digite seu E-mail: ")

    novo_cliente = {
        "ID" : id_cliente,
        "Nome" : nome_cliente,
        "Telefone" : telefone_cliente,
        "E-mail" :email_cliente
    }

    banco.append(novo_cliente)
    print("Cadastro realizado com sucesso.")
