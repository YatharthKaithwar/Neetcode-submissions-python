class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(currString, open, close):
            if len(currString) == 2*n:
                result.append(currString)
                return

            if open<n:
                backtrack(currString + '(',open+1,close)
            
            if close<open:
                backtrack(currString +')',open,close+1)

        backtrack("",0,0)
        return result
