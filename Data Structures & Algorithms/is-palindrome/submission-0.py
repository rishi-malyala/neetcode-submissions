class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ""

        stack = []
        rev = []

        for ch in s:
            if ch.isalnum():
                clean_text += ch.lower()
                stack.append(ch.lower())

        while stack:
            rev.append(stack.pop())

        return clean_text == ''.join(rev)