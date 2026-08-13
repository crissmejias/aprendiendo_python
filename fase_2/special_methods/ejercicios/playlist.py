class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
    def __len__(self):
        return len(self.canciones)
    def agregar_cancion(self,cancion):
        self.canciones.append(cancion)
        print(f"Se ha agregado la canción {cancion}!")
    # Imprime la referencia del objeto
    def __repr__(self):
        return f"Playlist(nombre={self.nombre!r}, cantidad_canciones={len(self)!r})"
    # Validar si existe un elemento en la lista
    def __contains__(self, nombre):
        return nombre in self.canciones
    # Iterable, slicing y acceder a indices con []
    def __getitem__(self,index):
            return self.canciones[index]

        
# Pruebas
        
mi_playlist = Playlist("criss") # Crear playlist
# Agregar canciones
mi_playlist.agregar_cancion("u + me = <3") 
mi_playlist.agregar_cancion("the cure")
mi_playlist.agregar_cancion("maggots for brains")

print(mi_playlist) #Imprime el __repr__

print("my way" in mi_playlist) # Imprime False

print(mi_playlist[0:2]) #["u + me = <3, the cure]"
