#global variables
Valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "*", "&", "#", "!"] 

Binary_prefix = Valid_characters[16]
Binary_base = Valid_characters[0:1]

Octal_prefix = Valid_characters[17]
Octal_base = Valid_characters[0:7]

Decimal_prefix = Valid_characters[18]
Decimal_base = Valid_characters[0:9]

Hex_prefix = Valid_characters[19]
Hex_base = Valid_characters[0:15]
Hex_dic = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

Valid_prefix = [Binary_prefix, Octal_prefix, Decimal_prefix, Hex_prefix]


def readFileAndIgnoreTrash(path_file):
    
    print(f"\n[+] Procesando archivo: {path_file}\n")

    file = open(path_file, mode="r")

    clean_file = []

    file_is_clean = False
    i = 0
    while not file_is_clean:
        character_clean_file = []

        file.seek(i)
        character_file = file.read(1)

        #condicional para limpiar basura, si no es un caracter valido, lo ignora y pasa al siguiente
        if character_file in Valid_characters:
            character_status = False
            x = i
            while not character_status:
                file.seek(i)
                character_file = file.read(1)
                if character_file in Valid_characters:
                    if character_file in Valid_prefix and x != i:
                        character_status = True
                    else:
                        character_clean_file.append(character_file)
                        i += 1
                elif character_file == "":
                    character_status = True
                else:
                    i += 1
            delimiter = ""
            join_str = delimiter.join(character_clean_file)
            clean_file.append(join_str)

        elif character_file == "":
            file_is_clean = True
            
        else:
            i += 1                
    file.close()

    return clean_file

def cleanFileToBaseRequired(clean_file, base_required):
    file_transformed = []
    for i in range (len(clean_file)):
        num_dec = toDecimal(clean_file[i])
        if base_required == 10:
            num = num_dec
        else:
            num = decimalToBinOctHex(num_dec,base_required)
        file_transformed.append(num)

    return file_transformed

def toDecimal(num):
    if num[0] == Binary_prefix:
        pot = 2
    elif num[0] == Octal_prefix:
        pot = 8
    elif num[0] == Decimal_prefix:
        pot = 10
    elif num[0] == Hex_prefix:
        pot = 16
        num = list(num)
        for i in range(len(num)):
            if num[i] in Hex_dic:
                num[i] = str(Hex_dic.get(num[i]))
        
    num_decimal = 0
    for i in range(len(num)-1):
        aux = int(num[i+1])
        i *= 1
        aux2 = aux * pot**(len(num)-2-i)
        num_decimal += aux2 
    
    return num_decimal

def decimalToBinOctHex(num, base_required):
    character_transformed = []

    finish = False
    while not finish:
        rest = num % base_required
        num = num // base_required
        
        if rest > 9:
            key = [k for k, v in Hex_dic.items() if v == rest]
            key = "".join(map(str, key))
            character_transformed.append(key)
        else:
            character_transformed.append(rest)

        if num == 0:
            finish = True
    character_transformed.reverse()

    character_transformed = "".join(map(str, character_transformed))

    return character_transformed
    


#main
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

#Leer el archivo e ignorar basura ; return lista de strings: ['*1001110', '&1112', '!75', '#110', '&143', '*1100001']
clean_file = readFileAndIgnoreTrash("prueba_6.txt") 

print(f"LISTA DE VALORES EXTRAÍDOS (Base {base}):\n--------------------------------------------------")

#Leer el archivo limpio y tranformar cada valor a su base requerida ; return lista de string transformados: 
transformed_file = cleanFileToBaseRequired(clean_file, base_required)

print("transformed_file", transformed_file)