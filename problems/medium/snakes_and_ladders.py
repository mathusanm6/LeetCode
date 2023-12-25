from collections import deque


class Solution:
    def snakesAndLadders(self, board):
        # board size
        row_sz = len(board)
        col_sz = len(board[0])

        q = deque()
        visited = set()
        parent = [-1] * ((row_sz * col_sz) + 1)
        distance = [-1] * ((row_sz * col_sz) + 1)

        q.append(1)
        visited.add(1)
        distance[1] = 0

        while q:
            node = q.popleft()

            for i in range(1, 7):
                n = node + i
                if n >= len(parent):
                    continue

                ft = (n - 1) // col_sz
                r = row_sz - 1 - ft
                c = (n - 1) % col_sz
                if ft % 2 != 0:
                    c = col_sz - 1 - c

                v = board[r][c]

                if v != -1:
                    n = v
                if n in visited or v == node:
                    continue

                q.append(n)
                visited.add(n)
                parent[n] = node
                distance[n] = distance[node] + 1

        return distance[-1]
