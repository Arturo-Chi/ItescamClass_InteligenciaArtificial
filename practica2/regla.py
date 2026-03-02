from typing import Callable
from accion import Accion
from percepcion import Percepcion
class Regla:
    nombre: str
    condicion: Callable[[Percepcion], bool]
    accion: Callable[[Percepcion], Accion]

    def __init__(self, nombre, condicion, accion):
        self.nombre = nombre
        self.condicion = condicion
        self.accion = accion



    def evaluar(self, p:Percepcion) -> bool:
        #if not p.esValida():
        #    raise ValueError("La percepción tiene datos inválidos")
        p.validar()
        return bool(self.condicion(p))

    

    def ejecutar(self, p:Percepcion) -> Accion:
        #if not p.esValida:
        #     raise ValueError("La percepción no es válida")
        p.validar()
        return self.accion(p)
