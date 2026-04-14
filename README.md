# Laboratorio 1: Decodificador de Notas - Sistemas Digitales UFT

## 1. Integrantes
* **Nombre:** Alonso Olmedo - **RUT:** 21.771.481-8
* **Nombre:** Felipe Madariaga - **RUT:** 21.360.588-7

## 2. Especificación de los Algoritmos y Desarrollo Realizado
El decodificador fue desarrollado en Python 3.x utilizando un enfoque modular para separar la lógica de extracción, filtrado y conversión. El flujo del programa se divide en las siguientes etapas principales:

* **Lectura Segura (`read_file`):** Maneja la lectura del archivo de texto (`notas_dm.txt`) incorporando bloques `try-except` para evitar interrupciones abruptas si el archivo no se encuentra en el directorio de ejecución.
* **Extracción y Filtrado de Ruido (`exctract_valid_char`):** Actúa como una máquina de estados finitos. Recorre el flujo de texto buscando los prefijos válidos (`*`, `&`, `#`, `!`). Una vez identificado un prefijo, captura los caracteres subsecuentes validando que pertenezcan estrictamente al conjunto de caracteres de dicha base. Si el sistema detecta un carácter ajeno a la base (ruido), lo ignora de forma transparente sin alterar el estado del prefijo actual, continuando con la recolección de los dígitos válidos siguientes hasta toparse con un nuevo prefijo o el fin del archivo.
* **Filtrado ASCII (`filter_ascii_valid_range`):** Evalúa el valor decimal de cada bloque extraído. Si el valor escapa del rango imprimible estándar (32 a 126), es descartado para la construcción del mensaje final.
* **Conversión de Bases:**
  * **Hacia Decimal (`to_decimal`):** Algoritmo de conversión manual que itera sobre la cadena de caracteres de derecha a izquierda, multiplicando cada dígito por la base elevada a la potencia correspondiente a su posición (Como un polinómio característico).
  * **Desde Decimal (`dec_to_bin_oct_hex`):** Implementa el método de divisiones sucesivas. Se divide el número decimal por la base de destino iterativamente, almacenando los restos (mapeados a caracteres hexadecimales si es necesario) hasta que el cociente es cero.
* **Decodificación (`decode_ascii`):** Transforma el arreglo de valores decimales limpios a su representación en caracteres utilizando el estándar ASCII.

## 3. Supuestos Utilizados
Durante el desarrollo de esta solución se asumieron las siguientes consideraciones:

1. **Uso de funciones (int y chr):** De acuerdo con las aclaraciones entregadas por el ayudante del curso a través del canal oficial de Discord (9 de abril de 2026), se asume como válido el uso de la función `int(x)` estrictamente para la conversión de un string a tipo de dato entero, así como el uso de `chr()` para la conversión final a ASCII. Se respeta rigurosamente la prohibición de usar `int(x, base)` u otras funciones de conversión automática.
2. **Definición de "Ruido Místico" (Transparencia Estricta):** Se asume que los caracteres inválidos (ruido) incrustados dentro de una secuencia numérica son estrictamente transparentes. El programa no asume que el ruido actúa como delimitador de cierre. Por ejemplo, si el flujo presenta un prefijo decimal seguido de dígitos interrumpidos por una letra ajena a la base (ejemplo: #84a1), el algoritmo ignorará silenciosamente el carácter inválido (a) y continuará concatenando los dígitos válidos (8, 4, 1), procesando el valor final como 841 en base decimal. El cierre y evaluación de un valor numérico se produce única y exclusivamente cuando el sistema detecta un nuevo prefijo válido (*, &, #, !) o cuando se alcanza el final del archivo (EOF).
