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
                    #placeholder output
                    print("Edit exercise")
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
    with open("data/exercises.json", mode="w", encoding="utf-8") as write_ex:
        json.dump(exercises, write_ex)
    print(f"\n{exercise_name} ({exercise_group} exercise) is added to the list")

def edit_exercise():
    #Edit an existing exercise in the list
    ...

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
            with open("data/workouts.json", mode="w", encoding="utf-8") as write_wo:
                json.dump(workouts, write_wo)

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