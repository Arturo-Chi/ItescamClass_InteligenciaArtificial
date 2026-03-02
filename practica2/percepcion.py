class Percepcion:

    luzNatural: int
    presencia: bool
    intensidadActual: int
    horaTipo: str


    def __init__(self, luz, presencia, intensidad, horaTipo: str):
        self.luzNatural = luz
        self.presencia = presencia
        self.intensidadActual = intensidad
        self.horaTipo = horaTipo.lower()

    def esValida(self)-> bool:
        try:
            self.validar()
            return True
        except:
            return False


    def validar(self) -> None:
        #Se manejan los casos negativos
        
        if self.luzNatural < 0 or not isinstance(self.luzNatural, int): 
            raise ValueError("El valor de lux no puede ser negativo")
          
        if (not isinstance(self.presencia, bool)) or (self.presencia not in (True, False)): 
            raise ValueError("El valor de presencia debe de ser boolean")
        
        if self.horaTipo.lower() not in ("diurna", "nocturna"): 
            raise ValueError("La hora debe ser 'diurna' o 'nocturna'")
        
        if self.intensidadActual < 0 or self.intensidadActual > 100: 
            raise ValueError("El valor de la intensidad debe estar entre 0 y 100%")
      
        if not isinstance(self.intensidadActual, int): 
            raise ValueError("El valor de la intensidad debe de ser numérico")
       


