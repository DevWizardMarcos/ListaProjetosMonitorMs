import random

class Character:
    def __init__(self, name, character_class, attributes):
        self.name = name
        self.character_class = character_class
        self.attributes = attributes

    def __str__(self):
        return f"Nome: {self.name}, Classe: {self.character_class}, Atributos: {self.attributes}"

def generate_random_name():
    names = ["Aragorn", "Legolas", "Gimli", "Frodo", "Samwise", "Gandalf"]
    return random.choice(names)

def generate_random_class():
    classes = ["Guerreiro", "Mago", "Ladrão", "Clérigo"]
    return random.choice(classes)

def generate_random_attributes():
    return {
        "Força": random.randint(1, 20),
        "Inteligência": random.randint(1, 20),
        "Destreza": random.randint(1, 20)
    }

def create_character():
    name = generate_random_name()
    character_class = generate_random_class()
    attributes = generate_random_attributes()
    return Character(name, character_class, attributes)

def main():
    print("Gerador de Fichas de RPG")
    option = input("Deseja gerar um personagem aleatório? (s/n): ")
    
    if option.lower() == 's':
        character = create_character()
        print(character)
    else:
        print("Operação cancelada.")

if __name__ == "__main__":
    main()