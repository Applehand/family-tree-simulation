import random
import math
from src.data.person_data import names_list


def gen_random_name() -> str:
    return random.choice(names_list)

def gen_random_sex() -> str:
    return random.choice(['male', 'female'])

def gen_death_probability(age: int) -> float:
    return 1 - math.exp(-age/100)

def get_random_probability() -> float:
    return random.random()
