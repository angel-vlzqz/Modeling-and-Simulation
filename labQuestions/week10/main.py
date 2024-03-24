import os
import matplotlib.pyplot as plt

def create_filesystem_tree(root_path):
    tree = {}

    for dirpath, dirnames, filenames in os.walk(root_path):
        parent_node = os.path.basename(dirpath)
        tree[parent_node] = []

        for dirname in dirnames:
            tree[parent_node].append(dirname)

        for filename in filenames:
            tree[parent_node].append(filename)

    return tree

def print_filesystem_tree(tree, indent=0):
    for node, children in tree.items():
        print('  ' * indent + node)
        if children:
            print_filesystem_tree(children, indent + 1)

root_path = '/path/to/root/directory'
tree = create_filesystem_tree(root_path)
print_filesystem_tree(tree)

# Usage example
root_path = '/path/to/root/directory'
create_filesystem_tree(root_path)
