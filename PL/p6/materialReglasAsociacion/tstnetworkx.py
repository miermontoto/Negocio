import matplotlib.pyplot as plt
import networkx as nx

# Sample rules represented as a list of (antecedent, consequent) pairs.
rules = [
    (frozenset(["Bread"]), frozenset(["Butter"])),
    (frozenset(["Milk"]), frozenset(["Cookies"])),
    (frozenset(["Bread", "Milk"]), frozenset(["Butter"]))
]

# Create a new directed graph
G = nx.DiGraph()

# Add nodes and edges for each rule
for rule in rules:
    antecedent = ', '.join(list(rule[0]))
    consequent = ', '.join(list(rule[1]))
    G.add_edge(antecedent, consequent)

# Draw the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 5))

nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=15, width=2, edge_color='gray')

plt.title("Association Rules")
plt.show()
