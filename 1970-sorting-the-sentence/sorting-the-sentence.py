class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        def get_index(word):
            return int(word[-1])
        words.sort(key=get_index)
        return ' '.join(word[:-1] for word in words)
        