class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else: 
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)
        
            

    # Función para mostrar personajes de planetas específicos
    def show_by_planet(self, planets):
        for character in self.__elements:
            if character['planet'] in planets:
                print(f"Nombre: {character['name']}, Planeta: {character['planet']}")

    # Función para mostrar planeta natal de ciertos personajes
    def show_planet_by_name(self, names):
        for character in self.__elements:
            if character['name'] in names:
                print(f"{character['name']} es de {character['planet']}")

    # Función para insertar antes de un personaje
    def insert_before(self, new_character, target_name):
        temp_queue = []
        inserted = False
        while len(self.__elements) > 0:
            character = self.attention()
            if character['name'] == target_name and not inserted:
                temp_queue.append(new_character)
                inserted = True
            temp_queue.append(character)
        
        self.__elements = temp_queue

    # Función para eliminar el personaje después de un personaje específico
    def remove_after(self, target_name):
        temp_queue = []
        found_target = False
        while len(self.__elements) > 0:
            character = self.attention()
            if found_target:
                found_target = False  # Se salta el siguiente personaje
            else:
                temp_queue.append(character)
            if character['name'] == target_name:
                found_target = True
        
        self.__elements = temp_queue

# Ejemplo de uso:
characters_queue = Queue()
characters_queue.arrive({'name': 'Luke Skywalker', 'planet': 'Tatooine'})
characters_queue.arrive({'name': 'Han Solo', 'planet': 'Corellia'})
characters_queue.arrive({'name': 'Leia Organa', 'planet': 'Alderaan'})
characters_queue.arrive({'name': 'Yoda', 'planet': 'Dagobah'})
characters_queue.arrive({'name': 'Jar Jar Binks', 'planet': 'Naboo'})
characters_queue.arrive({'name': 'Chewbacca', 'planet': 'Kashyyyk'})

# a. Mostrar personajes de Alderaan, Endor y Tatooine
print("Personajes de Alderaan, Endor, y Tatooine:")
characters_queue.show_by_planet(['Alderaan', 'Endor', 'Tatooine'])

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
print("\nPlaneta natal de Luke Skywalker y Han Solo:")
characters_queue.show_planet_by_name(['Luke Skywalker', 'Han Solo'])

# c. Insertar un nuevo personaje antes del maestro Yoda
characters_queue.insert_before({'name': 'Obi-Wan Kenobi', 'planet': 'Stewjon'}, 'Yoda')
print("\nDespués de insertar a Obi-Wan Kenobi antes de Yoda:")
characters_queue.show_planet_by_name(['Obi-Wan Kenobi', 'Yoda'])

# d. Eliminar el personaje después de Jar Jar Binks
characters_queue.remove_after('Jar Jar Binks')
print("\nDespués de eliminar al personaje ubicado después de Jar Jar Binks:")
characters_queue.show_planet_by_name(['Jar Jar Binks', 'Chewbacca'])  # Chewbacca debería haber sido eliminado
