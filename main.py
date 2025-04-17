from pet import Pet

def main():
    pet = Pet("Pookie")

    while True:
        print("\n--- What would you like to do? ---")
        print("1. Eat")
        print("2. Sleep")
        print("3. Play")
        print("4. Train")
        print("5. Show Tricks")
        print("6. Check Status")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pet.eat()
            print("Nom nom!")
        elif choice == "2":
            pet.sleep()
            print("Zzz...")
        elif choice == "3":
            pet.play()
            print("Yay!")
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
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
