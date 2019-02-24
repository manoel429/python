print(' Exercício 8.11 Escreva uma função para validar uma variável\n'
'string. Essa função recebe como parâmetro a string, o número mínimo\n'
'e máximo de caracteres. Retorne verdadeiro se o tamanho da string\n'
'entre os valores de máximo e mínimo, e falso em caso contrário.\n')
def tam(ask,mín,máx):
    str = input(ask)
    if len(str)<mín or len(str)>máx:
        print('Senha inválida! Digite um valor entre %d e %d'% (mín,máx))
    else:
        return ("OK")

senha = input("Digite uma senha com no mínimo 5 caracteres e no máximo 8:")
carac = int(len(senha))
tam(senha,5,8)
