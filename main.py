from pet import Pet

def main():
    print("Welcome to Pet Class!")
    name = input("Name your pet: ")
    pet = Pet(name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Check pet status")
        print("5. Teach a new trick")
        print("6. Show learned tricks")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            pet.get_status()
        elif choice == "5":
            trick = input("Enter a trick to teach: ")
            pet.train(trick)
        elif choice == "6":
            pet.show_tricks()
        elif choice == "7":
            print("Goodbye! Come back soon!")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
