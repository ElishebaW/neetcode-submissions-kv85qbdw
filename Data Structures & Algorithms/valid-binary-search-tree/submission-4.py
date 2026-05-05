# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        T: worst case O(n ) - in case of skewed tree
        S: worst case O(n) - case of skewed tree
        """

        def validate(node, min_val, max_val):
            if node is None:
                return True

            if not (min_val < node.val < max_val):
                return False

            return validate(node.right, node.val , max_val) and validate(node.left, min_val, node.val)

        return validate(root, float("-inf"), float("inf"))

        