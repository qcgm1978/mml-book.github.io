import unittest,re
# from utilities import getPath,parseNumber,update_json
from .Introduction_Motivation import IntroMotiv
class TDD_INTRODUCTION_MOTIVATION(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1
    def test_Introduction_Motivation(self):
        i=IntroMotiv()
        self.assertEqual(i.core, ('data', 'model', 'learning'))
        self.assertEqual(i.process_generate,['learn from data', 'generalize well to yet unseen data', 'find patterns and structure in data'])
        self.assertEqual(i.math_for,['creating new machine learning solutions','understanding and debugging existing approaches','learning about the inherent assumptions and limitations of the methodologies'])
        self.assertEqual(i.algorithm_senses['predictors'],'makes predictions based on input data')
        self.assertEqual(i.vector_view,['computer science','physics','mathematical'])
        self.assertEqual(i.foundations['Regression'][0],'Vector Calculus')
        self.assertRaises(AttributeError,lambda:i.__paraphrase)
if __name__ == '__main__':
    unittest.main()
                