import sys
import os, platform
import json

#check if json is empty
try:
    with open("data/exercises.json", mode="r", encoding="utf-8") as read_ex:
        #if json is not empty, read file
        exercises = json.load(read_ex)
#if json is empty, initialize excercises as a regular list
except Exception:
    exercises = []

try:
    with open("data/workouts.json", mode="r", encoding="utf-8") as read_wo:
        #if json is not empty, read file
        workouts = json.load(read_wo)
#if json is empty, initialize excercises as a regular list
except Exception:
    workouts = {}

def main():
    #ask user for an action, perform said action and loop until the program is stopped
    while True:
        try:
            choice = get_choice()
            match choice:
                case 1:
                    clear_terminal()
                    add_exercise()
                case 2:
                    clear_terminal()
                    edit_exercise()
                case 3:
                    clear_terminal()
                    #placeholder output
                    print("Remove exercise")
                case 4:
                    clear_terminal()
                    add_workout()
                case 5:
                    clear_terminal()
                    #placeholder output
                    print("View workouts")
                case 6:
                    clear_terminal()
                    #placeholder output
                    print("Remove workout")
                case 7:
                    clear_terminal()
                    sys.exit("Thank you for using CLIWOP\n")
                case _:
                    raise ValueError
        except ValueError:
            clear_terminal()
            print("Invalid input\n\nPlease choose an action from the provided list")
            pass

def get_choice():
    #Display list of actions, then ask for a choice from the user
    print("\nWelcome to CLIWOP - Please choose an action\n")
    print("1. Add an exercise")
    print("2. Edit an exercise")
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
    save_exercises()
    print(f"\n{exercise_name} ({exercise_group} exercise) is added to the list of exercises")

def edit_exercise():
    #Edit an existing exercise in the list
    if not exercises:
        print("Please add exercises before trying to edit the list")
    else:
        while True:
            print("Exercise list:\n")
            for exercise in exercises:
                print(f"{exercise["name"]} ({exercise["group"]})")
            to_edit = input("\nWhich exercise to edit: ")
            if not any(exercise["name"] == to_edit for exercise in exercises):
                clear_terminal()
                print("Invalid exercise, please select an exercise from the list\n")
            else:
                what_edit = input(f"Edit the name or group for {to_edit}?: ")
                if what_edit == "group":
                    for exercise in exercises:
                        if exercise["name"] == to_edit:
                            exercise["group"] = input("New muscle group worked: ")
                            save_exercises()
                            clear_terminal()
                elif what_edit == "name":
                    for exercise in exercises:
                        if exercise["name"] == to_edit:
                            exercise["name"] = input("New name: ")
                            save_exercises()
                            clear_terminal()
                else:
                    clear_terminal()
                    print("Invalid choice, please input 'name' or 'group'\n")
                

def remove_exercise():
    #Delete an existing exercise from the list
    ...

def add_workout():
    #Add a new workout program to the list using created exercises, then specify the reps and sets
    if not exercises:
        print("Please add exercises before creating a workout")
    else:
        workout_name = input("Name of the workout: ")
        workout = []
        clear_terminal()
        while True:
            print(f"Workout name: {workout_name}")
            print("\nExercise list:\n")
            for exercise in exercises:
                print(f"{exercise["name"]} ({exercise["group"]})")
            print("\nEnter 'stop' to stop adding exercises")
            try:
                workout_ex = input("\nExercise to add to workout: ")
                if workout_ex == "stop":
                    clear_terminal()
                    break #Exit the loop when stop" is entered
                else:
                    workout_ex_reps = input("Ammount of repitions to perform: ")
                    if workout_ex_reps == "stop":
                        clear_terminal()
                        break #Exit the loop when "stop" is entered
                    else:
                        workout_ex_sets = input("How many sets for this exercise?: ")
                        if workout_ex_sets == "stop":
                            clear_terminal()
                            break #Exit the loop when "stop" is entered
                        else:
                            workout_exercise = {
                                "exercise": workout_ex,
                                "reps": workout_ex_reps,
                                "sets": workout_ex_sets
                            }
                            workout.append(workout_exercise)
                            clear_terminal()
            except Exception as e:
                print(f"An error occured: {e}")
                break
        if workout:
            workouts[workout_name] = workout
            save_workouts()
            print(f"\n{workout_name} is added to the list of workouts")

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

def save_exercises():
    with open("data/exercises.json", mode="w", encoding="utf-8") as write_ex:
        json.dump(exercises, write_ex)

def save_workouts():
    with open("data/workouts.json", mode="w", encoding="utf-8") as write_wo:
        json.dump(workouts, write_wo)


if __name__ == "__main__":
    main()