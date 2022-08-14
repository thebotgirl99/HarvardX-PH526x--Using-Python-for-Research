# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:23:12 2022

@author: HP
"""

import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np

def er_graph(N,p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for n1 in G.nodes():
        for n2 in G.nodes():
            if n1 < n2 and bernoulli.rvs(p=p):
                G.add_edge(n1,n2) 
    return G

def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree k")
    plt.ylabel("P(k)")
    plt.title("Degree Distribution")
    
def basic_net_stats(G):
    print(f"No. of nodes = {G.number_of_nodes()}")
    print(f"No. of edges = {G.number_of_edges()}")
    degree_sequence = [d for n, d in G.degree()]
    print(f"Avg degree = {np.mean(degree_sequence):.2f}")

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u", "v"])
G.add_edge(1,2)
G.add_edge("u", "v")
G.add_edges_from([(1,3), (1,4), (1,5), (1,6)])
G.add_edge("u", "w")
G.remove_node(2)
G.remove_nodes_from([4,5])
G.remove_edge(1,3)
G.remove_edges_from([(1,2), ("u","v")])
print(G.nodes())
print(G.edges())
print(G.number_of_nodes())
print(G.number_of_edges())

G = nx.karate_club_graph()
nx.draw(G, with_labels = True, node_color= "red", edge_color= "black")
print(G.number_of_nodes())
print(G.number_of_edges())
print(G.degree(33))
print(G.degree(0) is G.degree()[0]) #true

G1 = er_graph(100,0.08)
plot_degree_distribution(G1)
G2 = er_graph(100,0.08)
plot_degree_distribution(G2)
G3 = er_graph(500,0.08)
plot_degree_distribution(G3)

A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

G1_LCC = max((G1.subgraph(c) for c in nx.connected_components(G1)), key = len)
G2_LCC = max((G2.subgraph(c) for c in nx.connected_components(G2)), key = len)
print( G1_LCC.number_of_nodes() / G1.number_of_nodes() )
print( G2_LCC.number_of_nodes() / G2.number_of_nodes() )

plt.figure()
nx.draw(G1_LCC, node_size = 20, node_color = "red", edge_color = "gray")
plt.savefig("G1_LCC.pdf")

plt.figure()
nx.draw(G2_LCC, node_size = 20, node_color = "blue", edge_color = "gray")
plt.savefig("G2_LCC.pdf")

