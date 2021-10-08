import sys
import tkinter as tk
from tkinter import messagebox


# This function is what I am going to use to create a Warning popup box
def warningmsg(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning(title, message)
    root.update()


class MonitoringSystem:

    # Using a static method because we need the function to be tied to the class and not necessarily an instance of
    # the class
    @staticmethod
    def AnimalCase():
        # Printing out a menu
        print("Choose an animal to monitor")
        print("Press 1 for Lion")
        print("Press 2 for Tiger")
        print("Press 3 for Bear")
        print("Press 4 for Giraffe")

        # Getting user input
        option = int(input())
        print()

        # Making the variable animal the user option
        if option == 1:
            animal = "Animal - Lion"
        elif option == 2:
            animal = "Animal - Tiger"
        elif option == 3:
            animal = "Animal - Bear"
        elif option == 4:
            animal = "Animal - Giraffe"
        else:
            sys.exit("Invalid choice: system exiting")

        # Try block to catch errors
        try:
            # Reading the file animals.txt file
            f = open("animals.txt", "r")

            # Reading the first line
            # Then going into a while loop to check if the line contains the user choice
            line = f.readline()
            while line:
                if animal in line:
                    break
                line = f.readline()

            # Reading the rest of the information
            name = f.readline()
            age = f.readline()
            health = f.readline()
            feed = f.readline()

            # If there is a problem we will print out a popup window
            if "*****" in health:
                print(animal, '\n')
                print(name)
                print(age)
                warningmsg("Warning " + animal, health)  # TODO: Print a window pane with an error here
                print(feed)

            elif "*****" in feed:
                print(animal, '\n')
                print(name)
                print(age)
                print(health)
                warningmsg("Warning " + animal, feed)  # TODO: Print a window pane with an error here

            else:
                print(animal, '\n')
                print(name)
                print(age)
                print(health)
                print(feed)

            # Closing the file
            f.close()

        # Catching error if file not found
        except (FileNotFoundError, IOError):
            print("The File was not found")

    # Using a static method because we need the function to be tied to the class and not necessarily an instance of
    # the class
    @staticmethod
    def HabitatCase():
        # Printing out a menu
        print("Choose what habitat you would like to monitor")
        print("Press 1 for the Penguin Habitat")
        print("Press 2 for the Bird house")
        print("Press 3 for the Aquarium")

        # Getting user input
        option = int(input())

        # Making the habitat variable the user option
        if option == 1:
            habitat = "Habitat - Penguin"
        elif option == 2:
            habitat = "Habitat - Bird"
        elif option == 3:
            habitat = "Habitat - Aquarium"
        else:
            sys.exit("Invalid choice: system exiting")

        # Try block to catch errors
        try:
            # Reading the file animals.txt file
            f = open("habitats.txt", "r")

            # Reading the first line
            # Then going into a while loop to check if the line contains the user choice
            line = f.readline()
            while line:
                if habitat in line:
                    break
                line = f.readline()

            # Reading the rest of the information
            temperature = f.readline()
            food = f.readline()
            cleanliness = f.readline()

            # Closing the file
            f.close()

            # Outputting all data and checking for any concerns
            if "*****" in temperature:
                print(habitat, '\n')
                warningmsg("Warning " + habitat, temperature)
                print(food)
                print(cleanliness)

            elif "*****" in food:
                print(habitat, '\n')
                print(temperature)
                warningmsg("Warning " + habitat, food)
                print(cleanliness)

            elif "*****" in cleanliness:
                print(habitat, '\n')
                print(temperature)
                print(food)
                warningmsg("Warning " + habitat, cleanliness)

            else:
                print(habitat, "\n")
                print(temperature)
                print(food)
                print(cleanliness)


        # Catching error if file not found
        except (FileNotFoundError, IOError):
            print("The File was not found")


# Main part of our code that will call the MonitoringSystem class and its functions

while True:
    # Printing the main menu
    print("Welcome to the Zoo Monitoring System")
    print("Press 1 to monitor animals")
    print("Press 2 to monitor habitats")
    print("Press 3 to Exit")

    # Getting the choice from the user
    choice = input()
    print()

    if choice == str(1):
        MonitoringSystem.AnimalCase()
    elif choice == str(2):
        MonitoringSystem.HabitatCase()
    elif choice == str(3):
        sys.exit()
    else:
        print("Invalid choice: Please try again")
        print()
        continue
