from entities.tree import FamilyTree

class Simulation:
    def __init__(self, family_tree: FamilyTree) -> None:
        self.tree = family_tree

    def year_tick(self):
        pass
