import csv
from claseViajero import ViajeroFrecuente

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregarViajero(self, unViajero):
        if type(unViajero) == ViajeroFrecuente:
            self.__lista.append(unViajero)    

    def crearInstancias(self):
        band = True
        archivo = open('ViajerosFrecuentes.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            if band:
                band = False
            else:
                unViajero = ViajeroFrecuente(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]))
                self.agregarViajero(unViajero)
        archivo.close() 

    def __str__(self):

        s = ''
        for viajero in self.__lista:
            s += str(viajero) + '\n\n'
        return s       

    def obtenerMaximo(self):
        maximo = -9999
        viajero = None
        for i in range(len(self.__lista)):
            if self.__lista[i] > maximo:
                maximo = self.__lista[i].obtenerMillas()
        return maximo     

    
    def buscarViajero(self, numero):
        encontro = False
        for i in range(len(self.__lista)):
            if self.__lista[i].obtenerNumeroViajero() == numero:
                return self.__lista[i]
                break
