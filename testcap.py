'''
testcap.py
'''

import unittest
import cap

class TestCap(unittest.TestCase):

    '''
    The last test should fail because the capitalize function just capitalizes the first letter fo the string, not each word in the string.
    '''

    def test_one_word (self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_sentence (self):
        text = 'python is cool'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python is cool')

    def test_title_case (self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()
