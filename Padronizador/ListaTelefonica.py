

user = []

while True:
    adicionar = input("Adicionar novo usuario: 1 Sim, 2 Nao\n")

    if adicionar == "1":
        name = input("Nome: ")
        phone = input("Telefone, formato recomendado (99) 99999-9999: ")

        phone = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        user.append({"Nome": name, "Telefone": phone})

        print(f"Usuario {name} cadastrado com sucesso!")

    elif adicionar == "2":
        print("Encerrando ...")
        break
    
    else:
        print("Opcao invalida! Tente novamente.")
    

print("---------Usuarios cadastrados---------")
for usuario in user:
    print(f"Nome: {usuario['Nome']}, Telefone: {usuario['Telefone']}\n")