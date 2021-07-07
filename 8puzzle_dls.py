import copy
import sys

MAX_DEPTH= int(3)
depth= int(0)
visited=[]
q = []

#finds position of blank space (number 0)
def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j]==0:
                return [i,j]

#moves blank space up
def up(a,pos):
    i = pos[0]
    j = pos[1]
    if i > 0:
        temp = copy.deepcopy(a)
        temp[i][j] = temp[i-1][j]
        temp[i-1][j] = 0
        return temp
    else:
        return a
#moves blank space down
def down(a,pos):
    i = pos[0]
    j = pos[1]
    if i < 2:

        temp = copy.deepcopy(a)
        temp[i][j] = temp[i+1][j]
        temp[i+1][j] = 0
        return temp
    else:
        return a
#moves blank space left
def left(a,pos):
    i = pos[0]
    j = pos[1]
    if j > 0:
        temp = copy.deepcopy(a)
        temp[i][j] = temp[i][j-1]
        temp[i][j-1] = 0
        return temp
    else:
        return a
#moves blank space right
def right(a,pos):
    i = pos[0]
    j = pos[1]
    if j < 2:

        temp = copy.deepcopy(a)
        temp[i][j] = temp[i][j+1]
        temp[i][j+1] = 0
        return temp
    else:
        return a

#DEPTH LIMITED FUNCTION  
def dlsSomething(a,g,depth):
    if depth<=MAX_DEPTH:
        if a in visited:
            return False
        if a == g:
            visited.append(a)
            print("Found It")
            return True
        visited.append(a)
        if up(a,find_pos(a)) != a and dlsSomething(up(a,find_pos(a)),g,depth+1):
            return True
        if right(a,find_pos(a)) != a and dlsSomething(right(a,find_pos(a)),g,depth+1):
            return True
        if down(a,find_pos(a)) != a and dlsSomething(down(a,find_pos(a)),g,depth+1):
            return True
        if left(a,find_pos(a)) != a and dlsSomething(left(a,find_pos(a)),g,depth+1):
            return True
        return False

    else:
        print("MAX DEPTH REACHED")
    return 


def main():
    a = [[2,0,3],[1,8,4],[7,6,5]]
    g = [[1,2,3],[8,0,4],[7,6,5]]

    if dlsSomething(a,g,depth):
        for i in range (len(visited)):
            print(visited[i])
        
        print("Number of states explored is ",len(visited))
main()

