import random


def jogar():
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3

    for rodada in range (1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Número secreto: {}. Você errou! O seu chute foi maior do que o número secreto.".format(numero_secreto))
            elif (menor):
                print("Número secreto: {}. Você errou! O seu chute foi menor do que o número secreto.".format(numero_secreto))

        rodada = rodada + 1

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()