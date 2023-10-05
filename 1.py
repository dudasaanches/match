num = int(input("Digite um número: "))
match num:
    case 1:
        print("Digitou 1")
    case 2:
        print("Digitou 2")
    case 3:
        print("Digitou 3")
    case _:
        print("Outro número")