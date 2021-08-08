from collections import deque
from typing import List


class Solution_BFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        count = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == '1':
                    self.bfs(grid, visited, row, col, i, j)
                    count += 1
        return count

    def bfs(self, grid, visited, row, col, i, j):
        queue = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue.append([i, j])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                new_x = x + dx
                new_y = y + dy
                if self.valid(grid, visited, row, col, new_x, new_y):
                    visited[new_x][new_y] = True
                    queue.append([new_x, new_y])

    def valid(self, grid, visited, row, col, x, y):
        return x >= 0 and x < row and y >= 0 and y < col and not visited[x][y] and grid[x][y] == '1'



class Solution_DFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        count = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid, visited, row, col, i, j)
                    count += 1
        return count

    def dfs(self, grid, visited, row, col, i, j):
        if not self.valid(grid, visited, row, col, i, j):
            return
        visited[i][j] = True
        self.dfs(grid, visited, row, col, i + 1, j)
        self.dfs(grid, visited, row, col, i - 1, j)
        self.dfs(grid, visited, row, col, i, j + 1)
        self.dfs(grid, visited, row, col, i, j - 1)

    def valid(self, grid, visited, row, col, x, y):
        return x >= 0 and x < row and y >= 0 and y < col and not visited[x][y] and grid[x][y] == '1'