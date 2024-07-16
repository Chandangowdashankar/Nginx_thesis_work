from graphviz import Digraph

# Create a new Digraph (directed graph)
dot = Digraph(comment='Docker Security with AppArmor')

# Define nodes (components)
dot.node('A', 'User')
dot.node('B', 'Docker Daemon')
dot.node('C', 'AppArmor Service')
dot.node('D', 'Host System')
dot.node('E', 'Check Security Options')
dot.node('F', 'Load and Apply\nAppArmor Profile')
dot.node('G', 'Profile Application')
dot.node('H', 'AppArmor Enforcement')
dot.node('I', 'Container Init')
dot.node('J', 'Container Execution')
dot.node('K', 'Monitoring & Logging')
dot.node('L', 'Container Shutdown')

# Define edges (connections)
dot.edges(['AB', 'BC', 'BD', 'BE', 'BF', 'CF', 'FG', 'GH', 'HI', 'IJ', 'JK', 'KL'])

# Save the Digraph to a file and render it as PNG
dot.format = 'png'
dot.render('docker_security_flowchart', view=True)

