login = str(input("Digite seu login: "))
senha = str(input("Digite sua senha: "))

match(login,senha):
    case ("admin", "admin_pass"):
        print("Logado com admin")
    case ("user", "user_pass"):
        print("Logado com user")
    case ("guest", _):
        print("Logado com guest")
    case _:
        print("Login ou senha errado")