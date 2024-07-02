import random

def jogar():
    print("**********************************")
    print("***Bem Vindo ao jogo de Adivinhação***!")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_tentativas = 5
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 20

    for rodada in range(1,total_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou o número ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Número inválido! Insira um entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu número foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! Seu número foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()