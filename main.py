import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    while tentativas == 0:
        print("Escolha o nível de dificuldade: \n1 fácil\n2 médio\n3 difícil ")
        escolha = int(input('=> '))
        if escolha == 1:
            tentativas = 10
        elif escolha == 2:
            tentativas = 5
        elif escolha == 3:
            tentativas = 1
        else:
            print ("Escolha inválida")
    print(f"Você tem {tentativas} tentativas.")

    while tentativas > 0:
        chute = int(input("Digite seu chute: "))

        if chute < numero_secreto:
            print("O número secreto é maior.")
        elif chute > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("Parabéns! Você acertou!")
            return

        tentativas -= 1
        if tentativas > 0:
            print(f"Você tem mais {tentativas} tentativas.")

    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)


jogo_adivinhacao()
