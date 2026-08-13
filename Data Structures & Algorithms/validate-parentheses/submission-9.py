class Solution:

    def isValid(self, s: str) -> bool:
        CLOSE_PAIR = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }

        stack = [s[0]]

        for i in range(1, len(s)):
            char = s[i]

            if len(stack) > 0 and stack[-1] in CLOSE_PAIR and char == CLOSE_PAIR[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0