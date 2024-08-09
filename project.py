#initialise in-memory data for exercises and workouts
exercises = [{}]
workouts = [{}]
#probably a good idea to implement JSON file later down the line for persistence

def main():
    #Placeholder match/case for testing
    choice = get_choice()
    match choice:
        case 1:
            print("Add exercise")
        case 2:
            print("Edit exercise")
        case 3:
            print("Remove exercise")
        case 4:
            print("Add workout")
        case 5:
            print("View workouts")
        case 6:
            print("Remove workout")
        case _:
            print("Invalid choice")

def get_choice():
    #Display list of actions, then ask for a choice from the user
    print("Welcome to CLIWOP - Please choose and action")
    print("1. Add an exercise")
    print("2. Edit and exercise")
    print("3. Remove an exercise")
    print("4. Add a workout")
    print("5. View workouts")
    print("6. Remove a workout")
    return int(input("Choice: "))

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

if __name__ == "__main__":
    main()