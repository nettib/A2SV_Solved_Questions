from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.q1 = deque([])
        self.q2 = deque([])
        self.val = value
        self.k = k
        self.id = 0

    def consec(self, num: int) -> bool:
        while self.q2 and len(self.q1) == self.k and self.q1[0][0] == self.q2[0][0]:
            self.q2.popleft()
        while len(self.q1) == self.k:
            self.q1.popleft()
        self.id += 1
        elem = [self.id, num]
        self.q1.append(elem)
        if num != self.val:
            self.q2.append(elem)
        
        return len(self.q2) == 0 and len(self.q1) == self.k



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)