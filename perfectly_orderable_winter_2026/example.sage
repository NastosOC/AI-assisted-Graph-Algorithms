# Simple graph: C4 w/ single edge tail
# This file was my first hands-on use of Sage to create and visualize graphs
# It demonstrates:
    # Constructing a basic graph (CycleGraph(4))
    # Adding a vertex and an edge to extend the structure
    # Assigning custom vertex labels and colours
    # Plotting the graph and saving to a PNG file
# Purpose: Familiarization with Sage's graph creation, modification, and plotting tools
# before building more complex enumeration scripts

# Constraints/Environmental Notes:
    # .show() is unreliable in this environment (VS Code + Sage) because it
        # requires and interactive Sage frontend
    # .save() is consistent and backend dependent
    # Vertex and edge colours must be provided as lists, not dictionaries
    # Sage automatically makes many standard objects available (graphs, digraphs, etc.)
        # so some variables appear as undefined or "false alarms" in VS Code
    # Sage auto generates a companion .py file for each .sage file
        # allowing the script to be run as standard Python if needed   

# Create C4
G = graphs.CycleGraph(4)
# Add tail
G.add_vertex(4)
G.add_edge(3, 4)

# Labels and (optional) Colours
labels = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
vertex_colors = ['skyblue','skyblue','skyblue','skyblue','orange']
edge_colors = ['red']

# Show graph
G.plot(vertex_labels=labels, vertex_color=vertex_colors, edge_colors=edge_colors, layout='spring').save('example.png')