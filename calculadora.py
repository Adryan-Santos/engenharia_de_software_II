import math

class Calculadora:
    
    def soma(self, a, b):
        return round (a + b, 2)
    
    def subtrai(self, a,b):
        return a - b
    
    def multiplica(self, a,b):
        return a * b
    
    def divide(self, a,b):
        if b == 0:
            raise ValueError("Não é permitida divisão por zero")
        return a / b
    
    def potencia(self, a, b):
        return a ** b
    
    def raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Não é possível calcular raiz de número negativo")
        return math.sqrt(a)