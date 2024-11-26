def calculo ():
    exp = input("Calculo: ").strip().split()

    p1 = None
    p2 = None
    expre = None

    for token in exp:
        match token:
            case "+" | "-" | "*" | "/":
                expre = token
            case _:
                if p1 == None:
                    p1 = float(token)
                else:
                    p2 = float(token)

    match expre:
        case "+":
            print(p1 + p2)
        case "-":
            print(p1 - p2)
        case "*":
            print(p1 * p2)
        case "/":
            print(p1 / p2)

calculo()