import re

# Definir la función enum_numeros_reales que recibe una cadena de texto y retorna la cantidad de números reales que cumplan con las siguientes condiciones:
def enum_numeros_reales(cadena):
    # Definir el patrón de expresión regular para encontrar números reales en el formato a.bbbb
    patron = r'\b([0-9][0-9]{0,2})\.(\d{4})\b'
    
    # Buscar todas las coincidencias del patrón en la cadena
    coincidencias = re.findall(patron, cadena)
    
    # Inicializar el contador de números reales válidos
    contador = 0
    
    # Iterar sobre todas las coincidencias encontradas
    for i, j in coincidencias:
        # Verificar que la parte entera esté entre 1 y 999 y que cada dígito de la parte decimal esté entre 0 y 9
        if 1 <= int(i) <= 999 and all(0 <= int(digit) <= 9 for digit in j):
            # Incrementar el contador si la coincidencia es válida
            contador += 1
    
    # Retornar el número total de coincidencias válidas
    return contador

# Ejemplo de uso de la función con una cadena de prueba patron a.bbbb
cadena = "999.1234, 00.9999, 0000.0000, 32.1234, 0.4567"

print(enum_numeros_reales(cadena))