# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        """
        BFS algo 
        Level by level

        queue = []
        result = []

        while queue
        loop through the level
        add both left and right
        but only add right to the result
        if the node is a left add the right but if no right
        add the left of that node to result

         return result

        """
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            original_len = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if i == original_len - 1:
                    result.append(node.val)

                if node.left != None:
                    queue.append(node.left)
                
                if node.right != None:
                    queue.append(node.right)
        
        return result
