def vetical ():
    coluna = int(input("Qual o tamanho da coluna? "))

    while coluna >= 0:
        print("?")
        coluna -= 1

vetical()

def horizontal ():
    linha = int(input("Qual o tamanho da linha? "))
    print("?" * linha)

horizontal()

def ambos ():
    linha = int(input("Qual o tamanho da linha? "))
    coluna = int(input("Qual o tamanho da coluna? "))
    print("?" * linha)

    while coluna >= 2:
        print("?" * linha)
        coluna -= 1

ambos()