import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_e2f_not_none(self):
        with self.assertRaises(ValueError) as context:
            english_to_french(None)
        self.assertEqual(str(context.exception),\
'english_text must be a string')

    def test_e2f_works(self):
        self.assertEqual(english_to_french('Hello'),\
'{\n  "translations": [\n    {\n      "translation": "Bonjour"\n    }\
\n  ],\n  "word_count": 1,\n  "character_count": 5\n}')
        self.assertEqual(english_to_french(['Hello', 'World']),\
'{\n  "translations": [\n    {\n      "translation": "Bonjour"\n    },\
\n    {\n      "translation": "Monde"\n    }\n  ],\n  "word_count": 2,\
\n  "character_count": 10\n}')

class TestFrenchToEnglish(unittest.TestCase):
    def test_f2e_not_none(self):
        with self.assertRaises(ValueError) as context:
            french_to_english(None)
        self.assertEqual(str(context.exception),\
'french_text must be a string')

    def test_f2e_works(self):
        self.assertEqual(french_to_english('Bonjour'),\
 '{\n  "translations": [\n    {\n      "translation": "Hello"\n    }\
\n  ],\n  "word_count": 1,\n  "character_count": 7\n}')
        self.assertEqual(french_to_english(['Bonjour', 'Monde']),\
'{\n  "translations": [\n    {\n      "translation": "Hello"\n    },\
\n    {\n      "translation": "World"\n    }\n  ],\n  "word_count": 2,\
\n  "character_count": 12\n}')


unittest.main()



