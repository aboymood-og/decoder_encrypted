#global variables

Valid_characters = ["*", "&", "#", "!", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

Binary_prefix = "*"
Binary_base = ["0","1"]

Octal_prefix = "&"
Octal_base = ["0","1","2","3","4","5","6","7"]

Decimal_prefix = "#"
Decimal_base = ["0","1","2","3","4","5","6","7","8","9"]

Hex_prefix = "!"
Hex_base = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

Valid_prefix = [Binary_prefix, Octal_prefix, Decimal_prefix, Hex_prefix]



def readFileAndIgnoreTrash(path_file): #RECORDATORIO; ACA VEO RECURSIVIDAD PERO NO RECUERDO COMO TRABAJAR CON ELLA AAJAJAJAJAJAJJJ, en un futuro vere si lo optimizo
    
    print(f"\n[+] Procesando archivo: {path_file}")

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
            clean_file.append(character_clean_file)

        elif character_file == "":
            file_is_clean = True
            
        else:
            i += 1                
    file.close()

    return clean_file





#main
print("--- DECODIFICADOR DE MENSAJES ---\n")

#Elegir por teclado la base a la que se quiere transformar el mensaje encripado
base_status = False
while not base_status:
    base = input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16):")
    if base in ("2", "8", "10", "16"):    
        base_status = True
        base = int(base)
    else:
        print("Porfavor, eliga una de las bases disponibles")

#Leer el archivo e ignorar basura
clean_file = readFileAndIgnoreTrash("prueba_6.txt")