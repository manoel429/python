print("Exercício 5.25 Escreva um programa que calcule a raiz \n"
"quadrada de um número. Utilize o método de Newton para obter\n"
"um resultado aproximado. Sendo n o número a obter a raiz\n"
"quadrada, considere a base b=2. Calcule p usando a fórmula\n"
"p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo,\n"
"faça b=p e recalcule p usando a fórmula apresentada. Pare\n"
"quando a diferença absoluta entre n e o quadrado de p for\n"
"menor que 0,0001.\n")

n = int(input("Digite um número: "))
base = 2
p = 0
while  True:

    p = (base+(n/base))/2
    b = p

print(" Número = %d \n Base = %d \n p = %d " % (n,base,p))
