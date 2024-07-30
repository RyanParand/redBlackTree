import networkx as nx  # Import NetworkX for graph visualization
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from red_black_tree import RedBlackTree  # Import the Red-Black Tree implementation

def visualize_tree(tree, filename="red_black_tree.png"):
    # Visualize the Red-Black Tree
    def add_edges(node, graph):
        # Add edges to the graph for the given node and its children
        if node != tree.NIL:
            if node.left != tree.NIL:
                graph.add_edge(node.key, node.left.key)  # Add edge from node to left child
                add_edges(node.left, graph)  # Recursively add edges for the left child
            if node.right != tree.NIL:
                graph.add_edge(node.key, node.right.key)  # Add edge from node to right child
                add_edges(node.right, graph)  # Recursively add edges for the right child

    graph = nx.DiGraph()  # Create a directed graph
    add_edges(tree.root, graph)  # Add edges from the tree to the graph
    pos = nx.spring_layout(graph)  # Compute layout positions for the nodes
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')  # Draw the graph
    plt.savefig(filename)  # Save the plot as an image
    print(f"Tree visualization saved as {filename}")

if __name__ == '__main__':
    tree = RedBlackTree()  # Create a new Red-Black Tree
    tree.insert(10)  # Insert nodes
    tree.insert(20)
    tree.insert(30)
    visualize_tree(tree)  # Visualize the tree
