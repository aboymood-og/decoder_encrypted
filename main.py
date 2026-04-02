Binario = '*'
BinarioDic = ["0","1"]

Octal = '&'
OctalDic = ["0","1","2","3","4","5","6","7"]

Decimal = '#'
DecimalDic = ["0","1","2","3","4","5","6","7","8","9"]

Hex = '!'
HexDic = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

Caracteres_Validos = ["*", "&", "#", "!", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

#Esta funcion lo que hace es leer el archivo caracter por caracter y lo ordena como una gran lista con listas internas las cuales, en principio y sin limpiar, cada sublista seria igual a un caracter ASCII
def archiveToList(texto):
    #Lectura de .txt caracter por caracter
    archivo = open(texto, mode="r")

    list = []

    i = -1
    while True:
        lst = []
        if i != -1:
            archivo.seek(i)
            caracter = archivo.read(1)
            lst.append(caracter)
        i += 1
        archivo.seek(i)
        caracter = archivo.read(1)

        if caracter != Binario or caracter != Octal or caracter != Decimal or caracter != Hex:
            lst.append(caracter)
            i += 1
            archivo.seek(i)
            caracter = archivo.read(1)
            
            while True:
                lst.append(caracter)
                i += 1
                archivo.seek(i)
                caracter = archivo.read(1)

                if caracter == Binario or caracter == Octal or caracter == Decimal or caracter == Hex or not caracter:
                    break

            
        list.append(lst)

        if not caracter:
            break
    archivo.close()

    #print(list)
    print(f"[+] Procesando archivo: {texto}")
    return list

#En este def intentaré limpiar la basura, osea, si hay alguna sublista de la lista que tenga un caracter fuera de lo que deberia, fuera. Tomare como "basura" si un posible numero contiene algo fuera de su rango serpa automaticamente descartado de momento (ex: *012, descartado completo por tener un 2, fuera de su rango); quiza cambio esto en un futuro a que primero recorra todo el string y elimine el ruido antes de pasarlo a una superlista, dependiendo si de la forma anterior me dan los resultados esperados o no
def filtadoDeDatos(lista):
    #Limpieza de "basura" en cada sublista
    i = 0
    aux = True
    while aux:
        for x in range(len(lista[i])):
            if lista[i][x] not in Caracteres_Validos:
                lista.pop(i)
                x = 0
                i -= 1 
                break
            else:
                x += 1
        i += 1
        if i >= len(lista):
            aux = False
        
    #Corroborar que cada sublista tenga los digitos correspondientes a su base


    return lista

        
        


#Programa principal:

megalista = archiveToList("prueba_1.txt")
cleanlst = filtadoDeDatos(megalista)
print(cleanlst)
