from claseFacu import Facultad
from claseCarrera import Carrera
import csv

class ManejadorFacultades:
    def __init__(self):
        self.__listaFacu = []
    
    def agrega(self, nuevo):
        self.__listaFacu.append(nuevo)
        
    def getLista(self):
        return self.__listaFacu
    
    def carga(self):
        archivo = open('carreras.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if  (fila[1] == 'Facultad de Ingenieria' or fila[1] == 'Facultad de Ciencias Exactas Fisicas y Naturales' or fila[1] == 'Facultad de Ciencias Sociales'):
                nuevaFacu = Facultad(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                self.agrega(nuevaFacu)
            
    def opcion1(self, cod):
        centinela = True
        i = 0
        while i < len(self.getLista()) and centinela:
            if cod == self.getLista()[i].getCodigo():
                print(f"Nombre Facultad:{self.getLista()[i].getNombre()}")
                self.getLista()[i].imprimirCarreras()
                centinela = False
            i+=1
        if centinela:
            print("No se encontro una facultad con ese numero de codigo... ")
    
    def opcion2(self, nom):
        i = 0
        centinela = True
        while i < len(self.getLista()) and centinela:
            centinela = self.getLista()[i].buscarEImprimirCarrera(nom)
            i+=1
        if centinela:
            print("No se encontro la carrera buscada...")
    