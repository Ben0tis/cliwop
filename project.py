import sys
import os, platform
import json

class UserExit(BaseException):
    pass

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
    #ask user for an action, perform said action and loop until the program is stopped with input = 7
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
                    remove_exercise()
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
    #Add input to exercise and push to json file
    exercises.append(exercise)
    save_exercises()
    print(f"\n{exercise_name} ({exercise_group} exercise) is added to the list of exercises")

def edit_exercise():
    #Edit an existing exercise in the list
    #Check if there are exercises in the list first
    if not exercises:
        print("Please add exercises before trying to edit the list")
    else:
        #Loop until user inputs "stop"
        while True:
            try:
                display_exercises()
                print("\nEnter 'stop' to stop editing exercises")
                #Get input of which exercise needs to be edited
                to_edit = get_input("\nWhich exercise to edit: ")
                #If the selected exercise is not in the list, loop
                if not any(exercise["name"] == to_edit for exercise in exercises):
                    clear_terminal()
                    print("Invalid exercise, please select an exercise from the list\n")
                #If the selected exercise is in the list, continue
                else:
                    #Get input of what to edit
                    what_edit = get_input(f"Edit the name or group for {to_edit}?: ")
                    if what_edit == "group":
                        for exercise in exercises:
                            #Only edit the exercise that was selected above
                            if exercise["name"] == to_edit:
                                #Change group and push to json
                                exercise["group"] = get_input("New muscle group worked: ")
                                save_exercises()
                                clear_terminal()
                    elif what_edit == "name":
                        for exercise in exercises:
                            #Only edit the exercise that was selected above
                            if exercise["name"] == to_edit:
                                #Change name and push to json
                                exercise["name"] = get_input("New name: ")
                                save_exercises()
                                clear_terminal()
                    #If input not 'name' or 'group', display error message and loop
                    else:
                        clear_terminal()
                        print("Invalid choice, please input 'name' or 'group'\n")
            #Exit back to main menu if user inputs "stop"
            except UserExit:
                clear_terminal()
                break
                

def remove_exercise():
    #Delete an existing exercise from the list
    #Check if there are exercises in the list first
    if not exercises:
        print("Please add exercises before trying to delete one from the list")
    else:
        #Loop until user inputs "stop"
        while True:
            try:
                display_exercises()
                print("\nEnter 'stop' to stop deleting exercises")
                #Get input of which exercise needs to be deleted
                to_delete = get_input("\nWhich exercise to delete: ")
                #If the selected exercise is not in the list, loop
                if not any(exercise["name"] == to_delete for exercise in exercises):
                    clear_terminal()
                    print("Invalid exercise, please select an exercise from the list\n")
                #If the selected exercise is in the list, continue
                else:
                    for exercise in exercises:
                    #Delete the exercise that was selected above
                        exercises[:] = [exercise for exercise in exercises if exercise["name"] != to_delete]
                        save_exercises()
                        clear_terminal()
            #Exit back to main menu if user inputs "stop"
            except UserExit:
                clear_terminal()
                break

def add_workout():
    #Add a new workout program to the list using created exercises, then specify the reps and sets
    #Check if there are exercises in the list first ***Could implement a way to check if the exercises added to workout are in list***
    if not exercises:
        print("Please add exercises before creating a workout")
    else:
        workout_name = input("Name of the workout: ")
        workout = []
        clear_terminal()
        #Loop until user inputs "stop"
        while True:
            print(f"Workout name: {workout_name}")
            #Display list of exercises ***Could implement a way to filter and/or organize by muscle worked*** Could refactor into separate function***
            display_exercises()
            print("\nEnter 'stop' to stop adding exercises")
            #Get user input for exercise name, reps and sets then add to workout
            try:
                workout_ex = get_input("\nExercise to add to workout: ")
                workout_ex_reps = get_input("Ammount of repitions to perform: ")
                workout_ex_sets = get_input("How many sets for this exercise?: ")
                workout_exercise = {
                    "exercise": workout_ex,
                    "reps": workout_ex_reps,
                    "sets": workout_ex_sets
                    }
                workout.append(workout_exercise)
                clear_terminal()
            #Stop loop if user inputs "stop"
            except UserExit:
                clear_terminal()
                break
        #If exercises were added to workout before "stop" input, push to json
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
    #Push exercises list of dicts to json file
    with open("data/exercises.json", mode="w", encoding="utf-8") as write_ex:
        json.dump(exercises, write_ex)

def save_workouts():
    #Push workouts dict of list of dicts to json file
    with open("data/workouts.json", mode="w", encoding="utf-8") as write_wo:
        json.dump(workouts, write_wo)

def get_input(prompt):
    #Check if user input is "stop"; if yes, raise UserExit
    response = input(prompt)
    if response=="stop":
        raise UserExit
    return response

def display_exercises():
    #Display list of exercises ***Could implement a way to filter and/or organize by muscle worked***
    print("\nExercise list:\n")
    for exercise in exercises:
        print(f"{exercise["name"]} ({exercise["group"]})")


if __name__ == "__main__":
    main()