class Profesor:                                
    def __init__(self, el_nombre, el_email):   
        self.__nombre__ = el_nombre                
        self.__email__ = el_email                  

    def dame_tu_nombre(self):
        return self.__nombre__                     
    
    def dame_tu_email(self):                   
        return self.__email__
    
class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
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
    
    def elegir_dieta(self, la_dieta):
        self.__dieta__ = la_dieta

    def es_vegano(self):
        self.__dieta__ = "Vegano"
        
    def mentoria(self, profesor):
        self.__mentor__ = profesor


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
