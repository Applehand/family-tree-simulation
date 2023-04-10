from src.entities.person import Person
import networkx as nx
import matplotlib.pyplot as plt
from json import dumps

class FamilyTree():

    def __init__(self, dynasty_name: str, matriarch: Person, patriarch: Person):
        self.graph = nx.MultiGraph(name=dynasty_name)
        self.name = dynasty_name
        self.members = []
        matriarch.spouse = patriarch
        patriarch.spouse = matriarch
        self.graph.add_edge(matriarch, patriarch, relationship='Spouse')

    def add_member(self, member):
        self.graph.add_node(member)
        self.members.append(member)

        self.graph.add_edge(member, member.parents[0], relationship="Parent/Child")
        self.graph.add_edge(member, member.parents[1], relationship="Parent/Child")
        
        for sibling in member.parents[0].children:
            if sibling == member:
                continue
            self.graph.add_edge(member, sibling, relationship="Sibling")
        

    def remove_member(self, member):
        self.graph.remove_node(member)
        self.members.remove(member)

    def draw_graph(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()

    def get_tree_json(self):
        nodes = []
        edges = []

        tree_dict = {
            "nodes": nodes,
            "edges": edges
        }

        for node in self.graph.nodes:
            nodes.append({
                "name": node.name,
                "age": node.age,
                "sex": node.sex,
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
