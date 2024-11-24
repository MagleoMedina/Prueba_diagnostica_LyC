import re

from collections import Counter

def contar_palabras_reservadas(cadena, keywords):
    # Utiliza una expresión regular para encontrar todas las palabras en la cadena
    palabras = re.findall(r'\b\w+\b', cadena)
    # Cuenta la frecuencia de cada palabra encontrada
    contador = Counter(palabras)
    #Se define un conjunto vacio
    resumen = {}
    total = 0

    # Itera sobre cada palabra reservada para contar su ocurrencia en el código
    for palabra in keywords:
        # Obtiene la cantidad de veces que la palabra reservada aparece en el código
        cantidad = contador.get(palabra, 0)
        # Almacena la cantidad en el diccionario resumen
        resumen[palabra] = cantidad
        # Suma la cantidad al total de palabras reservadas encontradas
        total += cantidad
    
    # Imprime el total de palabras reservadas encontradas
    print(f"Total de palabras reservadas encontradas: {total}")

    # Imprime la cantidad de cada palabra reservada encontrada
    for palabra, cantidad in resumen.items():
        print(f"'{palabra}': {cantidad}")

# Ejemplo de uso
codigo = """
public class Main {
    public static void main(String[] args) {
        
        int a = 1;
        int b = 2;
        int resultado = a + b;
        System.out.println(resultado);
        
        saludar("¡Hola, mundo!");
        
    }

    public static void saludar(String texto) {
        System.out.println(texto);
        
    }
}
"""

# Lista de palabras reservadas a buscar en el código
palabras_reservadas = ['public', 'class', 'static', 'void', 'int', 'return',
                        'if', 'else', 'for', 'while', 'System', 'out', 'println','String'] #agg 

# Llama a la función para contar las palabras reservadas en el código
contar_palabras_reservadas(codigo, palabras_reservadas)