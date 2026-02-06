class Solution:   
    def findUnion(self, a, b):
        track = set(a)
        
        ans = track.union(set(b))
        
        
        return list(ans)
        
        
        
        
        
        
