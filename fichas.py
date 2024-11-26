def listas():
    def list():
        #dicionario
        player = [
            {"Nome" : "Jhon" , "Idade" : "32" , "Origem" : "Criminoso" , "Papel" : "Assassino"},
            {"Nome" : "Clair" , "Idade" : "26" , "Origem" : "Idolo" , "Papel" : "Cantor"},
            {"Nome" : "Apollo" , "Idade" : "25" , "Origem" : "Technomédico" , "Papel" : "Químico"},
        ]

        npc = [
            {"Nome" : "Lorrenzo" , "Idade" : "47" , "Origem" : "Solo" , "Papel" : "Mercenario"},
            {"Nome" : "Angelica" , "Idade" : "48" , "Origem" : "Corporativo" , "Papel" : "Atravessador"},
            {"Nome" : "Rafaela" , "Idade" : "30" , "Origem" : "Netruner" , "Papel" : "Seeker"},
        ]

        #opções
        op = int(input("1 Para abrir lista de opções. | 2 Para escolher a opção. "))

        if op == 1:
            print("Lista de opções:")
            print("Players/jogadores:")
            for nome in player:
                print(nome["Nome"])
                print("----------")
            print(" ")

            print("Não jogaveis/Npc's")
            for nome in npc:
                print(nome["Nome"])
                print("----------")
            
            fc = input("Qual ficha você deseja abrir? ").title()
            for nome in player:
                if nome["Nome"] == fc:
                    print("Nome:", nome["Nome"])
                    print("Idade:", nome["Idade"])
                    print("Origem:", nome["Origem"])
                    print("Papel:", nome["Papel"])
            for nome in npc:
                if nome["Nome"] == fc:
                    print("Nome:", nome["Nome"])
                    print("Idade:", nome["Idade"])
                    print("Origem:", nome["Origem"])
                    print("Papel:", nome["Papel"])
            
        elif op == 2:
            fc = input("Qual ficha você deseja abrir? ").title()
            for nome in player:
                if nome["Nome"] == fc:
                    print("Nome:", nome["Nome"])
                    print("Idade:", nome["Idade"])
                    print("Origem:", nome["Origem"])
                    print("Papel:", nome["Papel"])
            for nome in npc:
                if nome["Nome"] == fc:
                    print("Nome:", nome["Nome"])
                    print("Idade:", nome["Idade"])
                    print("Origem:", nome["Origem"])
                    print("Papel:", nome["Papel"])

        else:
            print("Erro x_x")

    #começo
    loop1 = True
    while loop1 == True:

        list()
        p = input("Gostaria de ver outra ficha? ").title()

        match p:
            case "Sim" | "S" | "Yes" :      
                loop1 = True
            case "Não" | "N" | "No" :
                print("Até mais!")
                loop1 = False
            case _:
                print("Erro x_x")
                loop1 = False

listas()