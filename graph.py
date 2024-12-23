from graphviz import Digraph

def create_colored_system_design_diagram():
    # Create a new directed graph
    dot = Digraph(comment='Vehicle Detection System')

    # Define graph attributes for style
    dot.attr('node', shape='rectangle', style='filled', color='lightgrey', fontname='Helvetica')

    # Add nodes with colors
    dot.node('A', 'Camera Module', fillcolor='lightblue')
    dot.node('B', 'YOLOv8 Model', fillcolor='lightgreen')
    dot.node('C', 'Processing Unit', fillcolor='lightpink')
    dot.node('D', 'Traffic Analysis Dashboard', fillcolor='lightyellow')
    dot.node('E', 'Network Connection', fillcolor='lightcoral')
    dot.node('F', 'Power Supply', fillcolor='lightgray')

    # Add edges to represent the workflow
    dot.edge('A', 'B', 'Video Feed', color='black')
    dot.edge('B', 'C', 'Vehicle Detection', color='black')
    dot.edge('C', 'D', 'Data Analysis', color='black')
    dot.edge('D', 'E', 'Remote Access', color='black')
    dot.edge('F', 'A', 'Power', color='black')
    dot.edge('F', 'C', 'Power', color='black')

    # Save the diagram
    dot.render('colored_vehicle_detection_system', format='png', cleanup=True)
    print("System design diagram created as 'colored_vehicle_detection_system.png'.")

# Generate the colored system design diagram
create_colored_system_design_diagram()
