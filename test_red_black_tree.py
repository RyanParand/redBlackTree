import unittest
from red_black_tree import RedBlackTree

class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.tree = RedBlackTree()

    def test_insertion(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.assertEqual(self.tree.root.key, 20)
        self.assertEqual(self.tree.root.left.key, 10)
        self.assertEqual(self.tree.root.right.key, 30)
    
    def test_search(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.assertIsNotNone(self.tree.search(10))
        self.assertIsNotNone(self.tree.search(20))
        self.assertIsNotNone(self.tree.search(30))
        self.assertIsNone(self.tree.search(40))

    def test_in_order_traversal(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        result = self.tree.in_order_traversal(self.tree.root)
        self.assertEqual(result, [10, 20, 30])

if __name__ == '__main__':
    unittest.main()
