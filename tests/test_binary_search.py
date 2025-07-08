import unittest
from Ejemplos_Curso import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search(arr, 7), 3)
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 11), 5)
    
    def test_not_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search(arr, 4), -1)
        self.assertEqual(binary_search(arr, 0), -1)
        self.assertEqual(binary_search(arr, 12), -1)
    
    def test_empty(self):
        arr = []
        self.assertEqual(binary_search(arr, 1), -1)

if __name__ == "__main__":
    unittest.main()
