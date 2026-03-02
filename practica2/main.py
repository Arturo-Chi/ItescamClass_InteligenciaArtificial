from percepcion import Percepcion
from regla import Regla
from accion import Accion
from motor_inferencia import Motor
from agente import Agente





r6 = Regla(
    nombre="Sin Presencia",
    condicion= lambda p: (not p.presencia and p.intensidadActual >0),
    accion= lambda p: Accion("Apagar", 5, 0)
)
r1 = Regla(
    nombre="luz alta + presencia + dia",
    condicion= lambda p: (p.luzNatural > 500 and p.presencia and p.horaTipo == "diurna"),
    accion= lambda p: Accion("Apagar", 0, 0)
)
r7 = Regla(
    nombre="Muy baja + presencia + nocturna",
    condicion= lambda p: (p.luzNatural < 50 and p.presencia and p.horaTipo == "nocturna" and p.intensidadActual < 100),
    accion= lambda p: Accion("Encender", 0, 100)
)
r2 = Regla(
    nombre="Media + diurna",
    condicion= lambda p: (200 <= p.luzNatural <= 500 and p.presencia and p.horaTipo == "diurna" and p.intensidadActual < 30),
    accion= lambda p: Accion("Ajustar", 0, 30)
)
r3 = Regla(
    nombre="Media + nocturna",
    condicion= lambda p: (200 <= p.luzNatural <= 500 and p.presencia and p.horaTipo == "nocturna" and p.intensidadActual < 50),
    accion= lambda p: Accion("Ajustar", 0, 50)
)
r4 = Regla(
    nombre="Baja + diurna",
    condicion= lambda p: (p.luzNatural < 200 and p.presencia and p.horaTipo == "diurna" and p.intensidadActual < 60),
    accion= lambda p: Accion("Ajustar", 0, 60)
)
r5 = Regla(
    nombre="Baja + nocturna",
    condicion= lambda p: (p.luzNatural < 200 and p.presencia and p.horaTipo == "nocturna" and p.intensidadActual < 80),
    accion= lambda p: Accion("Ajustar", 0, 80)
)

#6, 1, 7, 2, 3, 4, 5


try:
    

    percepcion = Percepcion(12, True, 12, "diurna")
    print(percepcion.esValida())

    agente = Agente()
    agente.motor.add_regla(r6)
    agente.motor.add_regla(r1)
    agente.motor.add_regla(r7)
    agente.motor.add_regla(r2)
    agente.motor.add_regla(r3)
    agente.motor.add_regla(r4)
    agente.motor.add_regla(r5)

    agente.decidir(percepcion)
    
    #(r7.ejecutar(percepcion))

    


except ValueError as e:
    print(e)

#print("La prueba", r7.evaluar(percepcion))
#
#
#print("Esta es la 3era prueba:")
#motor = Motor()
#motor.add_regla(r6)
#motor.add_regla(r1)
#motor.add_regla(r7)
#motor.add_regla(r2)
#motor.add_regla(r3)
#motor.add_regla(r4)
#motor.add_regla(r5)
#print(motor.evaluar(percepcion))
#
#
#
#print("Prueba con el agente")
#agente = Agente()
#agente.decidir(percepcion)
#