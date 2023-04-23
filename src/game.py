from src.entities.tree import FamilyTree
from src.entities.person import Person
from src.managers.simulation import Simulation


def test():
    Ava = Person('Ava', 18, 'female')
    Bob = Person('Bob', 18, 'male')

    tree = FamilyTree('Applehans', Ava, Bob)

    sim = Simulation(tree)

    sim.begin_simulation()