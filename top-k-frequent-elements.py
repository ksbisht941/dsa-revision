https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    print(count)

    return heapq.nlargest(
        k,
        count.keys(),
        key=count.get
    )
