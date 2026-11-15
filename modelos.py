class Placa:
    def __init__(self, numero, departamento):
        self.numero = numero
        self.departamento = departamento

    def mostrar(self):
        return f"Placa {self.numero} - Depto. {self.departamento}"


class Policia:
    def __init__(self, nombre, experiencia, edad, placa_objeto):
        self.nombre = nombre
        self.disponibilidad = True
        self.experiencia = experiencia
        self.__edad = edad
        self.placa = placa_objeto

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if nueva_edad < 18 or nueva_edad > 100:
            print(f"Edad inválida: ({nueva_edad}). La edad debe estar entre 18 y 100.")
        else:
            self.__edad = nueva_edad
            print(f"Edad actualizada a {self.__edad} años.")

    def Caso(self, caso):
        if(self.disponibilidad == True):
            self.disponibilidad = False
            print(f"El policia {self.nombre} ha tomado el caso {caso}")
            self.experiencia += 1
        else :
            self.disponibilidad = True
            print(f"El policia {self.nombre} esta libre")

    def CambioVehiculo(self, placas):
        self.placa.numero = placas
        print(f"El policia {self.nombre} ha cambiado de placas a {self.placa.numero}")

    def Penalizacion(self, Pena):
        self.experiencia -= Pena
        print(f"El policia {self.nombre} ha sido penalizado por {Pena} puntos")

    def CambioEdad(self):
        self.set_edad(self.get_edad() + 1)
        print(f"El policia {self.nombre} cumple años y ahora tiene {self.get_edad()}!!!")
        if(self.get_edad() >= 65):
            print(f"El policia {self.nombre} se ha retirado")

    def describir(self):
        return (f"Policía: {self.nombre} | {self.placa.mostrar()} | "
                f"Experiencia: {self.experiencia} | Edad: {self.get_edad()}")


class Detective(Policia):
    def __init__(self, nombre, experiencia, edad, placa_objeto, especialidad, casos_resueltos):
        super().__init__(nombre, experiencia, edad, placa_objeto)
        self.especialidad = especialidad
        self.misterios_resueltos = casos_resueltos

    def resolver_misterio(self):
        self.misterios_resueltos += 1
        self.experiencia += 2
        print(f"El detective {self.nombre} resolvió un misterio de "
              f"{self.especialidad}. Total resueltos: {self.misterios_resueltos}.")

    def describir(self):
        base = super().describir()
        return (f"{base} | Detective especialista en {self.especialidad} | "
                f"Misterios resueltos: {self.misterios_resueltos}")