login = str(input("Digite seu login: "))
senha = str(input("Digite a sua senha: "))
match(login, senha):
    case ("Ana Luiza", "123"):
        print("Usuario logado com sucesso")

    case ("Breno", "321"):
        print("Administradora logada com sucesso")

    case _:
        print("Login ou senha incorreto")