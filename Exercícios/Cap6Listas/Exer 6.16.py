print("Exercício 6.16 Modifique o programa da listagem 6.44 para\n"
"ordenar a lista em ordem decrescente. L=[1,2,3,4,5] deve ser ordenada\n"
"como L=[5,4,3,2,1].\n")

L=[1,2,3,4,5]
fim=5
while fim > 1:
    trocou=False
    x=0
    while x<(fim-1):
        if L[x]<L[x+1]:
            trocou=True
            temp=L[x+1]
            L[x+1]=L[x]
            L[x]=temp
        x+=1
    if not trocou:
        break
    fim-=1
for e in L:
    print(e, end=" ")
