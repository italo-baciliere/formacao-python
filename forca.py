def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = '_'*len(palavra_secreta)

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.lower() == letra.lower()):
                letras_acertadas[index] = letra
                ## alterando o caracter
                #lista = list(letras_acertadas)
                #lista[index] = str(chute.lower())
                #letras_acertadas = "".join(lista)
            index = index + 1
        print(letras_acertadas)

        print("Jogando")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
