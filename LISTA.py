class lista:
    
    def __init__(self,nombre,contenido,instrucciones,num):
        self.nombre = nombre
        self.contenido = contenido
        self.instrucciones = instrucciones
        self.num = num
    
    #METODOS GETTER
    def getNombre(self):
        return self.nombre

    def getContenido(self):
        return self.contenido
    
    def getInstruccion(self):
        return self.instrucciones
    
    def getNum(self):
        return self.num
    
    #METODOS SETTER

    def setNombre(self,nombre):
        self.nombre = nombre

    def setContenido(self, contenido):
        self.contenido = contenido
    
    def setInstruccion(self, instrucciones):
        self.instrucciones = instrucciones

    def setNum(self,num):
        self.num = num

    def MOSTRARNOMBRES(self):
        for i in self.nombre:
            print(i)

    
    