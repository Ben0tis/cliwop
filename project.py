import sys
import os, platform

#initialise in-memory data for exercises and workouts
exercises = [{}]
workouts = [{}]
#probably a good idea to implement JSON file later down the line for persistence

def main():
    #ask user for an action, perform said action and loop until the program is stopped
    while True:
        try:
            choice = get_choice()
            match choice:
                case 1:
                    clear_terminal()
                    print("Add exercise\n")
                case 2:
                    clear_terminal()
                    print("Edit exercise\n")
                case 3:
                    clear_terminal()
                    print("Remove exercise\n")
                case 4:
                    clear_terminal()
                    print("Add workout\n")
                case 5:
                    clear_terminal()
                    print("View workouts\n")
                case 6:
                    clear_terminal()
                    print("Remove workout\n")
                case 7:
                    clear_terminal()
                    sys.exit("Thank you for using CLIWOP\n")
                case _:
                    clear_terminal()
                    print("Invalid choice\n")
        except ValueError:
            pass

def get_choice():
    #Display list of actions, then ask for a choice from the user
    print("Welcome to CLIWOP - Please choose an action\n")
    print("1. Add an exercise")
    print("2. Edit and exercise")
    print("3. Remove an exercise")
    print("4. Add a workout")
    print("5. View workouts")
    print("6. Remove a workout")
    print("7. Exit CLIWOP")
    return int(input("\nChoice: "))

def add_exercise():
    #Add a new exercise to the list, then specify the name and muscle group
    ...

def edit_exercise():
    #Edit an existing exercise in the list
    ...

def remove_exercise():
    #Delete an existing exercise from the list
    ...

def add_workout():
    #Add a new workout program to the list using created exercises, then specify the reps and sets
    ...

def view_workout():
    #Display the workout programs in the list, then choose one to display detailed information
    ...

def remove_workout():
    #Delete a workout from the list
    ...

def clear_terminal():
    #Clear terminal using the approriate function depending on windows vs unix/macOS
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()