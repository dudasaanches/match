animal = str(input("Digite um animal: ")).lower()
match animal:
    case ("vaca"|"galinha"|"ovelha"):
        print(f"Digitou {animal} ")
    case _:
        print("Animal desconhecido")