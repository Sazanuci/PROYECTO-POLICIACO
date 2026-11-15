from modelos import Placa, Policia, Detective

placa_juan = Placa("ABC123", "Patrullas")
placa_maria = Placa("XYZ789", "Homicidios")
placa_pedro = Placa("LMN456", "Cibercrimen")

p1 = Policia("Juan", 5, 30, placa_juan)
d1 = Detective("María", 8, 35, placa_maria, "Homicidios", 3)
d2 = Detective("Pedro", 15, 50, placa_pedro, "Cibercrimen", 10)

print(f"Edad de {d1.nombre}: {d1.get_edad()}")
d1.set_edad(-5)
d1.set_edad(40)

p1.Caso("Robo")
d1.Caso("Asesinato")
d1.resolver_misterio()

p1.CambioVehiculo("NEW999")

print(p1.describir())
print(d1.describir())
print(d2.describir())