def main(archivo): #funcion principal del programa, el cual recibe un str(archivo) para ejecutarse.

    print("--- DECODIFICADOR DE MENSAJES ---\n")

    #acá dejamos elegir por teclado la base a la que se quiere transformar el mensaje secreto
    base_status = False
    while not base_status:
        base = input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16):")
        if base == ("2" or "8" or "10" or "16"):    
            base_status = True
            base = int(base)
        else:
            print("Porfavor, eliga una de las bases disponibles")

    







#main

main("archivo_1 copy (copy).txt")














