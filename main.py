from claseViajero import ViajeroFrecuente
from claseManejador import Manejador

def test():
    print('Iniciando test...')
    viajero1 = ViajeroFrecuente(1,'44127975','Santiago','Jofre', 1500)
    otro_viajero = ViajeroFrecuente(2,'43212121','Geronimo','Lopez',1000)
    print(' === ANTES DE SUMAR MILLAS ===')
    print(viajero1)
    viajero1 = viajero1 + 1000
    print(' === DESPUES DE SUMAR MILLAS ===')
    print(viajero1)
    viajero1 = viajero1 - 500
    print(' === DESPUES DE CANJEAR 500 MILLAS ===')
    print(viajero1)
    if viajero1 == otro_viajero:
        print('Iguales')
    else:
        print('Distintos')
    print('Cerrando test...\n\n')



if __name__ == '__main__':
    test()
    lista = Manejador()
    lista.crearInstancias()
    print(lista)
    numero = int(input('Ingrese el numero de viajero: '))
    viajero = lista.buscarViajero(numero)
    numero2 = int(input('Ingrese el numero de otro viajero: '))
    otro_viajero = lista.buscarViajero(numero2)
    if type(viajero) == ViajeroFrecuente and type(otro_viajero) == ViajeroFrecuente:
        if viajero > otro_viajero:
            print('El viajero con mayor cantidad de millas es: {}' . format(viajero.obtenerNombre()))
        else:
            print('El viajero con mayor cantidad de millas es: {}' . format(otro_viajero.obtenerNombre()))
        millas_acumular = int(input('Ingrese la cantidad de millas a acumular: '))
        viajero += millas_acumular
        print('=== Millas acumuladas ===')
        print(viajero) 
        print('\n=== Millas canjeadas ===')
        millas_canjear = int(input('Ingrese la cantidad de millas a canjear: '))
        viajero -= millas_canjear
        print(viajero)
        print('\n=== Comparar millas ===')
        millas_comparar = int(input('Ingrese la cantidad de millas a comparar: '))
        if viajero == millas_comparar:
            print('La cantidad de millas ingresadas coincide con la cantidad de millas del Viajero: {}'. format(viajero.obtenerNombre()))
        else:
            print('La cantidad de millas ingresadas no coincide con la del viajero!')
        print(' === Sobrecarga por derecha (suma) ===')
        viajero = millas_acumular + viajero
        print(viajero)
        print('\n\n')
        print(' === Sobrecarga por derecha (resta) ===')
        viajero = millas_canjear - viajero
        print(viajero)
    else:
        print('ERROR: Viajero/s no encontrado/s')