class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = float("-inf")

        citations.sort()

        for i, citation in enumerate(citations):
            if (len(citations) - i) >= citation:
                h_index = max(h_index, citation)
            elif (len(citations) - i) < citation:
                h_index = max(h_index, len(citations) - i)
        
        return h_index
