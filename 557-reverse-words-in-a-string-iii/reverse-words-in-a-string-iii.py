class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        #print(a)
        words = []
        for word in a:
            words.append(word[::-1])
        st = " ".join(words)
        return st