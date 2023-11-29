import seaborn as sns
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
titanic = sns.load_dataset('titanic')

# Preprocess: For simplicity, let's select a few columns and convert them to string type
titanic = titanic[['class', 'sex', 'alive']]
titanic = titanic.astype(str)

# One-hot encode the data
titanic_encoded = pd.get_dummies(titanic)


# Find frequent itemsets
frequent_itemsets = apriori(titanic_encoded, min_support=0.1, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.5)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for _, rule in rules.iterrows():
    G.add_edge(', '.join(rule['antecedents']), ', '.join(rule['consequents']), weight=rule['lift'])

# Visualize the graph
plt.figure(figsize=(12, 6))
pos = nx.spring_layout(G, seed=22)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, edge_color='gray', width=[G[u][v]['weight'] for u, v in G.edges()])

plt.title("Association Rules from Titanic Dataset")
plt.show()
