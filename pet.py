class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        return self.tricks

    def get_status(self):
        return {
            "name": self.name,
            "hunger": self.hunger,
            "energy": self.energy,
            "happiness": self.happiness
        }

    def walk(self):
        if self.energy >= 2:
            self.energy -= 2
            self.hunger = min(10, self.hunger + 2)
            self.happiness = min(10, self.happiness + 3)
            print(f"{self.name} went for a walk! 🐕 Happiness +3, Energy -2, Hunger +2")
        else:
            print(f"{self.name} is too tired to go for a walk.")
