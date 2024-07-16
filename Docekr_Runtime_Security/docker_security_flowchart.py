import pydot

# Create a new directed graph
graph = pydot.Dot(graph_type='digraph', label='Docker Security with AppArmor')

# Define nodes (components)
nodes = [
    pydot.Node('A', label='User'),
    pydot.Node('B', label='Docker Daemon'),
    pydot.Node('C', label='AppArmor Service'),
    pydot.Node('D', label='Host System'),
    pydot.Node('E', label='Check Security Options'),
    pydot.Node('F', label='Load and Apply\nAppArmor Profile'),
    pydot.Node('G', label='Profile Application'),
    pydot.Node('H', label='AppArmor Enforcement'),
    pydot.Node('I', label='Container Init'),
    pydot.Node('J', label='Container Execution'),
    pydot.Node('K', label='Monitoring & Logging'),
    pydot.Node('L', label='Container Shutdown')
]

# Add nodes to the graph
for node in nodes:
    graph.add_node(node)

# Define edges (connections)
edges = [
    ('A', 'B'), ('B', 'E'), ('B', 'F'), ('B', 'C'), ('B', 'D'),
    ('C', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'I'), ('I', 'J'),
    ('J', 'K'), ('J', 'L')
]

# Add edges to the graph
for edge in edges:
    graph.add_edge(pydot.Edge(edge[0], edge[1]))

# Save the graph to a file and render it as PNG
graph.write_png('docker_security_flowchart_pydot.png')

print("Flowchart diagram generated successfully.")

