class ViajeroFrecuente:
    __num_viajero = None
    __dni = None
    __nombre = None
    __apellido = None
    __millas_acum = None

    def __init__(self, numViajero = None, dni = None, nombre = None, apellido = None, millas = None):
        self.__num_viajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas

    def __str__(self):
        s = 'Numero Viajero: {}\nDNI: {}\nNombre: {}\nApellido: {}\nMillas Acumuladas: {}' .format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
        return s    

    def obtenerNumeroViajero(self):
        return self.__num_viajero    

    def obtenerDNI(self):
        return self.__dni

    def obtenerNombre(self):
        return self.__nombre

    def obtenerApellido(self):
        return self.__apellido    

    def obtenerMillas(self):
        return self.__millas_acum            

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def AcumularMillas(self,cantidadMillas):
        self.__millas_acum += cantidadMillas
        return self.__millas_acum

    def CanjearMillas(self,cantidadMillas):
        if self.__millas_acum >= cantidadMillas:
            self.__millas_acum -= cantidadMillas
            return self.__millas_acum
        else:
            print('ERROR: La cantidad de millas a canjear supera  la cantidad de millas acumuladas')    

   #Código requerido para el ejercicio 6

    def __gt__(self, otroViajero):
        if type(otroViajero) == ViajeroFrecuente:
            if self.__millas_acum > otroViajero.__millas_acum:
                return True
            else:
                return False

    def __add__(self, millas):
        if type(millas) == int:
            millas += self.__millas_acum
            nuevo_viajero = ViajeroFrecuente(self.obtenerNumeroViajero(), self.__dni, self.__nombre, self.__apellido, millas) 
            return nuevo_viajero   

    def __sub__(self, millas):
        if type(millas) == int:
            if millas <= self.__millas_acum:
                millas = self.__millas_acum - millas
                nuevo_viajero = ViajeroFrecuente(self.obtenerNumeroViajero(), self.__dni, self.__nombre, self.__apellido, millas) 
                return nuevo_viajero        
            else:
                print('ERROR: millas insuficientes!')    
                
    #Código requerido para el ejercicio 7             

    def __eq__(self, millas):
        if self.__millas_acum == millas:
            return True
        else:
            return False

    def __radd__(self, millas):
        if type(millas) == int:
            millas += self.__millas_acum
            nuevo_viajero = ViajeroFrecuente(self.obtenerNumeroViajero(), self.__dni, self.__nombre, self.__apellido, millas)
        return nuevo_viajero

    def __rsub__(self, millas):
        if type(millas) == int:
            if millas <= self.__millas_acum:
                millas = self.__millas_acum - millas
                nuevo_viajero = ViajeroFrecuente(self.obtenerNumeroViajero(),self.__dni, self.__nombre, self.__apellido, millas)
            else:
                print('ERROR: millas insuficientes!')    
        return nuevo_viajero