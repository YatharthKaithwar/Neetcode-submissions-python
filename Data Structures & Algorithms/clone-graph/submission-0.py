"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        # Create clone of starting node
        visited[node] = Node(node.val)

        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:

                # If neighbor is not cloned yet
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Connect cloned current node
                # to cloned neighbor
                visited[current].neighbors.append(
                    visited[neighbor]
                )

        return visited[node]