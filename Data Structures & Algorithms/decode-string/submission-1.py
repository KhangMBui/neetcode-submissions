class Solution:
    def decodeString(self, s: str) -> str:
        # 2[a3[b]]c abbbabbbc
        # axb3[z]4[c] = axbzzzcccc

        # [2, abbb] abbbabbbc

        # use a stack to keep track of number?
        # We must be able to tell when a bracket starts

        if not s:
            return ""

        stack = [] # O(n)

        # O(n)
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                # 1. get encoded string inside brackets
                string = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string
                
                # 2. Remove "["
                stack.pop()

                # 3. Get repeat_number
                number_str = ""
                while stack and stack[-1].isdigit():
                    number_str = stack.pop() + number_str
                
                number = int(number_str)
                
                # 4. Decode and push back
                stack.append(string * number)

        return "".join(stack)
        