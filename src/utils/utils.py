import random
import math
import datetime
import requests

def get_random_name(sex) -> str:
    if sex == 'male':
        response = requests.get('https://names.drycodes.com/1?nameOptions=boy_names')
        response_content = str(response.content[2:-1], 'utf-8')
        name = response_content.split('_')[0]

        return name
    
    if sex == 'female':
        response = requests.get('https://names.drycodes.com/1?nameOptions=girl_names')
        response_content = str(response.content[2:-1], 'utf-8')
        name = response_content.split('_')[0]

        return name

def get_random_sex() -> str:
    return random.choice(['male', 'female'])

def get_death_probability(age: int) -> float:
    chance = 1 - math.exp(-age/100)
    print(f'Death prob: {chance}')
    return chance

def get_random_probability() -> float:
    chance = random.random()
    print(f'Random chance: {chance}')
    return chance

def get_random_birthday(age: int) -> datetime.date:
    current_year = datetime.date.today().year
    year_of_birth = current_year - age
    
    start_date = datetime.date(year_of_birth, 1, 1)
    end_date = datetime.date(year_of_birth, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    
    return random_date

def get_random_member(members):
    return random.choice(members)

def is_birthday_today(current_date, birthday):
    return (current_date.month, current_date.day) == (birthday.month, birthday.day)

def get_random_adoption_age():
    return random.randint(0, 16)

def get_random_partner_age(member_age):
    min_age = max(17, member_age - 6)
    max_age = member_age + 6
    return random.randint(min_age, max_age)

def get_random_friendship_age(member_age):
    min_age = max(3, member_age - 15)
    max_age = member_age + 15
    return random.randint(min_age, max_age)

def get_fertility_chance(age):
    chance = max(0, min(1, -0.0008*age**2 + 0.056*age - 0.3))
    print(f'Fertility chance: {chance}')
    return chance
