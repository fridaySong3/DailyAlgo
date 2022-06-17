# https://www.acmicpc.net/problem/1721
import sys

class box:
    wildcard = -1
    sideLen = 4
    def __init__(self, bx):
        self.up = bx[0]
        self.side = bx[1:1+box.sideLen]
    def rotate_to_be_same(self, other):
        for i in range(box.sideLen):
            isSame = True
            for j in range(box.sideLen):
                idx = (i + j) % box.sideLen
                if self.side[j] != box.wildcard and \
                    other[idx] != box.wildcard and \
                        self.side[j] != other[idx]:
                    isSame = False
                    break
            if isSame:
                return i
        return -1
    def rotate(self, r):
        return self.side[-r:] + self.side[:-r]
    def __str__(self):
        return "(" + str(self.up) + ", " + str(self.side) + ")"
    
N = int(sys.stdin.readline())
boxes = [box( list(map(int, sys.stdin.readline().split())) ) for _ in range(N**2)]
isUsed = [False for _ in range(len(boxes))]
boxLoc = [[None for _ in range(N)] for _ in range(N)]
boxUpRot = [[None for _ in range(N)] for _ in range(N)]

def get_template(r, c):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    match = [2, 3, 0, 1]
    template = []
    for d in range(len(dr)):
        nr = r + dr[d]
        nc = c + dc[d]
        inRange = (0 <= nr < N and 0 <= nc < N)
        if not inRange:
            template.append(0)
        else:
            if boxLoc[nr][nc] == None:
                template.append(-1)
            else:
                template.append(boxLoc[nr][nc][match[d]])
    return template

def next(r, c):
    nr = r
    nc = c + 1
    if nc == N:
        nc = 0
        nr = r + 1
    if nr == N:
        nr = 0
    return nr, nc

def arrange_boxes(r, c):
    template = get_template(r, c)
    for b in range(len(boxes)):
        if isUsed[b]:
            continue
        rot = boxes[b].rotate_to_be_same(template)
        if rot != -1:
            isUsed[b] = True
            boxLoc[r][c] = boxes[b].rotate(rot)
            boxUpRot[r][c] = (boxes[b].up, rot)
            if r==N-1 and c==N-1:
                return True
            nr, nc = next(r, c)
            success = arrange_boxes(nr, nc)
            if success:
                return True
            else:
                isUsed[b] = False
                boxLoc[r][c] = None
                boxUpRot[r][c] = None

success = arrange_boxes(0, 0)

if success:
    for row in boxUpRot:
        for up, _ in row:
            print(up, end=" ")
        print()
    for row in boxUpRot:
        for _, rot in row:
            print(rot, end=" ")
        print()
    
    