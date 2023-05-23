from claseCarrera import Carrera
import csv
class Facultad:
    def __init__ (self, codigo, nombre, direccion, localidad, provincia, telefono):
        self.__codigo = int(codigo)
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__provincia = provincia
        self.__telefono = telefono
        self.__listaCarreras = []
        archivo = open('carreras.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if self.__codigo == int(fila[0]) and fila[1] != "Facultad de Ingenieria" and fila[1] != "Facultad de Ciencias Exactas Fisicas y Naturales" and fila[1] != "Facultad de Ciencias Sociales":
                nuevoObjeto = Carrera(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                self.agregaCarrera(nuevoObjeto)
    
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion + " " + self.__localidad + " " + self.__provincia + " " 
    def getListaCarreras(self):
        return self.__listaCarreras
    def agregaCarrera(self, nuevo):
        self.getListaCarreras().append(nuevo)
    def imprimirCarreras(self):
        for i in range(len(self.getListaCarreras())):
            print(f"Carrera: {self.getListaCarreras()[i].getNombre()} - Duracion: {self.getListaCarreras()[i].getDuracion()}")
    def buscarEImprimirCarrera(self, nom):
        i = 0
        centinela = True
        while i < len(self.getListaCarreras()) and centinela:
            if nom == self.getListaCarreras()[i].getNombre():
                centinela = False
                print(f"Codigo: {self.getListaCarreras()[i].getCodigo()} - Nombre Facultad: {self.getNombre()} - Localidad: {self.getDireccion()}")
            i+=1
        return centinela
    