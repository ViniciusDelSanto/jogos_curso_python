import random
import palavras_dados
# pip install unidecode
from unidecode import unidecode
def jogar():
    print("*****************************")
    print(" Bem Vindo ao Jogo da Forca! ")
    print("*****************************")
    print("Descubra a palavra a seguir: ")

    palavra = random.choice(palavras_dados.palavras_dados).upper()
    palavra_sem_acentos = unidecode(palavra)
    num_caracteres = len(palavra)
    letras_certas = ["_" for _ in range(num_caracteres)]
    
    enforcou = False
    acertou = False
    erros = 0

    print(f"Palavra de {num_caracteres} letras!")
    print(" ".join(letras_certas))
    
    # while True e True
    while not enforcou and not acertou:

        chute = input("Digite uma letra:")
        chute = unidecode(chute.strip().upper())

        if len(chute) != 1 or not chute.isalpha():
            print("Por favor, digite apenas uma letra válida!")
            continue

        elif chute in palavra_sem_acentos:
            index = 0
            for letra in palavra:
                if chute == letra:
                    letras_certas[index] = palavra[index]
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {7-erros} tentativas.")

        enforcou = erros == 7
        acertou = "_" not in letras_certas
        print(" ".join(letras_certas))

    if acertou:
        print("Voce ganhou!!!")
    else:
        print("Voce perdeu!!!")
        print("A palavra era: {}".format(palavra))


    print("Fim de Jogo")


if __name__ == "__main__":
    jogar()