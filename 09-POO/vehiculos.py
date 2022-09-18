class vehiculos:
    def __init__(self, marca, modelo, numero_ruedas, color, estado):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
        self.color = color
        self.estado = estado
        self.numeracion = "vacio"
    

    def arrancar(self):
        self.estado="Arrancado"
    
    def parar(self):
        self.estado="Parado"
    
    def getInfo(self):
        info = "------Informacion del vehiculo--------"
        info += f"\nMarca: {self.marca}"
        info += f"\nModelo: {self.modelo}"
        info += f"\nNº Ruedas: {self.numero_ruedas}"
        info += f"\nColor: {self.color}"
        info += f"\nEstado: {self.estado}"
        info += f"\nNumeracion: {self.numeracion}"
        info += "\n--------------------------------------"
        return info

    def setInfo(self):
        self.marca = input("Marca: ")
        self.modelo = input("Modelo: ")
        self.numero_ruedas = input("Numero_ruedas: ")
        self.color = input("Color: ")
        self.estado = input("Estado: ")

class moto(vehiculos):
    def __init__(self):
        super().__init__()
        self.manillar = "15cm"
    
    def acelerar(self):
        return "Estoy acelerando"
    
    
    
        