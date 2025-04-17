from pet import Pet

my_pet = Pet("Buddy")

my_pet.get_status()
my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.train("Roll over")
my_pet.train("Sit")

my_pet.get_status()
my_pet.show_tricks()

from pet import Pet

def main():
    pet = Pet("Buddy")

    while True:
        print("\n--- What would you like to do? ---")
        print("1. Eat")
        print("2. Sleep")
        print("3. Play")
        print("4. Train")
        print("5. Show Tricks")
        print("6. Check Status")
        print("7. Take a Walk")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pet.eat()
            print("Nom nom! 🍖")
        elif choice == "2":
            pet.sleep()
            print("Zzz... 😴")
        elif choice == "3":
            pet.play()
            print("Yay! 🐾")
        elif choice == "4":
            trick = input("What trick should your pet learn? ")
            pet.train(trick)
            print(f"Learned {trick}!")
        elif choice == "5":
            tricks = pet.show_tricks()
            print("Tricks:", ", ".join(tricks) if tricks else "No tricks yet.")
        elif choice == "6":
            status = pet.get_status()
            print(f"Name: {status['name']}, Hunger: {status['hunger']}, Energy: {status['energy']}, Happiness: {status['happiness']}")
        elif choice == "7":
            pet.walk()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()

