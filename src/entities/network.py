from src.entities.person import Person
from src.utils.utils import get_random_member, is_birthday_today, get_random_adoption_age, get_random_partner_age, get_random_friendship_age
import networkx as nx
import matplotlib.pyplot as plt
from json import dumps

class SocialNetwork():

    def __init__(self, network_name: str, foremother: Person, forefather: Person):
        self.graph = nx.DiGraph(name=network_name)
        self.name = network_name
        self.all_members, self.alive_members, self.dead_members, self.associated_members = [], [], [], []
        foremother.spouse = forefather
        forefather.spouse = foremother
        self.graph.add_edge(foremother, forefather, relationship='spouse')
        self.all_members.extend([forefather, foremother])
        self.alive_members.extend([forefather, foremother])

    def add_member(self, current_member, new_member_relationship, secondary_member=None):

        def add_adoption(current_member: Person, second_parent=None):
            adopted_child = Person(age=get_random_adoption_age())
            current_member.adopt_child(adopted_child, second_parent)
            self.all_members.append(adopted_child)
            self.alive_members.append(adopted_child)
            self.graph.add_edge(current_member, adopted_child, relationship='adopted parent/child')
            if second_parent:
                self.graph.add_edge(second_parent, adopted_child, relationship='adopted parent/child')

            return adopted_child

        def add_child(current_member: Person, father: Person):
            child = current_member.have_child_with(father)
            self.all_members.append(child)
            self.alive_members.append(child)
            self.graph.add_edge(current_member, child, relationship='parent/child')
            self.graph.add_edge(father, child, relationship='parent/child')

            return child

        def add_partner(current_member: Person, partner=None):
            if not partner:
                partner = Person(age=get_random_partner_age(current_member.age))
                print(f'{partner.name} was created for {current_member.name}')
            current_member.establish_relationship(partner)
            self.all_members.append(partner)
            self.alive_members.append(partner)
            self.associated_members.append(partner)
            self.graph.add_edge(current_member, partner, relationship='partner')

            return partner

        def add_friendship(current_member: Person, friend=None):
            if not friend:
                friend = Person(age=get_random_friendship_age(current_member.age))
            current_member.meet_friend(friend)
            self.all_members.append(friend)
            self.alive_members.append(friend)
            self.associated_members.append(friend)
            self.graph.add_edge(current_member, friend, relationship='friendship')

            return friend

        relationship_functions = {
            'adoption': add_adoption,
            'child': add_child,
            'partner': add_partner,
            'friendship': add_friendship
        }

        if secondary_member:
            relationship_functions[new_member_relationship](current_member, secondary_member)
        else:
            relationship_functions[new_member_relationship](current_member)

    def remove_member(self, member: Person, removal_reason):
        if removal_reason == 'death':
            member.has_died()
            self.dead_members.append(member)
            self.alive_members.remove(member)

        if removal_reason == 'breakup':
            pass

        if removal_reason == 'divorce':
            pass

    def draw_graph(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()

    def update_random_member(self, current_date):
        if self.alive_members:
            chosen_member: Person = get_random_member(self.alive_members)

            # if chosen_member.mortality_check():
            #     self.remove_member(chosen_member, 'death')

            if chosen_member.pregnancy_check():
                if not chosen_member.spouse and not chosen_member.partner:
                    partner = self.add_member(chosen_member, 'partner')
                    self.add_member(chosen_member, 'child', partner)
                else:
                    self.add_member(chosen_member, 'child', chosen_member.partner or chosen_member.spouse)
            
            males = 0
            females = 0
            for member in self.alive_members:
                if member.sex == 'male':
                    males += 1
                elif member.sex == 'female':
                    females += 1

            print(f'Males: {males}')
            print(f'Females: {females}')

        else:
            print('Everyone is dead.')




    def check_for_birthdays(self, current_date):
        for member in self.all_members:
            if is_birthday_today(current_date, member.birthday):
                print(f"{member.name} has a birthday today!")
                member.age_up()

    def get_tree_json(self):
        nodes = []
        edges = []

        tree_dict = {
            "nodes": nodes,
            "edges": edges
        }

        for node in self.graph.nodes:
            nodes.append({
                "age": node.age,
                "sex": node.sex,
                "name": node.name,
                "birthday": node.birthday,
                "sig_other": node.sig_other.name if node.sig_other else None,
                "spouse": node.spouse.name if node.spouse else None,
                "ex_spouses": [ex_spouse.name for ex_spouse in node.ex_spouses],
                "children": [child.name for child in node.children],
                "parents": [parent.name for parent in node.parents],
                "is_alive": node.is_alive,
                "mortality": node.mortality
            })

        for edge in self.graph.edges:
            edges.append({
                "source": edge[0].name, 
                "target": edge[1].name,
                "relationship": self.graph.get_edge_data(edge[0], edge[1])[0]['relationship']
            })

        return dumps(tree_dict)
