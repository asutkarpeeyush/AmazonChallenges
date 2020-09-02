# https://www.geeksforgeeks.org/amazon-interview-experience-amazonwow/

# Question
# Print the length of the longest decreasing subsequence.
# Eg:   Input: arr[] = [15, 27, 14, 38, 63, 55, 46, 65, 85]
#       Output: 3
#       Explanation: The longest decreasing sub sequence is {63, 55, 46}

#       Input: arr[] = {50, 3, 10, 7, 40, 80}
#       Output: 3
#       Explanation: The longest decreasing subsequence is {50, 10, 7}

# Solution
from typing import List
class Solution:
    def longest_decreasing_ss(self, arr: List) -> int:
        if not arr:
            return 0

        n = len(arr)
        dp = [1] * n

        # For every index, check if this index can add on 
        # to max length encountered so far by comparing this index value
        # with ones before it
        for i in range(1, n):
            for j in range(i):
                if arr[j] > arr[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

        return max(dp)


from pathlib import Path
if __name__ == "__main__":
    sol = Solution()
    tests = []
    with open(f'test_files/{Path(__file__).stem}.txt') as file:
        for line in file:
            l = line.strip('\n')
            if l:
                tests.append(list(map(int,l.split(','))))
            else:
                tests.append([])

    for test in tests:
        longest = sol.longest_decreasing_ss(test)
        print(longest)
