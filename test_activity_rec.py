import unittest
import activity_rec

class TestRec(unittest.TestCase):

    def test_rec(self):
        result = activity_rec.activity_rec(1, 1, 'Sunny', 'Yes')
        self.assertEquals(result, 'Activity is: Sit in the sun')

if __name__ == '__main__':
    unittest.main()