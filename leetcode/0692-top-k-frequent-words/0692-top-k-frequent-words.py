class heapItem:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        track = {}

        for word in words:
            if word not in track: track[word] = 0
            track[word] += 1
        
        heap = []

        for word in track:
            item = heapItem(word, track[word])

            if len(heap) >= k:
                if item > heap[0]:
                    heappop(heap)
                    heappush(heap, item)
            else:
                heappush(heap, item)
        
        ans = []
        while heap:
            item = heappop(heap)
            ans.append(item.word)
        
        return ans[::-1]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna