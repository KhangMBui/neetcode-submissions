class Solution:
    def simplifyPath(self, path: str) -> str:
        # "." = current dir
        # ".." = previous dir
        # "//" or "///" are same as "/"
        # The rest are treated as dir or file names (even ... or ....)

        # Rules for output:
        # - Path starts with /
        # - Dir are separated with /
        # - Path cannot end with /
        # - Path can't have . or .. to denote curr or prev dir

        # /neetcode/practice//...///../courses
        # /neetcode/practice/courses

        # /..//_home/a/b/..///
        # /_home/a

        # use a stack
        # Do not take in any more than 1 slash
        # if meet '.', ignore
        # if meet '..', pop from stack
        # if meet '...' onwards, put it into the stack as a directory name
        # if meet words, count it as name to put into stack
        # Perhaps we need to use two pointers (slow and fast)
        # to find words to put into our stack

        # Actually, we put in the stack and then turn it into a string,
        # separated by "/"

        if not path:
            return ""

        stack = []
        l = r = 0
        n = len(path)

        while r < n:
            while r < n and path[r] == "/":
                r += 1

            l = r

            while r < n and path[r] != "/":
                r += 1

            word = path[l:r]
            if word == "..":
                if stack:
                    stack.pop()
            elif word == ".":
                # Ignore
                continue
            elif word != "":
                stack.append(word)
        res = ""
        for dir in stack:
            res += "/" + dir
        return res if res else "/"