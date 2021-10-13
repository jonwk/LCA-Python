import unittest
import LCA


class TestLCA(unittest.TestCase):

    def setUp(self):
        self.node1 = self.root = LCA.root = LCA.Node("a")
        self.node2 = self.root.left = LCA.Node("b")
        self.node3 = self.root.right = LCA.Node("c")
        self.node4 = self.node2.left = LCA.Node("d")
        self.node5 = self.node2.right = LCA.Node("e")

        self.node6 = self.node3.left = LCA.Node("f")
        self.node7 = self.node3.right = LCA.Node("g")

        self.node8 = self.node4.left = LCA.Node("h")
        self.node9 = self.node5.right = LCA.Node("i")

        self.node10 = self.node6.left = LCA.Node("j")
        self.node11 = self.node7.right = LCA.Node("k")

    def test_base1(self):
        self.assertTrue(LCA.findLCA("b", "c"), "a")
        self.assertTrue(LCA.findLCA("d", "e"), "b")
        self.assertTrue(LCA.findLCA("f", "g"), "c")

    def test_base2(self):
        self.assertTrue(LCA.findLCA("h", "i"), "b")
        self.assertTrue(LCA.findLCA("j", "k"), "c")
        self.assertTrue(LCA.findLCA("h", "j"), "a")
        self.assertTrue(LCA.findLCA("i", "k"), "a")

    def test_complex(self):
        self.assertTrue(LCA.findLCA("h", "e"), "b")
        self.assertTrue(LCA.findLCA("d", "i"), "b")
        self.assertTrue(LCA.findLCA("f", "k"), "c")
        self.assertTrue(LCA.findLCA("j", "g"), "c")

        self.assertTrue(LCA.findLCA("b", "g"), "a")
        self.assertTrue(LCA.findLCA("c", "h"), "a")

    def test_itself(self):
        self.assertTrue(LCA.findLCA("b", "d"), "b")
        self.assertTrue(LCA.findLCA("b", "e"), "b")
        self.assertTrue(LCA.findLCA("b", "h"), "b")

        self.assertTrue(LCA.findLCA("c", "g"), "c")
        self.assertTrue(LCA.findLCA("c", "f"), "c")
        self.assertTrue(LCA.findLCA("c", "k"), "c")

        self.assertTrue(LCA.findLCA("a", "b"), "a")
        self.assertTrue(LCA.findLCA("a", "c"), "a")

    def test_same_node(self):
        self.assertTrue(LCA.findLCA("a", "a"), "a")
        self.assertTrue(LCA.findLCA("b", "b"), "b")
        self.assertTrue(LCA.findLCA("c", "c"), "c")
        self.assertTrue(LCA.findLCA("d", "d"), "d")

    def test_invalid(self):
        self.assertTrue(LCA.findLCA("l", "d"), "Error")
        self.assertTrue(LCA.findLCA("l", "z"), "Error")

    def test_empty(self):
        self.assertTrue(LCA.findLCA(" ", "a"), "Error")
        self.assertTrue(LCA.findLCA(" ", " "), "Error")
        self.assertTrue(LCA.findLCA("", ""), "Error")

    def test_numbers(self):
        self.node1 = self.root = LCA.root = LCA.Node(1)
        self.node2 = self.root.left = LCA.Node(2)
        self.node3 = self.root.right = LCA.Node(3)
        self.node4 = self.node2.left = LCA.Node(4)
        self.node5 = self.node2.right = LCA.Node(5)

        self.node6 = self.node3.left = LCA.Node(6)
        self.node7 = self.node3.right = LCA.Node(7)

        self.node8 = self.node4.left = LCA.Node(8)
        self.node9 = self.node5.right = LCA.Node(9)

        self.node10 = self.node6.left = LCA.Node(10)
        self.node11 = self.node7.right = LCA.Node(11)

        #           1
        #       /       \
        #     2          3
        #    /  \       /  \
        #   4    5     6    7
        #  /      \   /      \
        #  8       9 10       11

        self.assertTrue(LCA.findLCA(2, 3), 1)
        self.assertTrue(LCA.findLCA(4, 5), 2)
        self.assertTrue(LCA.findLCA(6, 7), 3)


if __name__ == '__main__':
    unittest.main()
