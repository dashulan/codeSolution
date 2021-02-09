class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.rigth = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        self.pre =pre
        self.tin =tin
        root = self.recur(0,0,len(tin)-1)
        return root

    def recur(self,root,left,right):
        if left>right:
            return
        node = TreeNode(self.pre[root])
        i = self.tin.index(self.pre[root])
        # 当只有一个节点的情况时
        # 如果root传的是元素本身,那么root+1就越界了，但这里传的是索引下标所以没事
        # 此时一个节点的情况下 传进的left和right 变成了left>right 到了出口
        leftNode = self.recur(root+1,left,i-1)       
        rightNode = self.recur(((root+(i-left))+1),i+1,right)
        node.left = leftNode
        node.right = rightNode
        return node   
    
a = Solution()
pre =[1,2,3,4,5,6,7]
tin = [3,2,4,1,6,5,7]
a.reConstructBinaryTree(pre,tin)