class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if stack and c in close_to_open:
                if stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False