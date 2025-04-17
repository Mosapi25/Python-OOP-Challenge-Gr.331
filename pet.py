class Pet:
     def __init__(self, name):
         self.name = name
         self.hunger = 5
         self.energy = 5
         self.happiness = 5
         self.tricks = []
 
     def eat(self):
         old_hunger = self.hunger
         self.hunger = max(0, self.hunger - 3)
         self.happiness = min(10, self.happiness + 1)
         print(f"{self.name} ate some food. Hunger: {old_hunger} → {self.hunger}, Happiness: +1")
 
     def sleep(self):
         old_energy = self.energy
         self.energy = min(10, self.energy + 5)
         print(f"{self.name} took a nap. Energy: {old_energy} → {self.energy}")
 
     def play(self):
         if self.energy >= 2:
             self.energy -= 2
             self.happiness = min(10, self.happiness + 2)
             self.hunger = min(10, self.hunger + 1)
             print(f"{self.name} played! Energy -2, Happiness +2, Hunger +1")
         else:
             print(f"{self.name} is too tired to play! Let them rest.")
 
     def get_status(self):
         print(f"\n📋 {self.name}'s Status:")
         print(f"Hunger: {self.hunger}/10")
         print(f"Energy: {self.energy}/10")
         print(f"Happiness: {self.happiness}/10\n")
 
     def train(self, trick):
         if trick not in self.tricks:
             self.tricks.append(trick)
             self.happiness = min(10, self.happiness + 1)
             print(f"{self.name} learned a new trick: {trick}! 🎉 Happiness +1")
         else:
             print(f"{self.name} already knows how to {trick}!")
 
     def show_tricks(self):
         if self.tricks:
             print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
         else:
             print(f"{self.name} hasn't learned any tricks yet.")

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

