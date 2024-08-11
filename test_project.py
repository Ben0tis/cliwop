import pytest
from unittest.mock import patch
import project

#input 1, then 7 when prompted
@patch('builtins.input', side_effect=['1', '7'])
#mock the clear_terminal function
@patch('project.clear_terminal')
#mock the add_exercise funtion - only need to check that it is called when input = 1, no need to run it
@patch('project.add_exercise')
def test_main_menu(mock_add_exercise, mock_clear, mock_input):
    #check for SystemExit when input = 7
    with pytest.raises(SystemExit):
        project.main()
    mock_add_exercise.assert_called_once()

#input new execise, then arms, then stop
@patch('builtins.input', side_effect=['New Exercise', 'Arms', 'stop'])
#mock data
@patch('project.exercises', [])
#mock the save exercises function - no need to run it
@patch('project.save_exercises')
def test_add_exercise(mock_save_exercises, mock_input):
    #call add_exercise with the mock inputs
    project.add_exercise()
    #checks if input was added to list
    assert len(project.exercises) == 1
    #check if name and group is as input
    assert project.exercises[0]['name'] == 'New Exercise'
    assert project.exercises[0]['group'] == 'Arms'
    #check that save_exercises is called by add_exercise
    mock_save_exercises.assert_called_once()

#input push-ups then stop
@patch('builtins.input', side_effect=['Push-ups', 'stop'])
#mock data
@patch('project.exercises', [{"name": "Push-ups", "group": "Chest"}])
#mock the save exercises function
@patch('project.save_exercises')
def test_remove_exercise(mock_save_exercises, mock_input):
    #call remove_exercise with the mock inputs
    project.remove_exercise()
    #check that push-ups was removed from list
    assert len(project.exercises) == 0
    #check that save_exercises was called by remove_exercise
    mock_save_exercises.assert_called_once()

#input new workout, then exercise params then stop
@patch('builtins.input', side_effect=['New Workout', 'Push-ups', '10', '3', 'stop'])
#mock data
@patch('project.exercises', [{"name": "Push-ups", "group": "Chest"}])
@patch('project.workouts', {})
#mock save workouts function
@patch('project.save_workouts')
def test_add_workout(mock_save_workouts, mock_input):
    project.add_workout()
    #check that workout was added
    assert len(project.workouts) == 1
    #check that save_workouts was called by add_workout
    mock_save_workouts.assert_called_once()

#input name of workout, then stop
@patch('builtins.input', side_effect=['Full Body', 'stop'])
#mock data
@patch('project.workouts', {"Full Body": [{"exercise": "Push-ups", "reps": "10", "sets": "3"}]})
#mock save_workouts
@patch('project.save_workouts')
def test_remove_workout(mock_save_workouts, mock_input):
    project.remove_workout()
    #check that workout was removed
    assert len(project.workouts) == 0
    #check that save_workouts was called by remove_workout
    mock_save_workouts.assert_called_once()