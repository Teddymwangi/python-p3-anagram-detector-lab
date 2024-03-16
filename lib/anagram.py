class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        word = self.word.lower()
        anagrams = []
        for candidate in word_list:
            candidate_lower = candidate.lower()
            if candidate_lower != word and sorted(candidate_lower) == sorted(word):
                anagrams.append(candidate)
        return anagrams
