
def apaga(lista):
    x = 0
    lista2 = []
    lista3 = []
    c = len(lista) - 1
    while c >= 0:
        for n in lista:
            for x in lista:
                lista2.append(n)
                del lista[0]
                for x in lista:
                    if x != n:
                        lista3.append(x)
                del lista[0:]
                lista = lista3[:]
                del lista3[0:]
        c = c - 1
    lista = lista2[:]
    return lista


def remove_repetidos(lista):
    lista2 = []
    x = 0
    n = 0
    y = 0
    c = len(lista) - 1
    while c >= 0:
        for x in lista:
            for n in lista:
                while x > n:
                    n < x in lista
                    if True:
                        lista = [n] + lista
                        x = lista[0]
                    if False:
                        lista = lista[:(c)] + [n] + lista[(c):]
                        x = lista[0]
        lista2.append(x)
        lista = apaga(lista)
        c = len(lista) - 1
        lista = lista[1:]
        c = c - 1
    lista = lista2[:]
    print(lista)
                          
                        

            
                         
            
   


        
    
        
        
           
  
