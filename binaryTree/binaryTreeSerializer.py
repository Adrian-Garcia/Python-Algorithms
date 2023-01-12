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

    def deserialize(self, data: str):
        serializedTree = data.strip("][").split(",")

        if not serializedTree:
            return None

        val = int(serializedTree.pop(0))
        root = TreeNode(val)
        queue = [root]

        while serializedTree:
            curr = queue.pop(0)

        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

serialize = Codec().serialize(root)
deserialize = Codec().deserialize("[1,2,3,None,None,4,5]")

print(deserialize)
