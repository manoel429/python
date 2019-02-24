print(" Execício 7.7 Modifique o programa de forma a escrever a palavra secreta caso o jogador perca\n.")

palavra = input("Digite a palavra secreta: ").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha=""
    for letra in palavra:
        senha +=letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print(" Você acertou!")
        break
    tentativa = input("\n Digite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros +=1
            print(" Você errou!")
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2=""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3=""
    if erros == 5:
        linha3+=" /  "
    elif erros>=6:
        linha3+=" / \ "
    print("X%s" % linha3)
    print("X\n============")
    if erros == 6:
        print("Enforcado! A palavra secreta era %s." % palavra)
        break
