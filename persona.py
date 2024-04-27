
class Persona:

    def __init__(self, nombre: str = 'Melina', apellido: str = 'Gomez', du: int= 46161017):                # du= DNI
        self.__nombre__ = nombre                                                       # paso de parametro obligatorio a optativo cuando le pongo un valor por defecto
        self.__apellido__ = apellido
        self.__du__ = du 

    def __str__(self):
        return f'Mis datos son nombre = {self.__nombre__} \
              apellido = {self.__apellido__} \
              documento = {self.__du__}'

