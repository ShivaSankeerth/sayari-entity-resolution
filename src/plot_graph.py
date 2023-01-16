import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json, re

def preprocess_name(name):
    return re.sub('[!@#$.-]', '', name.split('\n')[0]).upper().strip()

def create_graph(data):
    business_graph = nx.Graph()
    nodes, edges = set(), set()
    for key, value in data.items():
        business_name = preprocess_name(value['Business Name'])
        for category in ['Owner','Registered Agent','Commercial Registered Agent']:
            if category in value:
                category_person = preprocess_name(value[category])
                nodes.add((category_person, category))
                edges.add(((category_person, category), (business_name, 'Business Name')))
    
    business_graph.add_nodes_from(nodes)
    business_graph.add_edges_from(edges)
    return business_graph

def draw_graph(G):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(20, 20))
    connected_components = (G.subgraph(c) for c in nx.connected_components(G))
    cm = {
        'Business Name': 'mediumseagreen',
        'Commercial Registered Agent': 'salmon',
        'Registered Agent': 'orchid',
        'Owner': 'slateblue'
    }
    legend_handles = [mpatches.Patch(color=cm['Business Name'], label='Business Name'),
                      mpatches.Patch(color=cm['Owner'], label='Owner'),
                      mpatches.Patch(color=cm['Registered Agent'], label='Registered Agent'),
                      mpatches.Patch(color=cm['Commercial Registered Agent'], label='Commercial Registered Agent')]
    for graph in connected_components:
        colormap = [cm[node[1]] for node in graph.nodes]
        nx.draw(graph,pos=pos,node_size=40,node_color=colormap,with_labels=False)
    plt.legend(handles=legend_handles)
    plt.title('Businesses Starting with X that are Active in North Dakota')
    plt.savefig('output/plot.png')

if __name__ == '__main__':
    with open('x_business.json', 'r') as f:
        data = json.load(f)
    G = create_graph(data)
    draw_graph(G)


