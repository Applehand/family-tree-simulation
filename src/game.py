from src.entities.tree import FamilyTree
from src.entities.person import Person

Ava = Person('Ava', 18, 'female')
Bob = Person('Bob', 18, 'male')

tree = FamilyTree('Applehans', Bob, Ava)

for i in range(3):
    tree.add_member(Ava.have_child_with(Bob))

data = tree.get_tree_json()

print(data)