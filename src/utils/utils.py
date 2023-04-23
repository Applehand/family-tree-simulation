import random
import math
import datetime
from src.data.person_data import names_list


def gen_random_name() -> str:
    return random.choice(names_list)

def gen_random_sex() -> str:
    return random.choice(['male', 'female'])

def gen_death_probability(age: int) -> float:
    return 1 - math.exp(-age/100)

def get_random_probability() -> float:
    return random.random()

def gen_random_birthday(age: int) -> datetime.date:
    current_year = datetime.date.today().year
    year_of_birth = current_year - age
    
    start_date = datetime.date(year_of_birth, 1, 1)
    end_date = datetime.date(year_of_birth, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    
    return random_date