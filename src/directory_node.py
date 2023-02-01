from __future__ import annotations

class DirectoryNode:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.subdirectories = list()

    def set_parent(self, parent):
        """Sets the parent of self"""
        self.parent = parent

    def set_name(self, name):
        """Sets the name of self"""
        self.name = name

    def add_subdirectory(self, node: DirectoryNode):
        """Add node to children of self"""
        assert node is not self, "node should not point to itself"
        node.parent = self
        self.subdirectories.append(node)

    def print(self, level=0):
        """
            recursively print the node along with its children
            https://stackoverflow.com/questions/30521991/python-recursively-printing-a-tree-from-a-list-structure
        """
        print('-' * (level-1) + '|-' * (level > 0) + self.name)
        for child in self.subdirectories:
            child.print(level+1)