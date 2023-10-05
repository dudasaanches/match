cor = str(input("Digite a cor: ")).lower()
match cor:
    case "vermelho":
        print("Cor vermelho")
    case "azul":
        print("Cor azul")
    case "verde":
        print("Cor verde")
    case _:
        print("Cor desconhecida")