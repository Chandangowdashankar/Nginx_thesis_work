import matplotlib.pyplot as plt

# Define the components and actions in the flow diagram
components = [
    "User", "Docker Daemon", "AppArmor Service", "Host System",
    "Check Security Options", "Load and Apply AppArmor Profile", 
    "Profile Application", "AppArmor Enforcement", 
    "Container Init", "Container Execution", 
    "Monitoring & Logging", "Container Shutdown"
]

# Define the connections between components
connections = [
    ("User", "Docker Daemon"),
    ("Docker Daemon", "Check Security Options"),
    ("Docker Daemon", "Load and Apply AppArmor Profile"),
    ("AppArmor Service", "Load and Apply AppArmor Profile"),
    ("Load and Apply AppArmor Profile", "Profile Application"),
    ("Profile Application", "AppArmor Enforcement"),
    ("AppArmor Enforcement", "Container Init"),
    ("Container Init", "Container Execution"),
    ("Container Execution", "Monitoring & Logging"),
    ("Monitoring & Logging", "Container Shutdown"),
]

# Create a plot
fig, ax = plt.subplots(figsize=(10, 8))

# Draw nodes
for component in components:
    ax.annotate(component, xy=(components.index(component) % 2, -components.index(component) // 2),
                xycoords='axes fraction', ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.5', fc='lightblue', alpha=0.5))

# Draw edges
for connection in connections:
    ax.annotate("", xy=(components.index(connection[0]) % 2, -components.index(connection[0]) // 2),
                xycoords='axes fraction', xytext=(components.index(connection[1]) % 2, -components.index(connection[1]) // 2),
                textcoords='axes fraction',
                arrowprops=dict(arrowstyle="->", color="black"))

# Remove axes
ax.axis('off')

# Set title
plt.title("Flow Diagram for Docker Security with AppArmor", fontsize=14)

# Show plot
plt.show()

