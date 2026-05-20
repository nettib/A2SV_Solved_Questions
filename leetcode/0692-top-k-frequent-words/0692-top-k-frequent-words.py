class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        track = {}

        for word in words:
            if word not in track:
                track[word] = 0
            track[word] += 1
        
        
        heap = []

        for val in track.values():
            if len(heap) == k:
                heappush(heap, max(val, heappop(heap)))
            else:
                heappush(heap, val)
        
        new_heap = set(heap)
        new_track = {}

        for word in track:
            if track[word] in new_heap:
                if track[word] not in new_track:
                    new_track[track[word]] = []
                new_track[track[word]].append(word)
        
        for freq in new_track:
             new_track[freq] = sorted(new_track[freq])
        
        heap.sort(reverse=True)
        ans = []

        for i in range(len(heap)):
            if i != 0 and heap[i] == heap[i - 1]:
                continue
            for word in new_track[heap[i]]:
                if len(ans) == k:
                    return ans
                ans.append(word)
                
        return ans


                






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna