class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5         # 0 = full, 10 = very hungry
        self.energy = 5         # 0 = tired, 10 = fully rested
        self.happiness = 5      # scale of 0–10
        self.tricks = []        # bonus: list of tricks

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
            print(f"{self.name} played happily! Energy: -2, Happiness: +2, Hunger: +1")
        else:
            print(f"{self.name} is too tired to play!")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print("-------------------------")


# Example usage:
my_pet = Pet("Pookie")
my_pet.get_status()
my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.train("Jump over a log")
my_pet.train("turn")
my_pet.show_tricks()
my_pet.get_status()
