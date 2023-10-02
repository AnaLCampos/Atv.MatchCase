numero = int(input("Digite um número inteiro: "))

match numero:
    case 1:
        print("Você digitou o número 1")
    case 2:
        print("Você digitou o número 2")
    case 3:
        print("Você digitou o número 3")
    case _:
        print("Você digitou outro número")