# https://www.geeksforgeeks.org/amazon-interview-experience-amazonwow/

# Question
# Given a string convert it into a valid address by inserting a ‘.’ after www then insert a ‘.’ before com and if there are more characters after com then put a ‘/’ after com and then the rest of the characters.
# Eg: Input:  wwwgooglecomr
#     Output: www.google.com/r

# Solution
class Solution:
    def convert_string(self, s: str) -> str:
        ans = ""

        if 'www' in s:
            ans += 'www.'
            s = s.strip('www')
        
        n = len(s)
        idx = 0
        while idx < n:
            if s[idx] == 'c' and (idx+1 < n and s[idx+1] == 'o') and (idx+2 < n and s[idx+2] == 'm'):
                ans += '.com'
                idx += 3
                break
            else:
                ans += s[idx]
                idx += 1

        if idx < n:
            ans += "/"

        while idx < n:
            ans += s[idx]
            idx += 1
        
        return ans

from pathlib import Path
if __name__ == "__main__":
    sol = Solution()
    with open(f'test_files/{Path(__file__).stem}.txt') as file:
        tests = [line for line in file]

    for test in tests:
        converted_s = sol.convert_string(str(test).strip('\n'))
        print(converted_s)
