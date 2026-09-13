class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        result = []

        def backtrack(index,current):
            if index==len(digits):
                result.append(current)
                return 
            
            currDigit = digits[index]
            for letter in map[currDigit]:
                backtrack(index+1,current+letter)
            
        backtrack(0,"")
        return result