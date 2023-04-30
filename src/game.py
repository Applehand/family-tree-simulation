from src.entities.network import SocialNetwork
from src.entities.person import Person
from src.managers.simulation import Simulation

def test():
    network = SocialNetwork('Applehans', Person(age=22, sex='male'), Person(age=19, sex='female'))
    sim = Simulation(network)

    sim.begin_simulation()