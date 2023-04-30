from src.utils.utils import get_random_name, get_random_sex, get_death_probability, get_random_birthday, get_random_probability, get_fertility_chance
from json import dumps

class Person:

    def __init__(self, name=None, age=0, sex=None):
        self.age = age
        self.sex = sex or get_random_sex()
        self.name = name or get_random_name(self.sex)
        self.birthday = get_random_birthday(age)
        self.partner = None
        self.spouse = None
        self.ex_spouses = []
        self.children = []
        self.parents = ()
        self.relationships = {}
        self.is_alive = True
        self.mortality = get_death_probability(self.age)

    def establish_relationship(self, other, tree):
        self.partner = other
        other.sig_other = self

    def meet_friend(self, friend):
        print(f'Made friends with {friend.name}')

    def break_up(self, other):
        self.partner = None
        other.partner = None

    def get_married(self, spouse):
        self.spouse = spouse
        spouse.spouse = self

    def get_divorced(self, spouse):
        self.spouse = None
        spouse.spouse = None
        self.ex_spouses.append(spouse)
        spouse.ex_spouses.append(self)

    def adopt_child(self, child, second_parent):
        if second_parent:
            child.parents = (self, second_parent)
            self.children.append(child)
            second_parent.children.append(child)
        else:
            self.children.append(child)
            child.parents = (self,)


    def have_child_with(self, father):
        child = Person()
        self.children.append(child)
        father.children.append(child)
        child.parents = (self, father)
        print(f'{child.name} has been born.')

        return child
    
    def age_up(self):
        self.age += 1

    def pregnancy_check(self):
        if self.sex != 'female':
            return False
        else:
            return get_random_probability() < get_fertility_chance(self.age)

    def mortality_check(self):
        return get_random_probability() < get_death_probability(self.age)

    def has_died(self):
        print(f'{self.name} has died.')
        self.is_alive = False

    def get_person_json(self):
        person_dict = {
            "age": self.age,
            "sex": self.sex,
            "name": self.name,
            "birthday": self.birthday,
            "partner": self.partner,
            "spouse": self.spouse,
            "ex-spouses": self.ex_spouses,
            "children": [child.name for child in self.children],
            "parents": [parent.name for parent in self.parents],
            "relationships": self.relationships,
            "is_alive": self.is_alive,
            "mortality": self.mortality
        }
        
        return dumps(person_dict)
    