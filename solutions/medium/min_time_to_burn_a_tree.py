# https://www.geeksforgeeks.org/amazon-interview-experience-amazonwow/

# Question
#  Given a binary tree and one node is set on fire so find the time required to burn all the nodes. 
# Input : 
#             1
#        /       \
#       2          3
#     /  \          \
#    4    5          6
#       /   \         \
#      7     8         9
#                       \
#                        10
# Leaf = 8
# Output : 7

# Solution
from typing import List, Optional

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.left_depth = 0
        self.right_depth = 0
        self.contains_burnt = False
        self.time = -1
        self.ans = -1


class Solution:
    def form_tree(self, arr: List) -> Optional[TreeNode]:
        if not arr:
            return None

        n = len(arr)
        arr[0] = TreeNode(arr[0])
        idx_stack = [0]
        while idx_stack:
            par_idx = idx_stack.pop(0)
            l_child_idx = par_idx*2 + 1
            r_child_idx = par_idx*2 + 2

            if l_child_idx < n and arr[l_child_idx] != -1:
                arr[l_child_idx] = TreeNode(arr[l_child_idx])
                arr[par_idx].left = arr[l_child_idx]
                idx_stack.append(l_child_idx)

            if r_child_idx < n and arr[r_child_idx] != -1:
                arr[r_child_idx] = TreeNode(arr[r_child_idx])
                arr[par_idx].right = arr[r_child_idx]
                idx_stack.append(r_child_idx)

        return arr[0]

    def min_time_to_burn(self, node: TreeNode, value: int) -> None:
        if not node:
            return

        # since leaf node is being burnt
        if not node.left and not node.right:
            if node.val == value:
                node.contains_burnt = True
                node.time = 0
                node.ans = 0
            return 

        self.min_time_to_burn(node.left, value)
        self.min_time_to_burn(node.right, value)

        # set left depth and right depth
        node.left_depth = max(node.left.left_depth, node.left.right_depth) + 1 if node.left else 0
        node.right_depth = max(node.right.left_depth, node.right.right_depth) + 1 if node.right else 0

        if node.left and node.left.contains_burnt:
            node.time = node.left.time + 1
            node.contains_burnt = True
            node.ans = node.time + node.right_depth
        elif node.right and node.right.contains_burnt:
            node.time = node.right.time + 1
            node.contains_burnt = True
            node.ans = node.time + node.left_depth
        
        return 
            
from pathlib import Path
if __name__ == "__main__":
    sol = Solution()
    tests = []
    with open(f'test_files/{Path(__file__).stem}.txt') as file:
        for line in file:
            l = line.strip('\n')
            if l:
                tests.append(list(map(int,l.split(' '))))
            else:
                tests.append([])

    for test in tests:
        burnt_val = test[0]
        root = sol.form_tree(test[1:])
        sol.min_time_to_burn(root, burnt_val)

        # stack = [root]
        # while stack:
        #     node = stack.pop(0)
        #     print(node.val, node.time, node.left_depth, node.right_depth, node.ans)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)

        print(root.ans)
