class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        track = {}

        for n1, n2 in edges:
            track[n1] = track.get(n1, 0) + 1
            track[n2] = track.get(n2, 0) + 1
        
        
        _max = -1
        center = -1
        for node in track:
            if track[node] > _max:
                center = node
                _max = track[node]
        
        return center