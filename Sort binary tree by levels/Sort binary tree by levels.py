# class Node:
#     def __init__(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
from collections import deque

def tree_by_levels(node):
    """
    Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.
    """
    if node is None:
        return []
    rs = []

    queue = deque([node])

    while queue:
        current = queue.popleft()
        rs.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return rs



# # # assert tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)) == [1, 2, 3, 4, 5, 6]


# print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))

# # [2,8,9,1,3,4,5]
# n = Node(Node(Node(None, None, 1), Node(None, None, 3), 8), Node(Node(None, None, 4), Node(None, None, 5), 9), 2)

# print(tree_by_levels(n))
