import sys
import os, platform

#initialise in-memory data for exercises and workouts
exercises = []
workouts = []
#probably a good idea to implement JSON file later down the line for persistence

def main():
    #ask user for an action, perform said action and loop until the program is stopped
    while True:
        try:
            choice = get_choice()
            match choice:
                case 1:
                    clear_terminal()
                    add_exercise()
                    print()
                    print(exercises)
                case 2:
                    clear_terminal()
                    print("Edit exercise")
                case 3:
                    clear_terminal()
                    print("Remove exercise")
                case 4:
                    clear_terminal()
                    add_workout()
                    print()
                    print(workouts)
                case 5:
                    clear_terminal()
                    print("View workouts")
                case 6:
                    clear_terminal()
                    print("Remove workout")
                case 7:
                    clear_terminal()
                    sys.exit("Thank you for using CLIWOP\n")
        except ValueError:
            clear_terminal()
            print("Invalid input\n\nPlease choose an action from the provided list")
            pass

def get_choice():
    #Display list of actions, then ask for a choice from the user
    print("\nWelcome to CLIWOP - Please choose an action\n")
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
    exercise_name = input("Exercise name: ")
    exercise_group = input("Muscle group worked: ")
    exercise = {
        "name": exercise_name,
        "group": exercise_group
    }
    exercises.append(exercise)
    print(f"\n{exercise_name} ({exercise_group} exercise) is added to the list")

def edit_exercise():
    #Edit an existing exercise in the list
    ...

def remove_exercise():
    #Delete an existing exercise from the list
    ...

def add_workout():
    #Add a new workout program to the list using created exercises, then specify the reps and sets
    program = []
    if not exercises:
        print("Please add exercises before creating a workout")
    else:
        while True:
            print("Exercise list:\n")
            for exercise in exercises:
                print(f"{exercise["name"]} ({exercise["group"]})")
            print("\nEnter 'Stop' to stop adding exercises")
            try:
                workout_exercise = input("\nExercise to add to workout: ")
                if workout_exercise == "Stop":
                    clear_terminal()
                    break #Exit the loop when "Stop" is entered
                else:
                    workout_reps = input("Ammount of repitions to perform: ")
                    if workout_reps == "Stop":
                        clear_terminal()
                        break #Exit the loop when "Stop" is entered
                    else:
                        workout_sets = input("How many sets for this exercise?: ")
                        if workout_sets == "Stop":
                            clear_terminal()
                            break #Exit the loop when "Stop" is entered
                        else:
                            workout = {
                                "exercise": workout_exercise,
                                "reps": workout_reps,
                                "sets": workout_sets
                            }
                            program.append(workout)
                            clear_terminal()
            except Exception as e:
                print(f"An error occured: {e}")
                break
        if program:
            workouts.append(program)

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