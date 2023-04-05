import random
import math

def gen_random_name() -> str:
    names = ['Alex', 'Avery', 'Bailey', 'Charlie', 'Dakota', 'Ellis', 'Emerson', 'Finley', 'Harper', 'Jordan', 'Kai', 'Lee', 'Logan', 'Morgan', 'Parker', 'Reese', 'Rowan', 'Sage', 'Skyler', 'Taylor', 'Zion', 'Adrian', 'Blair', 'Cameron', 'Devon', 'Eli', 'Finn', 'Gale', 'Hayden', 'Indigo', 'Jamie', 'Jesse', 'Kendall', 'Kit', 'Micah', 'Nico', 'Phoenix', 'Remy', 'Riley', 'Sasha', 'Shay', 'Sidney', 'Spencer', 'Tate', 'Toby', 'Yael']
    choice = random.choice(names)
    if names:
        names.remove(choice)
    else:
        names = ['Alex', 'Avery', 'Bailey', 'Charlie', 'Dakota', 'Ellis', 'Emerson', 'Finley', 'Harper', 'Jordan', 'Kai', 'Lee', 'Logan', 'Morgan', 'Parker', 'Reese', 'Rowan', 'Sage', 'Skyler', 'Taylor', 'Zion', 'Adrian', 'Blair', 'Cameron', 'Devon', 'Eli', 'Finn', 'Gale', 'Hayden', 'Indigo', 'Jamie', 'Jesse', 'Kendall', 'Kit', 'Micah', 'Nico', 'Phoenix', 'Remy', 'Riley', 'Sasha', 'Shay', 'Sidney', 'Spencer', 'Tate', 'Toby', 'Yael']
        names.remove(choice)
    
    return choice

def gen_random_sex() -> str:
    sexes = ['male', 'female']
    return random.choice(sexes)

def gen_death_probability(age: int) -> float:
    return 1 - math.exp(-age/100)

def get_random_probability() -> float:
    return random.random()