class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.degree = 0

board = [[0] * 8 for _ in range(8)]
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, 2, -2, 2, -2, 1, -1]
xStart = 0
yStart = 0
ok = False

def printChess():
    for row in board:
        print(" ".join(map(str, row)))

def canPlaceChess(xCur, yCur):
    return 0 <= xCur < 8 and 0 <= yCur < 8 and board[xCur][yCur] == 0

def setDeg(node):
    for i in range(8):
        if canPlaceChess(node.x + dx[i], node.y + dy[i]):
            node.degree += 1

def knightTour(xCur, yCur, move):
    global ok
    board[xCur][yCur] = move

    if ok:
        return
    if move == 64:
        printChess()
        ok = True
        return

    chess = []
    for i in range(8):
        if canPlaceChess(xCur + dx[i], yCur + dy[i]):
            node = Node(xCur + dx[i], yCur + dy[i])
            setDeg(node)
            chess.append(node)

    if chess:
        # Warnsdorff's heuristic
        chess.sort(key=lambda node: node.degree)
        for i in range(len(chess)):
            if not ok:
                knightTour(chess[i].x, chess[i].y, move + 1)
    board[xCur][yCur] = 0

if __name__ == "__main__":
    yStart, xStart = map(int, input("Nhap vi tri cua quan co(ex: 1 1): ").split())
    yStart -= 1
    xStart -= 1
    knightTour(xStart, yStart, 1)
