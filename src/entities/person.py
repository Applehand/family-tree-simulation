from utils.utils import gen_random_name, gen_random_sex, gen_death_probability, get_random_probability

class Person:
    def __init__(self, name: str, age: int, sex: str):
        self.name = name or gen_random_name()
        self.age = age or 0
        self.sex = sex.lower() or gen_random_sex()
        self.sig_other = None
        self.spouse = None
        self.children = []
        self.parents = ()
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

    def have_child(self, father):
        if self.sex != 'female':
            raise ValueError('Only females can give birth.')

        child = Person()
        self.children.append(child)
        father.children.append(child)
        child.parents = (self, father)

        return child
    
    def have_birthday(self):
        self.age += 1
        self.mortality = gen_death_probability(self.age)
        if get_random_probability() < self.mortality:
            print(f'{self.name} has died.')
            self.is_alive = False
