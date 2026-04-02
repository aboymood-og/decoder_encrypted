Binario = '*'
BinarioDic = ["0","1"]

Octal = '&'
OctalDic = ["0","1","2","3","4","5","6","7"]

Decimal = '#'
DecimalDic = ["0","1","2","3","4","5","6","7","8","9"]

Hex = '!'
HexDic = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

Caracteres_Validos = ["*", "&", "#", "!", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

Diccionario_ascii = {
    " ": [32, 20, 40, 100000],
    "!": [33, 21, 41, 100001],
    '"': [34, 22, 42, 100010],
    
}

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

    print(list)
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

#Este def se encargara de recorrer la lista procesada y crear una nueva lista con los numeros originales transformados a la base requerida.
def listToBaseRquired(lista_og, base_required):
    lista_transform = []
    for i in range(len(lista_og)):
        if base_required == 2:
            num = toBinary(lista_og[i])
        elif base_required == 8:
            num = toOctal(lista_og[i])
        elif base_required == 10:
            num = toDecimal(lista_og[i])
        elif base_required == 16:
            num = toHex(lista_og[i])
        lista_transform.append(num)
    return lista_transform
        

#ex de num a recibir: num = ['!', '0', '1']

#aca mas de lo mismo pero para octal
def toBinary(num):
    pass

#aca mas de lo mismo pero para octal
def toOctal(num):
    pass

#En este def aplicare un polinomio caracteristico para pasar de cualquier base disponible a decimal en caso de ser necesario.
def toDecimal(num):
    if num[0] == "*":
        pot = 2
    elif num[0] == "&":
        pot = 8
    elif num[0] == "#":
        pot = 10
    elif num[0] == "!":
        pot = 16
        #aplicar algun tipo de mapeo de A a F como 10 a 15 y reemplazar cada valor unico.
    
    num_transformed = 0
    for i in range(len(num)-1):
        aux = int(num[i+1])
        i *= 1
        aux2 = aux * pot**(len(num)-2-i)
        num_transformed += aux2

    return num_transformed
        
#aca mas de lo mismo pero para hex
def toHex(num):
    pass

#def para decodificar to ascii


#numero en lista separado tpo [["","",""]] to string como tal, unido, 1 solo







#Programa principal:
print("--- DECODIFICADOR DE NOTAS ---")

base_status = False
while not base_status:
    base = int(input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): "))
    if base == 2 or base == 8 or base == 10 or base == 16:
        base_status = True
    else:
        print("Porfavor, eliga una de las bases disponibles")


archivo_procesado = archiveToList("prueba_1 copy.txt")
archivo_filtrado = filtadoDeDatos(archivo_procesado)

print(f"LISTA DE VALORES EXTRAÍDOS (Base {base}):\n--------------------------------------------------")

archivo_trasnformado = listToBaseRquired(archivo_filtrado, base)

for i in range(len(archivo_trasnformado)):
    print(f"Valor {i}: {archivo_trasnformado[i]}\t(Original: {archivo_procesado[i]})")

print("--------------------------------------------------")

print("MENSAJE DECODIFICADO: ")
#FUNCION PARA DECODIFICAR

print("[Proceso finalizado con éxito]")