class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        MORSE_CODE = (
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
        "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")
        for word in words:
            morse = [None] * len(word)
            for i, c in enumerate(word):
                morse[i] = MORSE_CODE[ord(c) - ord('a')]
            res.add(''.join(morse))
        return len(res)
