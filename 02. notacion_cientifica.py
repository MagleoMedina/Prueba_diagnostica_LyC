import ast
import operator

# Definir operadores permitidos
operadores = {
    ast.Add: operator.add,  # Suma +
    ast.Sub: operator.sub,  # Resta - 
    ast.Mult: operator.mul, # Multiplicación *
    ast.Div: operator.truediv, # División /
    ast.Pow: operator.pow,  # Potencia **
    ast.USub: operator.neg  # Negación unaria -
}

def evaluar_expresion(expr):
    def _eval(node):
        # Si el nodo es un número, devolver su valor
        if isinstance(node, ast.Num):
            return node.n
        # Si el nodo es una operación binaria, evaluar recursivamente los operandos y aplicar el operador
        elif isinstance(node, ast.BinOp):
            return operadores[type(node.op)](_eval(node.left), _eval(node.right))
        # Si el nodo es una operación unaria, evaluar recursivamente el operando y aplicar el operador
        elif isinstance(node, ast.UnaryOp):
            return operadores[type(node.op)](_eval(node.operand))
        else:
            raise TypeError("Tipo de nodo no soportado")
    
    # Parsea la expresión en un árbol de sintaxis abstracta (AST)
    tree = ast.parse(expr, mode='eval')
    # Evaluar el cuerpo del árbol
    return _eval(tree.body)

# Ejemplo de uso
expresion_0 = "125e10-1e15"  # Definir una expresión en notación científica
expresion_1 = "5e-85*15"     # Definir otra expresión en notación científica
expresion_2 = "(125e10 - 1e15)/5e-85*15"  # Definir la expresion original quitar parentesis

# Evaluar las expresiones
resultado_0 = evaluar_expresion(expresion_0)
resultado_1 = evaluar_expresion(expresion_1)
resultado_2 = evaluar_expresion(expresion_2)

# Calcular el resultado de la división de los dos primeros resultados
result = resultado_0 / resultado_1

print("\n")
# Imprimir los resultados
print(f"El resultado 0 es = {resultado_0}") 
print(f"El resultado 1 es = {resultado_1}") 
print(f"El resultado de la division es = {result}") 
print(f"\nEl resultado 2 es = {resultado_2}\n") 