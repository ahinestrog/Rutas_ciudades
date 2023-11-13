class Nodo:
    def __init__(self, id, nombre, latitud, longitud):
        self.id = id
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        return f'[({self.id}) {self.nombre} | lon:{self.longitud} lat:{self.latitud})\t]'