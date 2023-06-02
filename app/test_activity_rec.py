import unittest
import pandas as pd
from app import activity_rec

class TestRec(unittest.TestCase):

    def test_rec(self):
        url = "https://raw.githubusercontent.com/Programming-The-Next-Step-2023/activityRecommendation/main/activities.csv"
        df = pd.read_csv(url, sep=";", encoding="ISO-8859-1")

        # Test case 1: Matching activity outside
        self.assertEqual(activity_rec(1, 3, 1, 'Yes', 'Sunny', 'Warm', df),
                         'Go for a walk')
        # Test case 2: Matching activity inside
        self.assertEqual(activity_rec(1, 3, 4, 'Yes', 'Rainy', 'Warm', df),
                         'Meet up with friends')
        # Test case 3: No matching activity
        self.assertEqual(activity_rec(1, 1, 5, 'Yes', 'Rainy', 'Warm', df),
                         'Error: No activities match your state')


if __name__ == '__main__':
    unittest.main()