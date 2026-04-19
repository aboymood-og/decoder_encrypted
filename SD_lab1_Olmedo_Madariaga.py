#Link a mi GitHub con el progreso del lab: https://github.com/aboymood-og/decoder_encrypted

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
HEX_DIC_INV = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

VALID_PREFIX = [BIN_PREFIX, OCT_PREFIX, DEC_PREFIX, HEX_PREFIX]

#funciones_del_programa
def read_file(path_file): 
    print(f"\n[+] Procesando archivo: {path_file}\n")
    
    try:
        with open(path_file, mode="r") as file:
            return file.read()
            
    except FileNotFoundError:
        print(f"[!] No se pudo encontrar el archivo {path_file}.\n Asegúrate de que el archivo esté en el mismo directorio que el script.")
        return None
    
    except Exception as e:
        print(f"[!] Ocurrió un error inesperado al leer el archivo: {e}")
        return None

def exctract_valid_char(read_file):#FILTRO Ignorar Basura: Cualquier caracter que no sea un prefijo valido o un dıgito perteneciente a su base debe ser ignorado silenciosamente sin detener la ejecución.; return list of strings
    filter1_file = []
    current_char = []
    current_prefix = None

    for character in read_file:
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
            elif current_prefix == HEX_PREFIX and character.upper() in HEX_BASE:
                current_char.append(character.upper())

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
            clean_file.append((char, num_dec))
            
    return clean_file

def clean_file_to_base_required(clean_file, base_required): 
    file_transformed = []
    for i in clean_file:
        char_og = i[0]
        num_dec = i[1]
        if base_required == 10:
            num = num_dec
        else:
            num = dec_to_bin_oct_hex(num_dec, base_required)
        file_transformed.append(num)

    return file_transformed

def to_decimal(num): 
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
            character_transformed.append(HEX_DIC_INV[rest])
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
    
def decode_ascii(clean_file):
    decode_msg = ""
    for i in clean_file:
        num_dec = i[1]
        decode_msg += chr(num_dec)

    return decode_msg

def main():
    print("--- DECODIFICADOR DE MENSAJES ---\n")

    text_to_process = "notas_dm.txt"

    #Elegir por teclado la base a la que se quiere transformar el mensaje encripado
    base = False
    while not base:
        base_required = input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16):")
        if base_required in ("2", "8", "10", "16"):    
            base = True
            base_required = int(base_required)
        else:
            print("Porfavor, eliga una de las bases disponibles")

    file_read = read_file(text_to_process)

    if file_read is None:
        print("\n[Proceso terminado por error del archivo a procesar]")
        return

    filter1_file = exctract_valid_char(file_read)

    print("[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n")

    clean_file = filter_ascii_valid_range(filter1_file)

    print(f"LISTA DE VALORES EXTRAÍDOS (Base {base_required}):\n--------------------------------------------------")

    transformed_file = clean_file_to_base_required(clean_file, base_required)

    #Imprimir tabla
    for i in range(len(clean_file)):
        value = clean_file[i][0]
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
    decode_msg = decode_ascii(clean_file)
    print(decode_msg)

    print("\n[Proceso finalizado con éxito]")

#ejectuar main()
if __name__ == "__main__":
    main()