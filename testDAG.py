from DAG import DAG
import unittest


class MyTestCase(unittest.TestCase):

    # test for add one node
    def test_addNode(self):
        DAG1 = DAG()
        DAG1.addNode('Z')
        DAG1.printDAG(DAG1.graph)
        self.assertTrue(DAG1.graph == {'Z': []})

    # test for a non-existent node
    def test_addNode2(self):
        DAG2 = DAG()
        DAG2.addNode('X')
        self.assertFalse(DAG2.graph == {'Z': []})

    # test for a non-existent node just after init
    def test_addNode3(self):
        DAG3 = DAG()
        self.assertFalse(DAG3.addNode('Z'))

    # further testing addNode Function
    def test_addNode4(self):
        DAG4 = DAG()
        self.assertFalse(DAG4.addNode('Z'))
        self.assertFalse(DAG4.addNode('X'))
        self.assertFalse(DAG4.addNode('Y'))
        self.assertFalse(DAG4.addNode('1'))
        self.assertFalse(DAG4.addNode('2'))
        self.assertFalse(DAG4.addNode('3'))


if __name__ == '__main__':
    unittest.main()
