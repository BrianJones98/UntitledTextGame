#Species

sentient_list = ["Human", "Shade", "Golem"]

class Sentient:
    def __init__(self, species, level):
        self.name = "default"
        self.level = level

        upper_species = species.upper()

        if upper_species in sentient_list:
            self.species = upper_species
        else:
            self.species = "Human"

        #Attributes
        self.strength = 10
        self.perception = 10
        self.intelligence = 10
        self.dexterity = 10
        self.endurance = 10
        self.resolve = 10
        self.speech = 10

        #Stats
        self.health = self.endurance + self.strength/2
        self.mana = self.resolve + self.endurance/2
        self.stamina = (self.strength + self.endurance + self.dexterity)/3

        self.armor = 0
        self.speed = (self.dexterity + self.strength)/2
        self.evade = (self.dexterity + self.perception + self.speed)/3.5

        #Species Modifications
        if self.species == "Golem":
            self.armor += 5

#Primary Classes

class Warrior(Sentient):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.strength += 10
        self.endurance += 10

        self.health += 5
        self.mana -= 10
        self.stamina += 5

class Assassin(Sentient):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.dexterity += 10
        self.perception += 5

        self.health += 5
        self.mana -= 10
        self.stamina += 5

class Sorcerer(Sentient):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.resolve += 10
        self.perception += 5
        self.intelligence += 5

        self.health -= 5
        self.mana += 10
        self.stamina -= 5

#Specialized Classes