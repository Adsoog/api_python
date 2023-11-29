class Michis:
    descuento_comida = 0.8
    all = []

    def __init__(self, nombre_michi: str, edad_michi: float, comida_michi=0):

        # corremos las validaciones de los argumentos
        assert comida_michi > - \
            1, f"La comida no puede ser menor a {comida_michi}"

        # Asignamos los valores de los objetos
        self.nombre_michi = nombre_michi
        self.edad_michi = edad_michi
        self.comida_michi = comida_michi

        # Acciones a ejecutar
        Michis.all.append(self)

    def total_comida_michi(self):
        return self.edad_michi * self.comida_michi

    def descuento_michi(self):
        return self.comida_michi * self.descuento_comida

    # repr stands for representing your objects
    def __repr__(self):  # mirar el otro metodo que seria __str__
        return f"Michis('{self.nombre_michi}','{self.edad_michi}''{self.comida_michi}')"


gato1 = Michis('Tribilla_mama', 7, 8)
gato2 = Michis("Gordilla", 7, 8)

print(Michis.all)

for michi in Michis.all:
    print(michi.nombre_michi)

# print(gato1.descuento_michi())
# print(gato1.total_comida_michi())
# gato2.descuento_comida = 0.7
# print(gato2.descuento_michi())
# print(gato2.total_comida_michi())
# print(Michis.__dict__)
# print(gato1.__dict__)


# Crear una clase que contenga 3 argumentos, 1 funccion init, 1 funcion de calculo,
# que se verifique el tipo de dato que tiene sera int str o double
# y usart assert para verificar que un valor sea correcto o entero
