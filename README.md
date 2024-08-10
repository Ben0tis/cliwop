# CLI Workout Planner (CLIWOP)
#### By: Benjamin Desmeules Otis
#### GitHub and EdX: Ben0tis
#### From: Quebec, Canada
#### Video Demo (Recorded on XXXX-XX-XX): ==TO DO==

## Project Overview

The **CLI Workout Planner** is a command-line application that allows users to manage exercices and create personalized workout programs. Designed to be simple and easy to use, this tool is perfect for those looking to organize their workout routines without the need for complex software.

## Features

- **Add Exercise**: Add new exercises to your exercise database, specifying the name and muscle group worked.
- **Edit Exercise**: Modify existing exercises in your database.
- **Remove Exercise**: Delete exercises that you no longer need.
- **Add Workout**: Build a workout program by selecting exercises from the database, specifying the ammount of reps and sets.
- **View Workout**: Display the workout programs you have created.
- **Remove Workout**: Delete workouts that you no longer need.

## Usage

### Adding an Exercise

1. Choose the `Add an exercise` option from the main menu.
2. Enter the name of the exercise when prompted.
3. Specify the muscle group worked by the exercise.
4. The exercise will be added to your database, and you will receive confirmation.
5. Repeat steps 2 to 4 until required exercises are added.
6. Input `stop` to return to the main menu.

### Editing an Exercise

1. Choose the `Edit an exercise` option from the main menu.
2. Select the exercise you want to edit from the list of existing exercises.
3. Specify whether you want to edit the name or the muscle group.
4. Provide the new value, and the exercise will be updated in your database.
5. Repeat steps 2 to 4 until required exercises are added.
6. Input `stop` to return to the main menu.

### Removing an Exercise

1. Choose the `Remove an exercise` option from the main menu.
2. Select the exercise you want to remove from the list.
3. The selected exercise will be deleted from your database, and you will receive confirmation.
4. Repeat steps 2 and 3 until the required exercises are removed.
5. Input `stop` to return to the main menu.

### Creating a Workout

1. Choose the `Add a workout` option from the main menu.
2. Enter a name for your workout program.
3. Select exercises from the database to include in the workout.
4. Specify the number of reps and sets.
5. Repeat steps 3 and 4 until required exercises are added.
6. Input `stop` to save workout and return to the main menu.
7. The workout will be added to your database, and you will receive confirmation.

### Viewing a Workout

1. Choose the `View workouts` option from the main menu.
2. Select the workout program you want to view from the list.
3. The details of the workout, including exercises, reps, and sets, will be displayed.
4. Input `stop` to return to the main menu.

### Removing a Workout

1. Choose the `Remove workouts` option from the main menu.
2. Select the workout program you want to delete from the list.
3. The selected workout will be removed from your database, and you will receive confirmation.
4. Repeat steps 2 and 3 until required workouts are removed.
5. Input `stop` to return to the main menu.

### Exiting the program

* Choose the `Exit CLIWOP` option from the main menu or;
* Input `exit` in any menu.

## Future Enhancements

- [x]  Implement a way to check if exercise added to workout is in list
- [x]  Include standard exercises and workouts
- [ ]  Inplement a way to filter the exercises and workouts lists
- [ ]  Implement a way to organize the lists by name or muscle group worked
