import random
import math

def gen_random_name() -> str:
    names = ['Janet', 'Nancy', 'Greg', 'Brett', 'Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'George', 'Hannah', 'Isaac', 'Jessica', 'Kevin', 'Linda', 'Michael', 'Nathan', 'Olivia', 'Peter', 'Rachel', 'Samantha', 'Thomas', 'Vanessa', 'William', 'Xander', 'Yvonne', 'Zachary', 'Adam', 'Benjamin', 'Catherine', 'Daniel', 'Elizabeth', 'Fiona', 'Gabriel', 'Henry', 'Isabella', 'Jacob', 'Katherine', 'Lucy', 'Maggie', 'Nina', 'Oliver', 'Patrick', 'Quinn', 'Rebecca', 'Sophie', 'Trevor', 'Uma', 'Victoria', 'Wendy', 'Xavier', 'Yvette', 'Zoe']
    return random.choice(names)

def gen_random_sex() -> str:
    sexes = ['Male', 'Female']
    return random.choice(sexes)

def gen_death_probability(age: int) -> float:
    return 1 - math.exp(-(age/100)**2)
