from Arista import Arista
from Nodo import Nodo

class Grafo:
    def __init__(self):
        self.nodos = {}     # diccionario "HashTable"
        self.aristas = []   # lista

    def agregar_nodo(self, nodo):
        self.nodos[nodo.id] = nodo

    def agregar_arista(self, nodo_inicio, nodo_destino, peso):
        if nodo_inicio.id in self.nodos and nodo_destino.id in self.nodos:
            arista = Arista(nodo_inicio, nodo_destino, peso)
            self.aristas.append(arista)

    def mostrar_grafo(self):
        for arista in self.aristas:
            print(f"{arista}")

    def encontrar_camino(self, inicio_id, destino_id, camino_actual=None):
        if camino_actual is None:
            camino_actual = []  # lista
        inicio = self.nodos.get(inicio_id)
        destino = self.nodos.get(destino_id)
        if inicio is None or destino is None:
            print("\nADVERTENCIA: Nodo de inicio o destino no encontrado en el grafo.")
            return
        camino_actual = camino_actual + [inicio]
        if inicio == destino:
            self.mostrar_camino(camino_actual)
            return
        for arista in self.aristas:
            if arista.nodo_inicio == inicio and arista.nodo_destino not in camino_actual:
                self.encontrar_camino(arista.nodo_destino.id, destino_id, camino_actual[:])

    def mostrar_camino(self, camino):
        if camino:
            print("\nCAMINO ENCONTRADO:")
            costo_total = 0
            for i in range(len(camino) - 1):
                arista = self.buscar_arista(camino[i].id, camino[i + 1].id)
                print(f"{arista.nodo_inicio.nombre} -> {arista.nodo_destino.nombre} (Peso: {arista.peso})")
                costo_total += arista.peso
            print(f"Costo total del camino: [{costo_total} Km]\n")
            print('-'*20)

    def buscar_arista(self, inicio_id, destino_id):
        for arista in self.aristas:
            if arista.nodo_inicio.id == inicio_id and arista.nodo_destino.id == destino_id:
                return arista

    def menu(self):
        grafo = Grafo()

        nodo_a = Nodo("A", "Madrid", 40.16, 3.703)
        nodo_b = Nodo("B", "Guadalajara", 40.63, 3.163)
        nodo_c = Nodo("C", "Segovia", 40.94, 4.123)
        nodo_d = Nodo("D", "Avila", 40.65, 4.701)
        nodo_e = Nodo("E", "Toledo", 39.85, 4.024)

        grafo.agregar_nodo(nodo_a)
        grafo.agregar_nodo(nodo_b)
        grafo.agregar_nodo(nodo_c)
        grafo.agregar_nodo(nodo_d)
        grafo.agregar_nodo(nodo_e)

        grafo.agregar_arista(nodo_e, nodo_c, 159)
        grafo.agregar_arista(nodo_c, nodo_d, 64.3)
        grafo.agregar_arista(nodo_c, nodo_b, 153)
        grafo.agregar_arista(nodo_d, nodo_b, 171)
        grafo.agregar_arista(nodo_a, nodo_e, 72.5)
        grafo.agregar_arista(nodo_a, nodo_c, 91.6)
        grafo.agregar_arista(nodo_a, nodo_b, 66.5)
        grafo.agregar_arista(nodo_e, nodo_d, 169)  # Primer arista creada
        grafo.agregar_arista(nodo_d, nodo_e, 181)  # bucle de la primer arista
        grafo.agregar_arista(nodo_e, nodo_b, 98)  # Segunda arista creada
        grafo.agregar_arista(nodo_d, nodo_a, 200)  # Tercer arista creada
        grafo.agregar_arista(nodo_b, nodo_d, 167)  # Cuarta arista creada
        grafo.agregar_arista(nodo_b, nodo_a, 78)  # Quinta arista creada
        grafo.agregar_arista(nodo_c, nodo_a, 159)  # Sexta arista creada
        grafo.agregar_arista(nodo_a, nodo_d, 167)   # Séptima arista creada
        grafo.agregar_arista(nodo_d, nodo_a, 214)  # Octava arista creada
        grafo.agregar_arista(nodo_e, nodo_a, 57)  # Novena arista creada
        grafo.agregar_arista(nodo_b, nodo_c, 134)  # Décima arista creada
        grafo.agregar_arista(nodo_b, nodo_e, 177)  # Onceava arista creada
        grafo.agregar_arista(nodo_d, nodo_c, 71)  # Doceava arista creada
        grafo.agregar_arista(nodo_c, nodo_e, 148)  # Treceava arista creada

        print("\nIngrese los ID de las ciudades donde quiere su ruta \n")
        inicio_id = input("ID de ciudad de partida: ").upper()
        destino_id = input("ID de ciudad de destino: ").upper()

        while True:
            print()
            opc = int(
                input("Ingrese una opción: \n1.Dirigirse a la ciudad de destino\n2.Devolverse a la ciudad de inicio"
                      "\n3.Costo mínimo ida y vuelta \n4.Ingresar diferente ruta\n5.Ver el grafo\n6.Acabar el programa\n->"))

            if opc == 1:
                print("\nCaminos de ida: \n")
                grafo.encontrar_camino(inicio_id, destino_id)
            elif opc == 2:
                print("\nCaminos de vuelta: \n")
                grafo.encontrar_camino(destino_id, inicio_id)
            elif opc == 3:
                print("\nCaminos de ida y vuelta: \n")
                arista1 = grafo.buscar_arista(inicio_id, destino_id)
                arista2 = grafo.buscar_arista(destino_id, inicio_id)
                print(f"Costo de ida y vuelta mínimo: [{arista1.peso + arista2.peso} Km]\n")
            elif opc == 4:
                print("\nIngrese las nuevas ciudades:\n")
                inicio_id = input("ID de ciudad de partida: ").upper()
                destino_id = input("ID de ciudad de destino: ").upper()
            elif opc == 5:
                print("\nGrafo de rutas: \n")
                grafo.mostrar_grafo()
            elif opc == 6:
                print("¡HASTA LUEGO!")
                exit()