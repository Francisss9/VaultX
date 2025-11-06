nome_jogo = 'Nº random'

import random, time

def main():

    jogar = True

    while jogar:
        numero_secreto = random.randint(1, 25)
        tentativa = 5
        time.sleep(3)
        
        questao = input("Olá, este jogo consiste em descobrir o número secreto (inteiro) no intervalo ]0,25], que foi gerado pelo algoritmo. Queres jogar? \n") 
        vitoria = False
        if questao.strip().lower() == "sim":
            print("Pronto, vamos começar, irá ter 5 tentativas. \n")
        elif questao.strip().lower() == "nao":
            print("Fica para uma próxima então. ")
            break
        else:
            print("Resposta inválida. Por favor, escreva 'sim' para jogar ou 'não' para sair.\n")
            continue

        time.sleep(1)

        while tentativa > 0:
            print(f"Tentativa nº{tentativa}")
            try:
                palpite = int(input("Insira o seu palpite: "))        
            except ValueError:
                print("Entrada inválida, tenta novamente, desta vez com um número inteiro.")
                continue
            if palpite < 1 or palpite > 25:
                print("Fora do intervalo ]0,25] ")
                continue
            elif palpite > numero_secreto:
                if tentativa == 1:
                    break
                else:
                    print("É mais pequeno que esse. ")
                    tentativa -= 1
            elif palpite < numero_secreto:
                if tentativa == 1:
                    break
                else:
                    print("É maior que esse. ")
                    tentativa -= 1
            else:
                vitoria = True
                break

        time.sleep(1)

        if vitoria == False:
            while True:
                resposta_false = input(f"É pena, o número secreto era {numero_secreto}, na próxima consegues... Queres reiniciar o jogo? ")
                if resposta_false.strip().lower() == "sim":
                    print("O jogo está a reiniciar...")
                    time.sleep(1)
                    break
                elif resposta_false.strip().lower() == "nao":
                    print("Volta quando quiseres!")
                    jogar = False
                    break
                else:
                    print("Resposta inválida. Por favor, escreva 'sim' para jogar ou 'não' para sair.")


        elif vitoria == True:
            while True:
                resposta_true = input("Boa, conseguiste, pretendes jogar novamente? \n")
                if resposta_true.strip().lower() == "sim":
                    print("O jogo está a reiniciar...\n\n")
                    time.sleep(1)
                    break
                elif resposta_true.strip().lower() == "nao":
                    print("Volta quando quiseres!")
                    jogar = False
                    break
                else:
                    print("Resposta inválida. Por favor, insere 'sim' para jogar ou 'não' para sair.")