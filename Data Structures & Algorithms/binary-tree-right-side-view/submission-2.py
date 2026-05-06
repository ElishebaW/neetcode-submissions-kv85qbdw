# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        T: O(n)
        S: O(n)
        """
        result = [] 

        if root is None:
            return result

        queue = deque([root])

        while queue:
            ori_level_size = len(queue)

            for i in range(len(queue)):
                node = queue.popleft()
                if i == ori_level_size - 1:
                    result.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return result

        