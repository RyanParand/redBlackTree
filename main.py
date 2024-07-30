from red_black_tree import RedBlackTree  # Import the Red-Black Tree implementation
from performance_analysis import measure_performance, plot_performance  # Import performance analysis functions
from visualization import visualize_tree  # Import visualization function

def main():
    # Test Red-Black Tree
    tree = RedBlackTree()  # Create a new Red-Black Tree
    tree.insert(10)  # Insert nodes
    tree.insert(20)
    tree.insert(30)
    print("In-order Traversal:", tree.in_order_traversal(tree.root))  # Perform in-order traversal and print the result

    # Performance Analysis
    sizes = [100, 1000, 10000, 100000]  # Different input sizes for performance analysis
    rb_tree_results = measure_performance(RedBlackTree, sizes)  # Measure performance of Red-Black Tree
    plot_performance(rb_tree_results, 'Red-Black Tree Performance')  # Plot the performance results

    # Visualization
    visualize_tree(tree)  # Visualize the tree

if __name__ == '__main__':
    main()  # Run the main function
