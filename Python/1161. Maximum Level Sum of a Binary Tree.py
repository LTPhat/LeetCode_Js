# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        currLevel = 1
        maxLevel = 1
        maxSum = float('-inf')
        queue = [root]
        while len(queue):
            levelNode = []
            levelSum = 0
            n = len(queue)
            for item in queue:
                levelSum += item.val
                if item.left:
                    levelNode.append(item.left)
                if item.right:
                    levelNode.append(item.right)
            if (levelSum > maxSum):
                maxSum = levelSum
                maxLevel = currLevel
            currLevel += 1
            queue = levelNode
        return maxLevel