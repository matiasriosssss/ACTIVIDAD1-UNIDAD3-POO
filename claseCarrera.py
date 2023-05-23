class Carrera:
    def __init__ (self, codigoF, codigoC, nombre, titulo, duracion, tipo):
        self.__codigo = codigoF + "," + codigoC
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__tipo = tipo
        
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    
    
    
    