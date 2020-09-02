# https://www.geeksforgeeks.org/amazon-interview-experience-amazonwow/

# Question
# Print all pairs with given sum
# Eg:
# Input  :  arr[] = {1, 5, 7, -1, 5}, 
#           sum = 6
# Output : (1, 5) (7, -1) (1, 5)

# Input  :  arr[] = {2, 5, 17, -1}, 
#           sum = 7
# Output :  (2, 5)

# Solution
from typing import List
from collections import defaultdict
class Solution:
    def print_pairs(self, arr: List, sum_: int) -> List:
        if not arr:
            return []

        # Since we need to print redundant pairs, 2 pointer method
        # wouldn't work
        map_ = defaultdict(lambda : 0)
        for ele in arr:
            map_[ele] += 1

        pairs = []
        for ele in arr:
            if ele in map_.keys() and sum_-ele in map_:
                if ele == sum_-ele and map_[ele] > 1:
                    count = (map_[ele] * (map_[ele]-1)) //2
                elif ele != sum_-ele:
                    count = map_[ele]*map_[sum_-ele]
                else:
                    continue
                pairs.extend([(ele, sum_-ele)]*count)
                del map_[sum_-ele]

            if ele in map_:
                del map_[ele]
                
        return pairs

from pathlib import Path
if __name__ == "__main__":
    sol = Solution()
    with open(f'test_files/{Path(__file__).stem}.txt') as file:
        lines = file.readlines()
        tests = []
        for idx in range(0, len(lines), 2):
            l = lines[idx].strip('\n')
            sum_ = int(lines[idx+1].strip('\n'))
            if l:
                tests.append((list(map(int,l.split(','))), sum_))
            else:
                tests.append(([], sum_))

    for test in tests:
        pairs = sol.print_pairs(test[0], test[1])
        print(pairs)
