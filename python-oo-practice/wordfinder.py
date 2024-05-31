"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    def __init__(self, path):
        self.path = path
        self.words = []
        self.get_words()
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        return [word.strip() for word in dict_file]
    
    def random(self):
        return random.choice(self.words)
    
    class SpecialWordFinder:
        def __init__(self, path):
            self.path = path
            self.words = []
            self.get_words()
            print(f"{len(self.words)} words read")
        
        def parse(self, dict_file):
            return [word.strip() for word in dict_file if word.strip() and not word.startswith("#")]
        
        def random(self):
            return random.choice(self.words)
        
    ...
