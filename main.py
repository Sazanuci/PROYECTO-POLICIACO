"""
Sistema de Gestión Policial - Avance 2
Sistema que modela policías y detectives aplicando:
Encapsulamiento, Herencia, Polimorfismo y uso de Getters/Setters.
"""

#CREACION DE SUPERCLASE
class Policia:
    def __init__(self, nombre, placas, experiencia, edad):
        self.nombre = nombre
        self.disponibilidad = True
        self.placas = placas
        self.experiencia = experiencia
        #Atributo encapsulado
        self.__edad = edad

#GETTER Y SETTER PARA EL ATRIBUTO ENCAPSULADO

    def get_edad(self):
        #Getter
        return self.__edad

    def set_edad(self, nueva_edad):
        #SETTER. VALIDA EDAD ENTRE 18 Y 100
        if nueva_edad < 18 or nueva_edad > 100:
            print(f"Edad inválida: ({nueva_edad}). La edad debe estar entre 18 y 100.")
        else:
            self.__edad = nueva_edad
            print(f"Edad actualizada a {self.__edad} años.")

#METODOS BASE
    def Caso(self, caso):
        if(self.disponibilidad == True):
            self.disponibilidad = False
            print(f"El policia {self.nombre} ha tomado el caso {caso}")
            self.experiencia += 1
        else :
            self.disponibilidad = True
            print(f"El policia {self.nombre} esta libre")

    def CambioVehiculo(self, placas):
        self.placas = placas
        print(f"El policia {self.nombre} ha cambiado de placas a {self.placas}")

    def Penalizacion(self, Pena):
        self.experiencia -= Pena
        print(f"El policia {self.nombre} ha sido penalizado por {Pena} puntos")

    def CambioEdad(self):
        self.edad +=1
        print(f"El policia {self.nombre} cumple años y ahora tiene {self.edad}!!!")
        if(self.edad >= 65):
            print(f"El policia {self.nombre} se ha retirado")

    #NUEVO METODO. POLIMORFISMO

    def describir(self):
        return (f"Policía: {self.nombre} | Placas: {self.placas} | "
                f"Experiencia: {self.experiencia} | Edad: {self.get_edad()}")


class Detective(Policia):
    def __init__(self, nombre, placas, experiencia, edad, especialidad, casos_resueltos):
        #REUTILIZA INIT
        super().__init__(nombre, placas, experiencia, edad)
        #ATRIBUTOS NUEVOS DE LA CLASE HIJA
        self.especialidad = especialidad
        self.misterios_resueltos = casos_resueltos

    #METODO PROPIO
    def resolver_misterio(self):
        self.misterios_resueltos += 1
        self.experiencia += 2
        print(f"El detective {self.nombre} resolvió un misterio de "
              f"{self.especialidad}. Total resueltos: {self.misterios_resueltos}.")

    #POLIMORFISMO
    def describir(self):
        # Reutiliza el método del padre y lo extiende
        base = super().describir()
        return (f"{base} | Detective especialista en {self.especialidad} | "
                f"Misterios resueltos: {self.misterios_resueltos}")

#PRUEBAS
p1 = Policia("Juan", "ABC123", 5, 30)
d1 = Detective("María", "XYZ789", 8, 35, "Homicidios", 3)
d2 = Detective("Pedro", "LMN456", 15, 50, "Cibercrimen", 10)

#ENCAPSIULAMIENTO. GETTER Y SETTER
print(f"Edad de {d1.nombre}: {d1.get_edad()}")
#RECHAZA
d1.set_edad(-5)
#ACEPTA
d1.set_edad(40)

#POLIMORFISMO
p1.Caso("Robo")
d1.Caso("Asesinato")
d1.resolver_misterio()

#DESCRIPCIONES DE PADRE E HIJOS
print(p1.describir())
print(d1.describir())
print(d2.describir())
