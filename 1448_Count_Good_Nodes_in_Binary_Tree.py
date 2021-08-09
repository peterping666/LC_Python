import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, root, max_val):
        if not root:
            return 0
        count = 0
        if root.val >= max_val:
            count = 1
            max_val = root.val
        return count + self.dfs(root.left, max_val) + self.dfs(root.right, max_val)