Binario = '*'
BinarioDic = ["0","1"]

Octal = '&'
OctalDic = ["0","1","2","3","4","5","6","7"]

Decimal = '#'
DecimalDic = ["0","1","2","3","4","5","6","7","8","9"]

Hex = '!'
HexDic = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
HexDic2 = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

Caracteres_Validos = ["*", "&", "#", "!", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

Sistemas_numericos = ["*", "&", "#", "!"]

Diccionario_ascii = {
    #    dec   hex    oct    bin
    " ": [32,  "20",  40,  100000],
    "!": [33,  "21",  41,  100001],
    '"': [34,  "22",  42,  100010],
    "#": [35,  "23",  43,  100011],
    "$": [36,  "24",  44,  100100],
    "%": [37,  "25",  45,  100101],
    "&": [38,  "26",  46,  100110],
    "'": [39,  "27",  47,  100111],
    "(": [40,  "28",  50,  101000],
    ")": [41,  "29",  51,  101001],
    "*": [42,  "2A",  52,  101010],
    "+": [43,  "2B",  53,  101011],
    ",": [44,  "2C",  54,  101100],
    "-": [45,  "2D",  55,  101101],
    ".": [46,  "2E",  56,  101110],
    "/": [47,  "2F",  57,  101111],
    "0": [48,  "30",  60,  110000],
    "1": [49,  "31",  61,  110001],
    "2": [50,  "32",  62,  110010],
    "3": [51,  "33",  63,  110011],
    "4": [52,  "34",  64,  110100],
    "5": [53,  "35",  65,  110101],
    "6": [54,  "36",  66,  110110],
    "7": [55,  "37",  67,  110111],
    "8": [56,  "38",  70,  111000],
    "9": [57,  "39",  71,  111001],
    ":": [58,  "3A",  72,  111010],
    ";": [59,  "3B",  73,  111011],
    "<": [60,  "3C",  74,  111100],
    "=": [61,  "3D",  75,  111101],
    ">": [62,  "3E",  76,  111110],
    "?": [63,  "3F",  77,  111111],
    "@": [64,  "40", 100, 1000000],
    "A": [65,  "41", 101, 1000001],
    "B": [66,  "42", 102, 1000010],
    "C": [67,  "43", 103, 1000011],
    "D": [68,  "44", 104, 1000100],
    "E": [69,  "45", 105, 1000101],
    "F": [70,  "46", 106, 1000110],
    "G": [71,  "47", 107, 1000111],
    "H": [72,  "48", 110, 1001000],
    "I": [73,  "49", 111, 1001001],
    "J": [74,  "4A", 112, 1001010],
    "K": [75,  "4B", 113, 1001011],
    "L": [76,  "4C", 114, 1001100],
    "M": [77,  "4D", 115, 1001101],
    "N": [78,  "4E", 116, 1001110],
    "O": [79,  "4F", 117, 1001111],
    "P": [80,  "50", 120, 1010000],
    "Q": [81,  "51", 121, 1010001],
    "R": [82,  "52", 122, 1010010],
    "S": [83,  "53", 123, 1010011],
    "T": [84,  "54", 124, 1010100],
    "U": [85,  "55", 125, 1010101],
    "V": [86,  "56", 126, 1010110],
    "W": [87,  "57", 127, 1010111],
    "X": [88,  "58", 130, 1011000],
    "Y": [89,  "59", 131, 1011001],
    "Z": [90,  "5A", 132, 1011010],
    "[": [91,  "5B", 133, 1011011],
    "\\": [92, "5C", 134, 1011100],
    "]": [93,  "5D", 135, 1011101],
    "^": [94,  "5E", 136, 1011110],
    "_": [95,  "5F", 137, 1011111],
    "`": [96,  "60", 140, 1100000],
    "a": [97,  "61", 141, 1100001],
    "b": [98,  "62", 142, 1100010],
    "c": [99,  "63", 143, 1100011],
    "d": [100, "64", 144, 1100100],
    "e": [101, "65", 145, 1100101],
    "f": [102, "66", 146, 1100110],
    "g": [103, "67", 147, 1100111],
    "h": [104, "68", 150, 1101000],
    "i": [105, "69", 151, 1101001],
    "j": [106, "6A", 152, 1101010],
    "k": [107, "6B", 153, 1101011],
    "l": [108, "6C", 154, 1101100],
    "m": [109, "6D", 155, 1101101],
    "n": [110, "6E", 156, 1101110],
    "o": [111, "6F", 157, 1101111],
    "p": [112, "70", 160, 1110000],
    "q": [113, "71", 161, 1110001],
    "r": [114, "72", 162, 1110010],
    "s": [115, "73", 163, 1110011],
    "t": [116, "74", 164, 1110100],
    "u": [117, "75", 165, 1110101],
    "v": [118, "76", 166, 1110110],
    "w": [119, "77", 167, 1110111],
    "x": [120, "78", 170, 1111000],
    "y": [121, "79", 171, 1111001],
    "z": [122, "7A", 172, 1111010],
    "{": [123, "7B", 173, 1111011],
    "|": [124, "7C", 174, 1111100],
    "}": [125, "7D", 175, 1111101],
    "~": [126, "7E", 176, 1111110],
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

    #print(list)
    print(f"\n[+] Procesando archivo: {texto}")
    return list

#limpieza de datoshkis jajjajaj
def filtadoDeDatos(lista):
    #Eliminar caracteres que no sean validos
    for i in range(len(lista)):
        y2 = 0
        for y in range(len(lista[i])):
            if lista[i][y2] not in Caracteres_Validos:
                lista[i].pop(y2)
            else:
                y2 += 1
    
    for i in range(len(lista)):
        y2 = 0
        for y in range(len(lista[i])):
            if lista[i][y2] in Sistemas_numericos and lista[i][y2+1] in Sistemas_numericos:
                lista[i].pop(y2)
            else:
                y2 += 1
    #print("lista filtrada paso 1?", lista)
       
    #Limpieza de "basura" en cada sublista
    #i = 0
    #aux = True
    #while aux:
    #    for x in range(len(lista[i])):
    #        if lista[i][x] not in Caracteres_Validos:
    #            lista.pop(i)
    #            x = 0
    #            i -= 1 
    #            break
    #            else:
    #            x += 1
    #    i += 1
    #    if i >= len(lista):
    #        aux = False
        
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
    if num == []:
        return None
    elif num[0] == "*":
        pot = 2
    elif num[0] == "&":
        pot = 8
    elif num[0] == "#":
        pot = 10
    elif num[0] == "!":
        pot = 16
        for i in range(len(num)):
            if num[i] in HexDic2:
                num[i] = str(HexDic2.get(num[i]))
                    
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
def decodeASCII(msj_og,base):
    msj_decode = []

    if base == 2:
        aux = 3
    elif base == 8:
        aux = 2
    elif base == 10:
        aux = 0
    elif base == 16:
        aux = 1

    for i in range(len(msj_og)):
        key = [k for k, v in Diccionario_ascii.items() if msj_og[i] == v[aux]]
        msj_decode.append(key)

    msj_decode_ite = filter(None, msj_decode)
    msj_decode_fin = list(msj_decode_ite)

    return msj_decode_fin



    for i in range():
        pass

#numero en lista separado tpo [[""],[""],[""]] to string como tal, unido, 1 solo
def listToString(lista):
    res = ""
    for i in range(len(lista)):
        res += lista[i][0]

    return res





#Programa principal:
print("--- DECODIFICADOR DE NOTAS ---\n")

base_status = False
while not base_status:
    base = int(input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16):"))
    if base == 2 or base == 8 or base == 10 or base == 16:
        base_status = True
    else:
        print("Porfavor, eliga una de las bases disponibles")


archivo_procesado = archiveToList("notas_dm.txt")

print("[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n")

archivo_filtrado = filtadoDeDatos(archivo_procesado)

print(f"LISTA DE VALORES EXTRAÍDOS (Base {base}):\n--------------------------------------------------")

archivo_trasnformado = listToBaseRquired(archivo_filtrado, base)

for i in range(len(archivo_trasnformado)):
    value = listToString(archivo_procesado[i])
    if value == "":
        base_og = ""
    elif value[0] == "*":
        base_og = "Binario "
    elif value[0] == "&":
        base_og = "Octal "
    elif value[0] == "#":
        base_og = "Decimal "
    elif value[0] == "!":
        base_og == "Hexadecimal "
    print(f"Valor {i}: {archivo_trasnformado[i]}\t(Original: {base_og}{value})")

print("--------------------------------------------------\n")

print("MENSAJE DECODIFICADO: ")
mensaje_codificado = decodeASCII(archivo_trasnformado, base)
mensaje_codificado_final = listToString(mensaje_codificado)
print(mensaje_codificado_final)


print("\n[Proceso finalizado con éxito]")