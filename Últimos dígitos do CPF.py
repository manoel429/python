print("Esse programa vai identificar os Ultimos dois numeros do RG")

C1 = int(input("digite o primeiro digito ="))
C2 = int(input("digite o segundo digito ="))
C3 = int(input("digite o terceiro digito ="))
C4 = int(input("digite o quarto digito ="))
C5 = int(input("digite o quinto digito ="))
C6 = int(input("digite o sexto digito ="))
C7 = int(input("digite o setimo digito ="))
C8 = int(input("digite o oitavo digito ="))
C9 = int(input("digite o nono digito ="))
#C10 = 0
#C11 = None
#res_C10 = None

res_C10 = int ((C1*1)+(C2*2)+(C3*3)+(C4*4)+(C5*5)+(C6*6)+(C7*7)+(C8*8)+(C9*9))
resto_div_C10 = int(res_C10 % 11)
res_C11 = int ((C1*9)+(C2*8)+(C3*7)+(C4*6)+(C5*5)+(C6*4)+(C7*3)+(C8*2)+(C9*1)  )
resto_div_C11 = int(res_C11 % 11)
print("decimo numero = %d e decimo primeiro = %d " % (resto_div_C10, resto_div_C11))

#res_C10 = ((C1*9)+(C2*8)+(C3*7)+(C4*6)+(C5*5)+(C6*4)+(C7*3)+(C8*2)+(C9*1)/11)

#div_res_C10 = (res_C10 % 11)
#str_div_res_C10 = str(div_res_C10)

#if div_res_C10 == 0 or 1:
#    C10 = (0)

#    print (C10)

#else:
#    C10 = (11 - (div_res_C10))

#    print (C10)
