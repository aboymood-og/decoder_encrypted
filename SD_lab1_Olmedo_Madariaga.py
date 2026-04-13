#CONSTANTS
VALID_CHAR = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "*", "&", "#", "!"] 

BIN_PREFIX = VALID_CHAR[16]
BIN_BASE = VALID_CHAR[0:2]

OCT_PREFIX = VALID_CHAR[17]
OCT_BASE = VALID_CHAR[0:8]

DEC_PREFIX = VALID_CHAR[18]
DEC_BASE = VALID_CHAR[0:10]

HEX_PREFIX = VALID_CHAR[19]
HEX_BASE = VALID_CHAR[0:16]
HEX_DIC = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

VALID_PREFIX = [BIN_PREFIX, OCT_PREFIX, DEC_PREFIX, HEX_PREFIX]

DIC_ASCII = {
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


#funciones_del_programa
def read_file(path_file): #return lista ; ex = ['!', '!', 'X', 'Y', 'z', '#', '8', '4', '-', '-', '-', 'a', 'b', 'c']
    print(f"\n[+] Procesando archivo: {path_file}\n")
    file = open(path_file, mode="r")
    file_read = []
    file_read_finish = False
    i = 0
    while not file_read_finish:
        file.seek(i)
        character_file = file.read(1) 
        if character_file == "":
            file_read_finish = True
        else:      
            file_read.append(character_file) 
        i += 1                
    file.close()

    return file_read

def exctract_valid_char(read_file):#FILTRO Ignorar Basura: Cualquier caracter que no sea un prefijo valido o un dıgito perteneciente a su base debe ser ignorado silenciosamente sin detener la ejecución.; return list of strings
    filter1_file = []
    current_char = []
    current_prefix = None

    for i in range(len(read_file)):
        character = read_file[i]

        if character in VALID_PREFIX:
            if len(current_char) > 1:
                delimiter = ""
                join_str = delimiter.join(current_char)
                filter1_file.append(join_str)
            current_char = [character]
            current_prefix = character
            
        elif current_prefix != None:
            if current_prefix == BIN_PREFIX and character in BIN_BASE:
                current_char.append(character)
            elif current_prefix == OCT_PREFIX and character in OCT_BASE:
                current_char.append(character)
            elif current_prefix == DEC_PREFIX and character in DEC_BASE:
                current_char.append(character)
            elif current_prefix == HEX_PREFIX and character in HEX_BASE:
                current_char.append(character)

    if len(current_char) > 1:
        delimiter = ""
        join_str = delimiter.join(current_char)
        filter1_file.append(join_str)

    return filter1_file

def filter_ascii_valid_range(file_char_filt1):#FILTRO Solo se consideran valores validos aquellos cuyo equivalente decimal este entre el rango 32 y 126 (caracteres ASCII imprimibles).return list of strings
    clean_file = []
    
    for i in range(len(file_char_filt1)):
        char = file_char_filt1[i]
        num_dec = to_decimal(char)        
        if 32 <= num_dec <= 126:
            clean_file.append(char)
            
    return clean_file

def clean_file_to_base_required(clean_file, base_required): #CAPAZ SE PODRIA APROVECHAR QUE YA PASAMOS ALL A DECIMAL EN EL DEF ANTERIOR, GUARDARLO EN UNA LISTA Y RETURNEARLO APRA USARLO ACA Y ASI NO TENER 2 FOR QUE HACEN LO MISMO PERO QUIZA LO VEO DESPUES JAJA
    file_transformed = []
    for i in range (len(clean_file)):
        num_dec = to_decimal(clean_file[i])
        if base_required == 10:
            num = num_dec
        else:
            num = dec_to_bin_oct_hex(num_dec,base_required)
        file_transformed.append(num)

    return file_transformed

def to_decimal(num): #recibe un str
    if num[0] == BIN_PREFIX:
        pot = 2
    elif num[0] == OCT_PREFIX:
        pot = 8
    elif num[0] == DEC_PREFIX:
        pot = 10
    elif num[0] == HEX_PREFIX:
        pot = 16
        num = list(num)
        for i in range(len(num)):
            if num[i] in HEX_DIC:
                num[i] = str(HEX_DIC.get(num[i]))
        
    num_decimal = 0
    for i in range(len(num)-1):
        aux = int(num[i+1])
        aux2 = aux * pot**(len(num)-2-i)
        num_decimal += aux2 
    
    return num_decimal

def dec_to_bin_oct_hex(num, base_required):
    character_transformed = []

    finish = False
    while not finish:
        rest = num % base_required
        num = num // base_required
        
        if rest > 9:
            key = [k for k, v in HEX_DIC.items() if v == rest]
            key = "".join(map(str, key))
            character_transformed.append(key)
        else:
            character_transformed.append(rest)

        if num == 0:
            finish = True
    character_transformed.reverse()
    character_transformed = "".join(map(str, character_transformed))
    if base_required == 16:
        return character_transformed
    else:
        character_transformed = int(character_transformed)
        return character_transformed
    
def decode_ascii(encode_file, base):
    decode_msg = ""

    if base == 2:
        aux = 3
    elif base == 8:
        aux = 2
    elif base == 10:
        aux = 0
    elif base == 16:
        aux = 1

    for i in range(len(encode_file)):
        key = None
        for k, v in DIC_ASCII.items():
            if encode_file[i] == v[aux]:
                key = k
                break
        if key != None:
            decode_msg += key
    
    return decode_msg

def main():
    print("--- DECODIFICADOR DE MENSAJES ---\n")

    #Elegir por teclado la base a la que se quiere transformar el mensaje encripado
    base = False
    while not base:
        base_required = input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16):")
        if base_required in ("2", "8", "10", "16"):    
            base = True
            base_required = int(base_required)
        else:
            print("Porfavor, eliga una de las bases disponibles")

    file_read = read_file("prueba_1.txt")

    filter1_file = exctract_valid_char(file_read)

    print("[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n")

    clean_file = filter_ascii_valid_range(filter1_file)

    print(f"LISTA DE VALORES EXTRAÍDOS (Base {base_required}):\n--------------------------------------------------")

    transformed_file = clean_file_to_base_required(clean_file, base_required)

    #Imprimir tabla
    for i in range(len(clean_file)):
        value = clean_file[i]
        if value == "": 
            base_og = ""
        elif value[0] == "*":
            base_og = "Binario "
        elif value[0] == "&":
            base_og = "Octal "
        elif value[0] == "#":
            base_og = "Decimal "
        elif value[0] == "!":
            base_og = "Hexadecimal "
        print(f"Valor {i}: {transformed_file[i]}\t(Original: {base_og}{value})")

    #Imprimir por pantalla el mensaje decodificado
    print("--------------------------------------------------\n\nMENSAJE DECODIFICADO: ")
    decode_msg = decode_ascii(transformed_file, base_required)
    print(decode_msg)

    print("\n[Proceso finalizado con éxito]")

#ejectuar main()
if __name__ == "__main__":
    main()