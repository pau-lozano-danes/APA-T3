"""
Módulo algebra/vectores.py
Implementación de una clase Vector para operaciones de álgebra lineal.

Nombre del alumno: Pau Lozano Danes

Tests unitarios de la clase:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])
>>> v1 * v2
Vector([4, 10, 18])
>>> v1 @ v2
32
>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
"""

class Vector:
    """
    Representación de un vector euclidiano y sus operaciones fundamentales.
    """

    def __init__(self, componentes):
        """
        Instancia un nuevo objeto Vector.

        Parámetros:
            componentes (iterable): Una secuencia de números reales que definen el vector.
        """
        self.vector = list(componentes)

    def __repr__(self):
        """
        Genera la representación formal del objeto en cadena de texto.

        Retorno:
            str: Cadena con el formato 'Vector([x1, x2, ...])'.
        """
        return f"Vector({self.vector})"

    def __add__(self, otro):
        """
        Realiza la suma algebraica de dos vectores.

        Parámetros:
            otro (Vector): El vector que se desea sumar.
            
        Retorno:
            Vector: Una nueva instancia con la suma componente a componente.
        """
        return Vector(a + b for a, b in zip(self.vector, otro.vector))

    def __sub__(self, otro):
        """
        Realiza la resta algebraica de dos vectores.

        Parámetros:
            otro (Vector): El vector que se desea restar.
            
        Retorno:
            Vector: Una nueva instancia con la diferencia componente a componente.
        """
        return Vector(a - b for a, b in zip(self.vector, otro.vector))

    def __mul__(self, otro):
        """
        Implementa el producto por escalar y el producto de Hadamard (asterisco).

        Cometido:
            Si el operando es un número, escala el vector.
            Si el operando es otro Vector, multiplica elemento a elemento.

        Parámetros:
            otro (int, float, Vector): Escalar o vector para la operación.

        Retorno:
            Vector: Resultado de la multiplicación.
        """
        if isinstance(otro, (int, float)):
            return Vector(a * otro for a in self.vector)
        elif isinstance(otro, Vector):
            return Vector(a * b for a, b in zip(self.vector, otro.vector))
        return NotImplemented

    def __rmul__(self, otro):
        """
        Gestiona la multiplicación por escalar cuando este aparece a la izquierda.

        Parámetros:
            otro (int, float): Escalar que multiplica al vector.

        Retorno:
            Vector: El vector resultante escalado.
        """
        return self.__mul__(otro)

    def __matmul__(self, otro):
        """
        Calcula el producto escalar (dot product) usando el operador arroba (@).

        Parámetros:
            otro (Vector): El vector con el que se realiza el producto.

        Retorno:
            float/int: La suma de los productos de las componentes correspondientes.
        """
        return sum(a * b for a, b in zip(self.vector, otro.vector))

    def __floordiv__(self, otro):
        """
        Obtiene la componente paralela (tangencial) mediante el operador //.

        Cometido:
            Calcula la proyección del vector actual sobre la dirección de 'otro'.
            Fórmula: v_paralela = ((v1 · v2) / |v2|²) * v2

        Parámetros:
            otro (Vector): El vector de referencia para la dirección.

        Retorno:
            Vector: La componente tangencial de self respecto a otro.
        """
        # (self @ otro) es el producto escalar. 
        # (otro @ otro) equivale al cuadrado de la norma del vector.
        escalar_proyeccion = (self @ otro) / (otro @ otro)
        return escalar_proyeccion * otro

    def __mod__(self, otro):
        """
        Obtiene la componente perpendicular (normal) mediante el operador %.

        Cometido:
            Calcula el vector rechazo de self respecto a 'otro'.
            Fórmula: v_normal = v1 - v_paralela

        Parámetros:
            otro (Vector): El vector de referencia.

        Retorno:
            Vector: La componente normal de self respecto a otro.
        """
        # Se basa en la propiedad de descomposición: v1 = v_paralela + v_normal
        return self - (self // otro)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)