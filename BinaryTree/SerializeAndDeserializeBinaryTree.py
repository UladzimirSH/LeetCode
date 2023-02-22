class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        if not root:
            return ""

        values = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node is None:
                values.append(None)
                continue

            values.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        while values[-1] is None:
            values.pop()

        return "[" + ", ".join(str(x) if x is not None else "None" for x in values) + "]"

    def deserialize(self, data):
        if data == "":
            return None

        values = eval(data)

        root = TreeNode(values.pop(0))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if len(values) > 0:
                left_node_val = values.pop(0)
                if left_node_val is not None:
                    left_node = TreeNode(left_node_val)
                    node.left = left_node
                    queue.append(left_node)
            if len(values) > 0:
                right_node_val = values.pop(0)
                if right_node_val is not None:
                    right_node = TreeNode(right_node_val)
                    node.right = right_node
                    queue.append(right_node)

        return root


node5 = TreeNode(5)
node4 = TreeNode(0)
node2 = TreeNode(2)
node3 = TreeNode(3, left=node4, right=node5)
node1 = TreeNode(1, left=node2, right=node3)
codec = Codec()
serialized = codec.serialize(node1)
print(serialized)
print(codec.deserialize(serialized))