class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pattern_graph = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                pattern_graph[pattern].append(word)
        
        graph = defaultdict(set)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for nei in pattern_graph[pattern]:
                    if nei not in graph[word] and nei != word:
                        graph[word].add(nei)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for nei in graph[word]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append(nei)
            res += 1
        
        return 0

        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna