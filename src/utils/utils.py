import random
import math
from src.sim_data.person_data import names_list


def gen_random_name() -> str:
    choice = random.choice(names_list)
    return choice

def gen_random_sex() -> str:
    sexes = ['male', 'female']
    return random.choice(sexes)

def gen_death_probability(age: int) -> float:
    return 1 - math.exp(-age/100)

def get_random_probability() -> float:
    return random.random()

print(gen_random_name())
