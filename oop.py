class Profesor:                                
    def __init__(self, __nombre__, __email__):   
        self.__nombre__ = __nombre__          
        self.__email__ = __email__                  

    def dame_tu_nombre(self):
        return self.__nombre__                     
    
    def dame_tu_email(self):                   
        return self.__email__
    
class Alumno:
    def __init__(self, __nombre_del_alumno__):
        self.__nombre__ = __nombre_del_alumno__
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None                     

    def falta(self):
        self.__inasistencias__ += 1

    def esta_libre(self):
        if self.__inasistencias__ >= 5:
            return "Esta libre"
        else:
            return "OK"
    
    def elegir_dieta(self, __la_dieta__):
        self.__dieta__ = __la_dieta__

    def es_vegano(self):
        self.__dieta__ = "Vegano"
        
    def mentoria(self, __profesor__):
        self.__mentor__ = __profesor__


profe_elio = Profesor("Elio", "elio@gmail.com")            
profe_gabi = Profesor("Gabriel", "gabriel@gmail.com")      

print(profe_elio.dame_tu_nombre())                        
print(profe_gabi.dame_tu_nombre())

print(profe_elio.dame_tu_email())
print(profe_gabi.dame_tu_email())

                                                    
alumno_juan = Alumno("Juancito")
alumno_maria = Alumno("Maria")

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()                                      
alumno_juan.falta()
print(alumno_juan.esta_libre())

alumno_juan.falta()
print(alumno_juan.esta_libre())


alumno_maria.elegir_dieta("Vegetariana")
print(alumno_maria.__dieta__)

alumno_juan.es_vegano()
print(alumno_juan.__dieta__)

alumno_juan.mentoria(profe_elio)
print(alumno_juan.__mentor__.__nombre__)                         
alumno_maria.mentoria(profe_gabi)
print(alumno_maria.__mentor__.__nombre__) 
