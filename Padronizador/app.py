usuarios = []

while True:
    adicionar = input("Adicionar usuário? 1 para SIM, 2 para NÃO: ")

    if adicionar == "1":
        nome = input("Nome: ")
        telefone = input("Telefone (formato recomendado: (99) 99999-9999): ")

        telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

        usuarios.append({"Nome": nome, "Telefone": telefone})

        print(f"Usuário {nome} adicionado com sucesso! Telefone formatado: {telefone}")
    
    elif adicionar == "2":
        print("Encerrando...")
        break

    else:
        print("Opção inválida, tente novamente.")

print("\nLista de usuários cadastrados:")
for usuario in usuarios:
    print(f"Nome: {usuario['Nome']}, Telefone: {usuario['Telefone']}")
