dia = str(input("Digite um dia da semana: ")).lower()
match dia:
    case ("segunda"|"terça"|"quarta"|"quinta"|"sexta"):
        print(f"{dia} é dia útil")
    case ("sabádo","domingo"):
        print(f"{dia} é fim de semana")