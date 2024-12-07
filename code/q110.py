# Your code here
def compute_robot_distance(movements):
    x, y = 0, 0

    for move in movements:
        direction, steps = move.split()
        steps = int(steps)

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    distance = (x**2 + y**2)**0.5
    rounded_distance = round(distance)

    return rounded_distance

print(compute_robot_distance(["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]))
### test.py
import pytest, io, sys, json, mock, re, os

@pytest.mark.it('The function compute_robot_distance must exist')
def test_function_existence(capsys, app):
    assert app.compute_robot_distance

@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    movements_list = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]
    assert app.compute_robot_distance(movements_list) ==  2

@pytest.mark.it('The solution should work with other entries')
def test_another_output(capsys, app):
    movements_list = ["DOWN 20", "UP 5", "LEFT 5", "RIGHT 2"]
    assert app.compute_robot_distance(movements_list) ==  15

@pytest.mark.it('The solution should work with negative inputs')
def test_negative_inputs(capsys, app):
    movements_list = ["DOWN -1", "UP -5", "LEFT 50", "RIGHT 20"]
    assert app.compute_robot_distance(movements_list) ==  30