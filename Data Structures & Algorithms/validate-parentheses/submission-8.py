class Solution:
    def isValid(self, s: str) -> bool:
        #solution: create a hashmap of pair closeToOpen
        #when iterate the string, if we hit close, we check
        #if the top of the stack is the corresponding open
        #if yes, pop. 
        stack = []
        closeToOpen = { ")" : "(", "}": "{", "]": "[" }
        for c in s:
            #Check if it's in the key (close)
            if c in closeToOpen:
                #Then the stack has to be not empty, otherwise no open but close == false
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
        


        