# To run: python3 -m unittest tests/test_directory_node.py

import unittest

from directory_node import DirectoryNode

class TestDirectoryNode(unittest.TestCase):

    def setUp(self):
        self.root = DirectoryNode(None, "root")

    def test_root(self):
        """test that self.root is instance of DirectoryNode"""
        self.assertIsInstance(self.root, DirectoryNode)

    def test_root_parent(self):
        """test that self.root.parent is None"""
        self.assertIsNone(self.root.parent)

    def test_root_name(self):
        """test that self.root.name is 'root'"""
        self.assertEquals(self.root.name, "root")

    def test_empty_subdirectories(self):
        """test that self.root has no children"""
        self.assertEqual(self.root.subdirectories, set())

    def test_add_one_subdirecotry(self):
        """
            test adding child to self.root
            should update parent of child
        """
        child = DirectoryNode(None, "child")
        self.root.add_subdirectory(child)
        self.assertEqual(self.root.subdirectories, {child})
        self.assertEqual(self.root, child.parent)



if __name__ == "__main__":
    unittest.main()