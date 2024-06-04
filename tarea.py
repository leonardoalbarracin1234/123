class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad  # Agrega esta línea para asignar la edad

    def obtener_nombre(self):
        return self._nombre

persona1 = Persona("Juan", 30)
print(persona1.obtener_nombre())
print(persona1._edad)


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau guau"

class Gato(Animal):
    def sonido(self):
        return "Miau miau"

mi_perro = Perro("Firulais")
mi_gato = Gato("Pelusa")

print(mi_perro.nombre)  # Imprime "Firulais"
print(mi_perro.sonido())  # Imprime "Guau guau"
print(mi_gato.nombre)  # Imprime "Pelusa"
print(mi_gato.sonido())  # Imprime "Miau miau"



class Vehicle:
    def __init__(self, auto, toyota):
        self.auto = auto
        self.toyota = toyota

mi_carro = Vehicle("sedán", "Toyota Corolla")
mi_camion = Vehicle("camión", "Toyota Tacoma")

print(f"Auto: {mi_carro.auto}, Toyota: {mi_carro.toyota}")
print(f"Auto: {mi_camion.auto}, Toyota: {mi_camion.toyota}")



class Animal:
    def hablar(self):
        pass
#Por otro lado tenemos otras dos clases, Perro, Gato que heredan de la anterior. Además, implementan el método hablar() de una forma distinta.
class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")
#A continuación creamos un objeto de cada clase y llamamos al método hablar(). Podemos observar que cada animal se comporta de manera distinta al usar hablar().
for animal in Perro(), Gato():
    animal.hablar()
