import sys
import os, platform
import json
from tabulate import tabulate
from pyfiglet import Figlet
from colorama import Fore, Style, init

init(autoreset=True)

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
#if json is empty, initialize excercises as a regular dict
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
                    view_workout()
                case 6:
                    clear_terminal()
                    remove_workout()
                case 7:
                    clear_terminal()
                    print(Fore.GREEN + "Thank you for using")
                    title("CLIWOP")
                    sys.exit()
                case _:
                    raise ValueError
        except ValueError:
            clear_terminal()
            print(Fore.RED + Style.BRIGHT +"Invalid input\n")
            print(Fore.RED + "Please choose an action from the provided list")
            pass

def get_choice():
    #Display list of actions, then ask for a choice from the user
    table = [
        [1, "Add an exercise"], [2, "Edit an exercise"], [3, "Remove an exercise"], 
        [4, "Add a workout"], [5, "View workouts"], [6, "Remove workouts"], [7, "Exit CLIWOP"]
        ]
    print(Fore.GREEN + "\nWelcome to")
    title("CLIWOP")
    print(Fore.GREEN + "Please choose an action\n")
    print(Fore.GREEN + Style.BRIGHT + tabulate(table, tablefmt="double_grid"))
    return int(get_input(Fore.GREEN + "\nChoice: "))

def add_exercise():
    #Loop until user inputs "stop"
    while True:
        try:
            title("Create exercises\n")
            print(Fore.GREEN + Style.DIM + "\nEnter 'stop' to stop editing exercises\n")
            #Add a new exercise to the list, then specify the name and muscle group
            exercise_name = get_input(Fore.GREEN + "Exercise name: ")
            exercise_group = get_input(Fore.GREEN + "Muscle group worked: ")
            exercise = {
                "name": exercise_name,
                "group": exercise_group
            }
            #Add input to exercise and push to json file
            exercises.append(exercise)
            save_exercises()
            clear_terminal()
            print(Fore.YELLOW + Style.BRIGHT + f"\n\"{exercise_name}\" ({exercise_group} exercise) is added to the list of exercises")
        except UserExit:
            clear_terminal()
            break

def edit_exercise():
    #Edit an existing exercise in the list
    #Check if there are exercises in the list first
    if not exercises:
        print(Fore.RED + "Please add exercises before trying to edit the list")
    else:
        #Loop until user inputs "stop"
        while True:
            try:
                title("Edit exercises\n")
                display_exercises()
                print(Fore.GREEN + Style.DIM + "\nEnter 'stop' to stop editing exercises")
                #Get input of which exercise needs to be edited
                to_edit = get_input(Fore.GREEN + "\nWhich exercise to edit: ")
                #If the selected exercise is not in the list, loop
                if not any(exercise["name"] == to_edit for exercise in exercises):
                    clear_terminal()
                    print(Fore.RED + Style.BRIGHT + "Invalid exercise\n")
                    print(Fore.RED + "Please select an exercise from the list\n")
                #If the selected exercise is in the list, continue
                else:
                    #Get input of what to edit
                    what_edit = get_input(Fore.GREEN + f"Edit the name or group for {to_edit}?: ")
                    if what_edit == "group":
                        for exercise in exercises:
                            #Only edit the exercise that was selected above
                            if exercise["name"] == to_edit:
                                #Change group and push to json
                                exercise["group"] = get_input(Fore.GREEN + "New muscle group worked: ")
                                save_exercises()
                                clear_terminal()
                    elif what_edit == "name":
                        for exercise in exercises:
                            #Only edit the exercise that was selected above
                            if exercise["name"] == to_edit:
                                #Change name and push to json
                                exercise["name"] = get_input(Fore.GREEN +"New name: ")
                                save_exercises()
                                clear_terminal()
                    #If input not 'name' or 'group', display error message and loop
                    else:
                        clear_terminal()
                        print(Fore.RED + Style.BRIGHT + "Invalid choice\n")
                        print(Fore.RED + "Please input 'name' or 'group'\n")
            #Exit back to main menu if user inputs "stop"
            except UserExit:
                clear_terminal()
                break
                

def remove_exercise():
    #Delete an existing exercise from the list
    #Check if there are exercises in the list first
    if not exercises:
        print(Fore.RED + "Please add exercises before trying to delete one from the list")
    else:
        #Loop until user inputs "stop"
        while True:
            try:
                title("Remove exercises\n")
                display_exercises()
                print(Fore.GREEN + Style.DIM + "\nEnter 'stop' to stop deleting exercises")
                #Get input of which exercise needs to be deleted
                to_delete = get_input(Fore.GREEN + "\nWhich exercise to delete: ")
                #If the selected exercise is not in the list, loop
                if not any(exercise["name"] == to_delete for exercise in exercises):
                    clear_terminal()
                    print(Fore.RED + Style.BRIGHT + "Invalid exercise\n")
                    print(Fore.RED + "Please select an exercise from the list\n")
                #If the selected exercise is in the list, continue
                else:
                    for exercise in exercises:
                    #Delete the exercise that was selected above
                        exercises[:] = [exercise for exercise in exercises if exercise["name"] != to_delete]
                        save_exercises()
                        clear_terminal()
                        print(Fore.YELLOW + Style.BRIGHT + f"\n\"{to_delete}\" has been removed from the list of exercises")
            #Exit back to main menu if user inputs "stop"
            except UserExit:
                clear_terminal()
                break

def add_workout():
    #Add a new workout program to the list using created exercises, then specify the reps and sets
    #Check if there are exercises in the list first
    if not exercises:
        print(Fore.RED + "Please add exercises before creating a workout")
    else:
        title("Create workouts\n")
        workout_name = input("Name of the workout: ")
        workout = []
        clear_terminal()
        #Loop until user inputs "stop"
        while True:
            title("Create workouts\n")
            print(Fore.GREEN + f"Workout name: {workout_name}\n")
            #Display list of exercises
            display_exercises()
            print(Fore.GREEN + Style.DIM + "\nEnter 'stop' to stop adding exercises")
            #Get user input for exercise name, reps and sets then add to workout
            try:
                workout_ex = get_input(Fore.GREEN + "\nExercise to add to workout: ")
                # Check if the exercise is in the list of exercises
                if not any(exercise["name"] == workout_ex for exercise in exercises):
                    raise ValueError()
                workout_ex_reps = get_input(Fore.GREEN + "Ammount of repitions to perform: ")
                workout_ex_sets = get_input(Fore.GREEN + "How many sets for this exercise?: ")
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
            except ValueError:
                clear_terminal()
                print(Fore.RED + Style.BRIGHT + "Invalid exercise\n")
                print(Fore.RED + "Please select an exercise from the list\n")
                pass
        #If exercises were added to workout before "stop" input, push to json
        if workout:
            workouts[workout_name] = workout
            save_workouts()
            print(Fore.YELLOW + Style.BRIGHT + f"\n{workout_name} is added to the list of workouts")

def view_workout():
    #Display the workout programs in the list, then choose one to display detailed information
    if not workouts:
        print(Fore.RED + "Please add workouts before trying to view the list")
    else:
        #Loop until user inputs "stop"
        while True:
            try:
                title("View workouts\n")
                display_workouts()
                print(Fore.GREEN + Style.DIM + "\nEnter 'stop' to stop viewing workouts")
                #Get input of which exercise needs to be edited
                to_view = get_input(Fore.GREEN + "\nWhich workout to view: ")

                if to_view  in workouts:
                    clear_terminal()
                    title("View workouts\n")
                    # Prepare data for tabulate
                    workout_data = [
                        [i + 1, exercise["exercise"], exercise["sets"], exercise["reps"]]
                        for i, exercise in enumerate(workouts[to_view])
                    ]
                    headers = ["#", "Exercise", "Sets", "Reps"]
                    
                    # Display the workout details using tabulate
                    print(Fore.GREEN + Style.BRIGHT + tabulate(workout_data, headers=headers, tablefmt="double_grid"))
                        
                    check_stop = get_input(Fore.GREEN + Style.DIM + "\nEnter 'stop' to stop viewing workout: ")
                #If input not in workouts list, loop
                else:
                    clear_terminal()
                    print(Fore.RED + Style.BRIGHT + "Invalid workout name\n")
                    print(Fore.RED + "Please select a workout from the list\n")
            #Stop loop if user inputs "stop"
            except UserExit:
                clear_terminal()
                break

def remove_workout():
    #Delete a workout from the list
    #Check if there are workouts in the list first
    if not workouts:
        print(Fore.RED + "Please add workouts before trying to delete one from the list")
    else:
        #Loop until user inputs "stop"
        while True:
            try:
                title("Remove workouts\n")
                display_workouts()
                print(Fore.GREEN + Style.DIM + "\nEnter 'stop' to stop deleting workouts")
                #Get input of which workout needs to be deleted
                to_delete = get_input(Fore.GREEN + "\nWhich workout to delete: ")
                #If the selected workout is not in the list, loop
                if not any(workout == to_delete for workout in workouts):
                    clear_terminal()
                    print(Fore.RED + Style.BRIGHT + "Invalid workout\n")
                    print(Fore.RED + "Please select a workout from the list\n")
                #If the selected workout is in the list, continue
                else:
                    #Delete the workout that was selected above
                        del workouts[to_delete]
                        save_workouts()
                        clear_terminal()
                        print(Fore.YELLOW + Style.BRIGHT + f"\n\"{to_delete}\" has been removed from the list of exercises")
            #Exit back to main menu if user inputs "stop"
            except UserExit:
                clear_terminal()
                break

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
    if response.lower()=="stop":
        raise UserExit
    #Check if user input is "exit"; if yes, abort program
    elif response.lower() =="exit":
        clear_terminal()
        print(Fore.GREEN + "Thank you for using")
        title("CLIWOP")
        sys.exit()
    return response

def display_exercises():
    #Display list of exercises ***Could implement a way to filter and/or organize by muscle worked***
    #Prepare for tabulation
    ex_table = [[exercise["name"], exercise["group"]] for exercise in exercises]
    ex_headers = ["Exercise name", "Muscle Group"]
    #Create and display table
    print(Fore.GREEN + Style.BRIGHT + tabulate(ex_table, ex_headers, tablefmt="double_grid"))

def display_workouts():
    #Display list of workouts ***Could implement a way to filter and/org organize***
    #Prepare for tabulation
    wo_table = [[workout] for workout in workouts.keys()]
    wo_headers = ["Workout name"]
    #Create and display table
    print(Fore.GREEN + Style.BRIGHT + tabulate(wo_table, wo_headers, tablefmt="double_grid"))

def title(text):
    f = Figlet(font="standard")
    titled = (f.renderText(text))
    print(Fore.GREEN + Style.BRIGHT + titled, end="")

if __name__ == "__main__":
    main()