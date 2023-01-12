"""
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or
object into a sequence of bits so that it can be stored in a file
or memory buffer, or transmitted across a network connection link
to be reconstructed later in the same or another computer
environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a binary tree
can be serialized to a string and this string can be deserialized
to the original tree structure.

Clarification: The input/output format is the same as how LeetCode
serializes a binary tree. You do not necessarily need to follow
this format, so please be creative and come up with different
approaches yourself. 

How to serialize a tree
https://support.leetcode.com/hc/en-us/articles/360011883654-
What-does-1-null-2-3-mean-in-binary-tree-representation-

Example 1:
    - Input: root = [1,2,3,null,null,4,5]
    - Output: [1,2,3,null,null,4,5]

Example 2:
    - Input: root = []
    - Output: []
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "[]"

        result = []
        queue = []
        queue.append(root)

        while queue:
            curr = queue.pop(0)

            if curr:
                result.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                result.append(str(None))

        while result[len(result) - 1] == "None":
            result.pop()

        return f'[{ ",".join(result) }]'

    def convertTreeNodes(self, data: str):
        serializedTree = data.strip("][").split(",")
        treeNodeList = []
        for node in range(len(serializedTree)):
            if serializedTree[node] != "None":
                treeNodeList.append(TreeNode(int(serializedTree[node])))
            else:
                treeNodeList.append(None)

        return treeNodeList

    def deserialize(self, data: str) -> list:
        if data in ["", "[]", "None", None]:
            return None

        treeNodeList = self.convertTreeNodes(data)

        root = treeNodeList.pop(0)
        queue = [root]

        while queue:
            curr = queue.pop(0)

            if not curr:
                continue

            left = treeNodeList.pop(0) if treeNodeList else None
            right = treeNodeList.pop(0) if treeNodeList else None

            curr.left = left
            queue.append(curr.left)

            curr.right = right
            queue.append(curr.right)

        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()

serialize = codec.serialize(root)
deserialize = codec.deserialize(serialize)
serialize2 = codec.serialize(deserialize)

print("deserialize", deserialize)
print("serialize", serialize)
print("serialize2", serialize2)
