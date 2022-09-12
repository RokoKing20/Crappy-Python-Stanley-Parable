import random

points = 0
losing_points = 0
letters = ["1","2","3","4","5","6","7","8","9","0","10","q","Q","W","w","E","e","R","r","T","t","Z","z","U","u","I","i","O","o","P","p","A","a","S","s","D","d","F","f","G","g","H","h","J","j","K","k","L","l"]

def adding_points(points):
    points = points + 1
    return points

def losier_points(losing_points):
    losing_points = losing_points + 1
    return losing_points

def task(user_input, answer):
    if user_input == answer:
        return True
    else:
        return False


def game_logic(user_input, answer):
    if task(user_input, answer) ==  True:
        adding_points()
    elif task(user_input, answer):
        losier_points()

def random_choose(list):
    return random.choice(list)

def check(string):
    if string == "Yes":
        return True
    else:
        return False

def check_user(random_string, user_input):
    if user_input == random_string:
        return True
    elif user_input != random_string:
        return False