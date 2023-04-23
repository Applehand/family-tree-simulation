from src.utils.utils import gen_random_name, gen_random_sex, gen_death_probability, get_random_probability, gen_random_birthday
from json import dumps

class Person:

    def __init__(self, name=None, age=0, sex=None):
        self.name = name or gen_random_name()
        self.age = age
        self.sex = sex or gen_random_sex()
        self.birthday = gen_random_birthday(age)
        self.sig_other = None
        self.spouse = None
        self.ex_spouses = []
        self.children = []
        self.parents = ()
        self.relationships = {}
        self.is_alive = True
        self.mortality = gen_death_probability(self.age)

    def establish_relationship(self, other):
        self.sig_other = other
        other.sig_other = self

    def break_up(self, other):
        self.sig_other = None
        other.sig_other = None

    def get_married(self, spouse):
        self.spouse = spouse
        spouse.spouse = self

    def get_divorced(self, spouse):
        self.spouse = None
        spouse.spouse = None

    def have_child_with(self, father):
        if self.sex != 'female':
            raise ValueError('Only females can give birth.')

        child = Person()
        self.children.append(child)
        father.children.append(child)
        child.parents = (self, father)

        return child
    
    def age_up(self):
        self.age += 1
        self.mortality = gen_death_probability(self.age)
        if get_random_probability() < self.mortality:
            print(f'{self.name} has died.')
            self.is_alive = False

    def get_person_json(self):
        person_dict = {
            "name": self.name,
            "age": self.age,
            "sex": self.sex,
            "birthday": self.birthday,
            "sig_other": self.sig_other,
            "spouse": self.spouse,
            "ex-spouses": self.ex_spouses,
            "children": [child.name for child in self.children],
            "parents": [parent.name for parent in self.parents],
            "relationships": self.relationships,
            "is_alive": self.is_alive,
            "mortality": self.mortality
        }
        
        return dumps(person_dict)