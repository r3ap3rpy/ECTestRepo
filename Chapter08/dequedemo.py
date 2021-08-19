# DEQUE -> Double Ended Queue
# O -> O(1) -> O(n-1)
from collections import deque
#deque([iterable],maxlen)
emptydeque = deque()
notempty = deque(range(10), maxlen = 10)
notempty.appendleft(10)
notempty.index(17)