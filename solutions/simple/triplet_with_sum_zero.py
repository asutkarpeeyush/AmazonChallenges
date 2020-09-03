# https://www.geeksforgeeks.org/amazon-interview-experience-amazonwow/

# Question
# Find all triplets with zero sum
# Eg:
# Input : arr[] = {0, -1, 2, -3, 1}
# Output : (0 -1 1), (2 -3 1)

# Explanation : The triplets with zero sum are
# 0 + -1 + 1 = 0 and 2 + -3 + 1 = 0  

# Input : arr[] = {1, -2, 1, 0, 5}
# Output : 1 -2  1
# Explanation : The triplets with zero sum is
# 1 + -2 + 1 = 0 

# Solution
from typing import List
from collections import defaultdict
class Solution:
    def print_triplets(self, arr: List) -> List:
        if not arr:
            return []
        
        map_ = defaultdict(lambda: 0)
        for ele in arr:
            map_[ele] += 1
        
        arr.sort()
        pairs = []
        s_i = 0
        e_i = len(arr) - 1
        while s_i < e_i:
            sum_of_two = arr[s_i] + arr[e_i]
            if 0 - sum_of_two in map_:
                pairs.append((arr[s_i], arr[e_i], 0-sum_of_two))
                s_i += 1
                e_i -= 1
            elif sum_of_two < 0:
                s_i += 1
            else:
                e_i -= 1

        return pairs

from pathlib import Path
if __name__ == "__main__":
    sol = Solution()
    with open(f'test_files/{Path(__file__).stem}.txt') as file:
        lines = file.readlines()
        tests = []
        for idx in range(0, len(lines)):
            l = lines[idx].strip('\n')
            if l:
                tests.append(list(map(int,l.split(','))))
            else:
                tests.append([])
    print(tests)
    for test in tests:
        pairs = sol.print_triplets(test)
        print(pairs)
