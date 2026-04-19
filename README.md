# Laboratorio 1: Decodificador de Notas - Sistemas Digitales UFT

## 1. Integrantes
* **Nombre:** Alonso Olmedo - **RUT:** 21.771.481-8
* **Nombre:** Felipe Madariaga - **RUT:** 21.360.588-7

## 2. Especificación de los Algoritmos y Desarrollo Realizado
El decodificador fue desarrollado en Python 3.x utilizando un enfoque modular para separar la lógica de extracción, filtrado y conversión. El flujo del programa se divide en las siguientes etapas principales:

* **Lectura Segura (`read_file`):** Maneja la lectura del archivo de texto (Ejemplo: `notas_dm.txt`) incorporando bloques `try-except` para evitar interrupciones abruptas si el archivo no se encuentra en el directorio de ejecución.

* **Extracción y Filtrado de Ruido (`exctract_valid_char`):** Actúa como una máquina de estados finitos. Recorre el flujo de texto buscando los prefijos válidos (`*`, `&`, `#`, `!`). Una vez identificado un prefijo, captura los caracteres siguientes validando que pertenezcan estrictamente al conjunto de caracteres de dicha base. Para el caso hexadecimal, el algoritmo normaliza la entrada convirtiéndola a mayúsculas (`.upper()`), volviéndolo tolerante a variaciones de formato (*case-insensitive*). Si el sistema detecta un carácter ajeno a la base (ruido), lo ignora de forma transparente sin alterar el estado del prefijo actual, continuando con la recolección de los dígitos válidos siguientes hasta toparse con un nuevo prefijo o el fin del archivo.
* **Filtrado ASCII (`filter_ascii_valid_range`):** Evalúa el valor decimal de cada bloque extraído. Si el valor escapa del rango imprimible estándar (32 a 126), es descartado para la construcción del mensaje final.
* **Conversión de Bases:**
  * **Hacia Decimal (`to_decimal`):** Algoritmo de conversión manual que itera sobre la cadena de caracteres de derecha a izquierda, multiplicando cada dígito por la base elevada a la potencia correspondiente a su posición (Como un polinómio característico).
  * **Desde Decimal a Binario u Octal o Hexadecimal(`dec_to_bin_oct_hex`):** Implementa el método de divisiones sucesivas. Se divide el número decimal por la base de destino iterativamente, almacenando los restos (mapeados a caracteres hexadecimales si es necesario) hasta que el cociente es cero.
* **Decodificación (`decode_ascii`):** Transforma el arreglo de valores decimales limpios a su representación en caracteres utilizando el estándar ASCII.

## 3. Supuestos Utilizados
Durante el desarrollo de esta solución se asumieron las siguientes consideraciones:

1. **Uso de funciones (int y chr):** De acuerdo con las aclaraciones entregadas por el ayudante del curso a través de Discord (9 de abril de 2026), se asume como válido el uso de la función `int(x)` estrictamente para la conversión de un string a tipo de dato entero, así como el uso de `chr()` para la conversión final a ASCII. Se respeta rigurosamente la prohibición de usar `int(x, base)` u otras funciones de conversión automática.
2. **Definición de "Ruido Místico" (Transparencia Estricta):** Se asume que los caracteres inválidos (ruido) incrustados dentro de una secuencia numérica son estrictamente transparentes. El programa no asume que el ruido actúa como delimitador de cierre. Por ejemplo, si el flujo presenta un prefijo decimal seguido de dígitos interrumpidos por una letra ajena a la base (ejemplo: `#84a1`), el algoritmo ignorará silenciosamente el carácter inválido (`a`) y continuará concatenando los dígitos válidos (`8`, `4`, `1`), procesando el valor final como `841` en base decimal. El cierre y evaluación de un valor numérico se produce única y exclusivamente cuando el sistema detecta un nuevo prefijo válido (`*`, `&`, `#`, `!`) o cuando se alcanza el final del archivo (EOF).
3. **Flexibilidad del Formato Hexadecimal (Case-Insensitive):** Se asume que el archivo de texto a procesar puede contener caracteres hexadecimales escritos mezclando mayúsculas y minúsculas. El sistema asume que la capitalización no define la validez del carácter. Por ejemplo, se considera que un bloque como `!6f` debe ser tratado exactamente igual que `!6F` (resultando en el valor decimal `111`, correspondiente a la letra `o` en ASCII). Si el programa fuera estrictamente sensible a mayúsculas, la letra `f` minúscula habría sido tratada como "ruido místico" e ignorada, dejando un valor aislado de `6` (hexadecimal), el cual habría sido posteriormente descartado por el filtro ASCII al estar fuera del rango imprimible.

## 4. Ejemplo de Ejecución y Filtrado

Para ilustrar el comportamiento de los algoritmos de extracción y filtrado (específicamente la transparencia del ruido, la validación ASCII y la flexibilidad de mayúsculas/minúsculas), supongamos que tenemos un archivo `ejemplo.txt` que contiene la siguiente cadena de texto:

**Archivo de entrada (`ejemplo.txt`):**
`*010x01y000!6f@&15z49#9w7#200`

**Proceso de decodificación paso a paso:**

1. **`*010x01y000` (Binario a ASCII 'H'):**
   * El sistema detecta el prefijo binario `*`.
   * Ignora silenciosamente las letras minúsculas `x` e `y` (ruido místico).
   * Concatena los dígitos válidos: `01001000` (Base 2).
   * Al convertir a decimal resulta en `72`, el cual está en el rango válido y corresponde al carácter **'H'**.

2. **`!6f@` (Hexadecimal a ASCII 'o'):**
   * El sistema detecta el prefijo hexadecimal `!`.
   * Procesa la `f` minúscula convirtiéndola a mayúscula (`F`), validándola correctamente y evitando que sea considerada ruido. Ignora el símbolo `@`.
   * Concatena los dígitos válidos: `6F` (Base 16).
   * Al convertir a decimal resulta en `111`, correspondiente al carácter **'o'**.

3. **`&15z49` (Octal a ASCII 'l'):**
   * El sistema detecta el prefijo octal `&`, cerrando el bloque anterior.
   * Ignora la letra `z` y el numero '9' ya que esta fuera del rango de su base.
   * Concatena los dígitos válidos: `154` (Base 8).
   * Al convertir a decimal resulta en `108`, correspondiente al carácter **'l'**.

4. **`#9w7` (Decimal a ASCII 'a'):**
   * Detecta el prefijo decimal `#`.
   * Ignora la letra `w`.
   * Concatena los dígitos válidos: `97` (Base 10).
   * El decimal `97` es válido y corresponde al carácter **'a'**.

5. **`#200` (Filtro de Rango ASCII):**
   * Detecta el prefijo decimal `#`.
   * El valor decimal resultante es `200`.
   * Como `200` escapa del rango imprimible estándar (32 a 126), la función `filter_ascii_valid_range` lo descarta por completo y no se incluye en el mensaje final.

**Mensaje Decodificado Final:**
```text
Hola