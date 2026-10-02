class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matchedIndices = set()

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            
            for i,value in enumerate(t):
                if value==target[i]:
                    matchedIndices.add(i)
            
            if len(matchedIndices)==3:
                return True
        return len(matchedIndices)==3
            
