from utils.utils import gen_random_name, gen_random_sex

class Person:
    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.spouse = None
        self.children = []
        self.parents = ()
        self.is_alive = True
        self.sex = sex or gen_random_sex()

    def get_married(self, spouse):
        self.spouse = spouse
        spouse.spouse = self

    def get_divorced(self, spouse):
        self.spouse = None
        spouse.spouse = None

    def have_child(self, father):
        child = Person(gen_random_name(), age=0)
        self.children.append(child)
        father.children.append(child)
        child.parents = (self, father)

        return child
    
    def have_birthday(self):
        self.age += 1

    def die(self):
        self.is_alive = False
    