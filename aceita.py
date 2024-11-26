def termos (txt="Termos..."):
    termos= txt
    print(termos)
    per= input("Você concorda com os termos? ").title()
    match per:
        case "Sim" | "S" | "Concordo" | "Yes" | "Yep":
            print("Termos aceitos.")
            per= "S"
        case "Não" | "N" | "Não concordo" |"No" | "Nop" :
            print("Termos negados")
            per= "N"
        case _:
            print("Sem resposta. . .")