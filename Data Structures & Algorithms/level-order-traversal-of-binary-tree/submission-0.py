# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Tree
        # BFS
      
        """
        Input: root = [1,2,3,4,5,6,7]

        Output: [[1],[2,3],[4,5,6,7]]

        queue 
        visited = set()
        result = []

        while queue:
            pop top of queue
            new list = []
            loop through the nodes at that level adding them to a new. list

            root.right
            root.left
            add them to new list
            add new list to result 



        return the result
        """
        if root is None:
            return []

        queue = deque([root])
        result = []
        while queue:
            new_list = []

            for i in range(len(queue)):
                node = queue.popleft()
                new_list.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            result.append(new_list)
        
        return result













