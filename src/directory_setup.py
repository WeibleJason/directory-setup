from directory_node import DirectoryNode

def print_directory_structure(node: DirectoryNode):
    print("\n")
    node.print()

root = DirectoryNode(None, "root")
root.add_subdirectory(DirectoryNode(root,"child1"))
root.add_subdirectory(DirectoryNode(root,"child2"))
root.subdirectories[0].add_subdirectory(DirectoryNode(root.subdirectories[0],"grandchild1"))
root.subdirectories[1].add_subdirectory(DirectoryNode(root.subdirectories[1],"grandchild2"))
print_directory_structure(root)