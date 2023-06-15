

def suma (a,b):
    '''suma 2 valores'''
    resultado = a+b
    return resultado

def resta (a,b):
    '''resta 2 valores '''
    return  a-b
    
def multiplicacion (a,b):
    '''multiplica 2 valores '''
    return  a*b

def division (a,b):
    '''divide 2 valores '''
    return  a/b

def exponenciacion (a,b):
    '''eleva un numero'''
    return  a**b

def raices (a):
    ''' raiz de 1 valor '''
    import math
    return math.sqrt (a)

def suma5 ():
    suma = 0
    for i in range (0,5):
        h= int (input ("ingrese un numero "))
        suma = suma + h 
    print (suma)

suma5()
