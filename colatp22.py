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

    # a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
    def find_by_superhero_name(self, superhero_name):
        for character in self.__elements:
            if character['superhero'] == superhero_name:
                print(f"El personaje de {superhero_name} es {character['name']}")
                return
        print(f"No se encontró el superhéroe {superhero_name}")

    # b. Mostrar los nombres de los superhéroes femeninos
    def show_female_superheroes(self):
        print("Superhéroes femeninos:")
        for character in self.__elements:
            if character['gender'] == 'F':
                print(character['superhero'])

    # c. Mostrar los nombres de los personajes masculinos
    def show_male_characters(self):
        print("Personajes masculinos:")
        for character in self.__elements:
            if character['gender'] == 'M':
                print(character['name'])

    # d. Determinar el nombre del superhéroe del personaje Scott Lang
    def find_superhero_by_character(self, character_name):
        for character in self.__elements:
            if character['name'] == character_name:
                print(f"El superhéroe de {character_name} es {character['superhero']}")
                return
        print(f"No se encontró el personaje {character_name}")

    # e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con 'S'
    def show_data_by_initial(self, initial):
        print(f"Personajes o superhéroes cuyos nombres comienzan con '{initial}':")
        for character in self.__elements:
            if character['name'].startswith(initial) or character['superhero'].startswith(initial):
                print(character)

    # f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
    def find_carol_danvers(self):
        for character in self.__elements:
            if character['name'] == 'Carol Danvers':
                print(f"Carol Danvers es {character['superhero']}")
                return
        print("Carol Danvers no se encuentra en la cola")

# Ejemplo de uso:
mcu_queue = Queue()
mcu_queue.arrive({'name': 'Tony Stark', 'superhero': 'Iron Man', 'gender': 'M'})
mcu_queue.arrive({'name': 'Steve Rogers', 'superhero': 'Capitán América', 'gender': 'M'})
mcu_queue.arrive({'name': 'Natasha Romanoff', 'superhero': 'Black Widow', 'gender': 'F'})
mcu_queue.arrive({'name': 'Carol Danvers', 'superhero': 'Capitana Marvel', 'gender': 'F'})
mcu_queue.arrive({'name': 'Scott Lang', 'superhero': 'Ant-Man', 'gender': 'M'})

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
mcu_queue.find_by_superhero_name('Capitana Marvel')

# b. Mostrar los nombres de los superhéroes femeninos
mcu_queue.show_female_superheroes()

# c. Mostrar los nombres de los personajes masculinos
mcu_queue.show_male_characters()

# d. Determinar el nombre del superhéroe del personaje Scott Lang
mcu_queue.find_superhero_by_character('Scott Lang')

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con 'S'
mcu_queue.show_data_by_initial('S')

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
mcu_queue.find_carol_danvers()
