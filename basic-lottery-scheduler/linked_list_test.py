import unittest

from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    def test_empty(self):
        linkedlist = LinkedList()

        self.assertEqual(linkedlist.empty(), True)

    def test_methods(self):
        linkedlist = LinkedList()

        minval = 1
        maxval = 5

        for i in range(minval, maxval + 1):
            linkedlist.insert(i)

        self.assertEqual(list(linkedlist), [1, 2, 3, 4, 5])

        for i in range(minval, maxval + 1):
            linkedlist.remove(i)
        
        self.assertEqual(list(linkedlist), [])

    def test_remove(self):
        linkedlist = LinkedList()

        minval = 1
        maxval = 5

        for i in range(minval, maxval + 1):
            linkedlist.insert(i)

        linkedlist.remove(3)
        self.assertEqual(list(linkedlist), [1, 2, 4, 5])

        linkedlist.remove(1)
        self.assertEqual(list(linkedlist), [2, 4, 5])

        linkedlist.remove(5)
        self.assertEqual(list(linkedlist), [2, 4])

    def test_remove_by_key(self):
        linkedlist = LinkedList()

        for pair in [('A', 1), ('B', 2), ('C', 3)]:
            linkedlist.insert(pair)
        
        linkedlist.remove_by_key(lambda x: x[0], 'B')
        self.assertEqual(list(linkedlist), [('A', 1), ('C', 3)])

        linkedlist.remove_by_key(lambda x: x[0], 'A')
        self.assertEqual(list(linkedlist), [('C', 3)])

        linkedlist.remove_by_key(lambda x: x[0], 'C')
        self.assertEqual(list(linkedlist), [])

if __name__ == '__main__':
    unittest.main()