import sys
import unittest

sys.path.insert(0, '..')
# from card import *
from cardA import *

class CardTest(unittest.TestCase):
    def testConstructor(self):
        c1 = Card(1, 'c')
        c2 = Card(6, 'd')
        c3 = Card(10, 'h')
        c4 = Card(13, 's')
        self.assertEqual(str(c1), 'Ace of Clubs')
        self.assertEqual(str(c2), 'Six of Diamonds')
        self.assertEqual(str(c3), 'Ten of Hearts')
        self.assertEqual(str(c4), 'King of Spades')

def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)