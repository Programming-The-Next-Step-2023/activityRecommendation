import unittest
import activity_rec

class TestRec(unittest.TestCase):

    def test_rec(self):
        self.assertEqual(activity_rec.activity_rec(1, 1, 'Yes', 'Sunny', 'Warm'), 'Sit in the sun')
        # when cloudy and cold -> inside
        self.assertEqual(activity_rec.activity_rec(1, 3, 'No', 'Cloudy', 'Cold'), 'Reading')
        # when rainy (cold and warm) -> inside
        self.assertEqual(activity_rec.activity_rec(1, 3, 'No', 'Rainy', 'Warm'), 'Reading')

if __name__ == '__main__':
    unittest.main()