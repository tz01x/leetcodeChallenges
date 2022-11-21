class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = [
            w
            for w in s.split(' ')
            if len(w.strip())
        ]
        words.reverse()
        return ' '.join(words)