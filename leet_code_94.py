from  typing import List,Optional
class TreeNode:
    def __init__(self,val= 0,left = None, right = None ):
        self.val = val 
        self.left = None
        self.right = None

class Solution(TreeNode):
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []

        result = []
        result.extend(self.inorderTraversal(root.left))
        result.extend([root.val])
        result.extend(self.inorderTraversal(root.right))
        return result

s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.inorderTraversal(root))
        
