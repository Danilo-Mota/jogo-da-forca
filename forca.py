import random

palavras = ["python", "programacao", "jogo", "computador", "desenvolvedor"]

palavra = random.choice(palavras)

letras = list(palavra)
palavraEscondida = ["_"] * len(letras)


maximoDeTentativas = 6
tentativasErradas = 0
acertos = 0

while tentativasErradas < maximoDeTentativas and acertos < len(letras):
    print("Palavra: " + " ".join(palavraEscondida))
    letra = input("Digite uma letra: ")

    if letra in letras:
        print("Acertou!")
        for i in range(len(letras)):
            if letras[i] == letra:
                palavraEscondida[i] = letra
        acertos += 1
    else:
        print("Errou!")
        tentativasErradas += 1

if acertos == len(letras):
    print("Parabéns, você ganhou!")
else:
    print("Você perdeu. A palavra era:", palavra)
