# https://www.geeksforgeeks.org/amazon-interview-experience-amazonwow/

# Question
# Given a string with ‘U’ and ‘D’. Find the number of mountains and valleys 
# Eg: 

# Input: UUDDDDUDUU
# Output: Mountain 1 is formed by UUDD and 1 Valley by DDUDUU

# Solution
from typing import List
class Solution:
    def count_mountains_valleys(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        count = 0
        for ch in s:
            if not stack or stack[-1] == ch:
                stack.append(ch)
            else:
                stack.pop(-1)

            if not stack:
                count += 1
        
        return count
            
from pathlib import Path
if __name__ == "__main__":
    sol = Solution()
    tests = []
    with open(f'test_files/{Path(__file__).stem}.txt') as file:
        for line in file:
            l = line.strip('\n')
            tests.append(str(l))

    for test in tests:
        count = sol.count_mountains_valleys(test)
        print(count)
