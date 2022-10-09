#1-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bfs(T):
    q = queue.Queue()
    if T != None:
        q.enqueue(T)
        while not q.isempty():
            val = q.dequeue()
            print(val.key,end = " ")
            if val.left != None:
                q.enqueue(val.left)
            if val.right != None:
                q.enqueue(val.right)  # This line adds the right son of the dequeued node to the q thread

#2----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def dfs(T):
    "T not empty tree"
    if T == None:
        return 0
    else:
        return dfs(T.left) and dfs(T.right)

#3----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def degenerate(B):
    "B not empty tree"
    if B == None:
        return True
    else:
        if B.left != None and B.right != None:
            return False
        else:
            return degenerate(B.left) and degenerate(B.right)

#4----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def occurences(B):
    "B not empty tree"
    L = []
    q = queue.Queue()
    q.enqueue(B,"")
    while not q.isempty():
        (B,occ) = q.dequeue()
        L.append(occ)
        if B.left != None:
            q.enqueue(B, occ + '0')
        if B.right != None:
            q.enqueue(B, occ + '1')
    L[0] = char(949)
    return L

#5----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def nodes_leaves(B):
    if B.left == None:
        return 1
    else:
        lleaves = nodes_leaves(B.left)
        rleaves = nodes_leaves(B.right)
    return rleaves + lleaves

def nodes(B):
    nl = nodes_leaves(B)
    return (nl - 1,nl)

#6----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def gapline(L):
    for i in range(len(L)):
        minline = min(L)
        maxline = max(L)
    gap = (maxline - minline)
    return gap

def maxgap(M):
    maximumgap = 0
    for line in range(len(M)):
        maxgaps = gapline(M[line])
        if maxgaps >= maximumgap:
            maximumgap = maxgaps
    return maximumgap

#7----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_matrices(A,B):
    (LineA,colA) = (len(A), len(A[0]))
    (LineB,colB) = (len(B), len(B[0]))
    if LineA != LineB or colA != colB:
        raise Exception("these matrices don't contain the same dimensions")
    else:
        M = []
        for line in range(len(A)):
            subM = []
            for column in range(len(A[0])):
                subM.append(A[line][column] + B[line][column])
            M.append(subM)
        return M

#8----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def listcheck(L,A):  #checks if the elements of a list are in a list
    (lenL,lenA) = (len(L),len(A))
    if lenA >= lenL:
        return False
    else:
        res = 0
        for i in range(lenA):
            for j in range(lenL):
                if L[j] == A[i]:
                    res += 1
                else:
                    res = 0
        if res == lenA:
            return True
        else:
            return False


def sub_line(M,L):   #checks in all the lists in a matric=x using function listcheck
    lenM = len(M)
    for i in range(len(M)):
        lcheck = listcheck(M[i],L)
        if lcheck != None:
            return True
        else:
            return False

#9----------------------------------------------------------------------------------------------------------------------------------------------------------------------


#10----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def exp2str(B):
    'B not empty tree'
    if B.left == None and B.right == None:
        return B.key
    else:
        return '(' + exp2str(B.left) + B.key + exp2str(B.right) + ')'

#11----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def to_linear(B):  #gets the 
    'B not empty tree'
    if B == None:   
        return '()'
    else:
        s = '(' + str(B.key)
        return s + to_linear(B.left) +  to_linear(B.right) + ')'

#12----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def width(B):  #gets the maximum width in a binary tree
    'B not empty tree'
    if B != None:
        q = queue.Queue()
        q.enqueue(B)
        width = 1
        numnodes = 1
        while not q.isempty():
            numchildren = 0
            while numnodes > 0:
                val = q.dequeue()
                if val.left != None:
                    q.enqueue(val.left)
                    numchildren += 1
                if val.right != None:
                    q.enqueue(val.right)
                    numchildren += 1
                numnodes -= 1
            width = max(width,numchildren)
            numnodes = numchildren
        return width
    return 0

#13----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def init(M):  #creates a matrix with values "val"
    matrix = []
    for line in range(len(M)):
        lines = []
        for column in range(len(M[0])):
            lines.append(0)
        matrix.append(lines)
    return matrix

#14----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mult_matrices(A,B):  #Technique for multiplying 2 matrices
    colA = len(A[0])
    lenB = len(B)
    if colA != lenA:
        print('Dimensions are not compatible !')
    else:
        lenA = len(A)
        colB = len(B[0])
        M = matrix.init(lenA,colA,0)
        for i in range(lenA):
            for j in range(colB):
                for k in range(colA):
                    M[i][j] += A[i][k] * B[k][j]
        return M

#15----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Siamese(n):  #Magic Square
    M = matrix.init(n,n,0)
    i = n - 1
    j = n // 2
    M[i][j] = 1
    for k in range(2,n*n + 1):
        i2 = (i + 1) % n
        j2 = (j + 1) % n
        if M[i2][j2] == 0:
            (i,j) = (i2,j2)
        else:
            i -= 1
            if i == -1:
                i = n - 1
        M[i][j] = k
    return M

#16----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def perfect_dfs_depth(B,depth = 0):  
    if B.left == None:
        if B.right == None:
            return depth
        else:
            return -1
    else:
        if B.right == None:
            return -1
        else:
            ltree = perfect_dfs_depth(B.left,depth += 1)
            rtree = perfect_dfs_depth(B.right,depth += 1)
        if ltree = rtree:
            return ltree
        else:
            return -1

def perfect_dfs(B):
    if B == None:
        return True
    else:
        return perfect_dfs_depth(B) != -1

#17----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def symetric_vertical(M):  #check if a matrix is symmetric vertically
    (l,c) = (len(M),len(M[0]))
    cdiv2 = c // 2
    i = 0
    b = False
    while i < l and not b:
        j = 0
        while j < cdiv2 and M[i][j] == M[i][c - j - 1]:
            j += 1
        b = (j < cdiv2)
        i += 1
    return not b

#18----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def symmetric_diagonal(M):  #check if a matrix is symmetric diagonally
    (l,c) = len(M),len(M[0])
    if l != c:
        return False
    (i,b) = 0,True
    while i < l and b:
        j = 0
        while j < l and b:
            b = M[i][j] == M[j][i]
            j += 1
        i += 1
    return b

#19----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def symmetric_horizontal(M):  #check if a matrix is symmetric horizontally
    (l,c) = (len(M),len(M[0]))
    ldiv2 = l // 2
    (i,j) = (0,c)
    while i < ldiv2 and j == c:
        j = 0
        while j < c and M[i][j] == M[l - i - 1][j]:
            j += 1
        i += 1
    return j == c

#20----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def transpose(M):   #reverses the Matrix
    (l,c) = (len(M),len(M[0]))
    L = []
    for i in range(c):
        line = []
        for j in range(l):
            line.append(M[j][i])
        L.append(line)
    return M

#21----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Search_Matrix(M,x):  #search x position in Matrix
    (r,c) = (len(M),len(M[0]))
    for i in range(r):
        for j in range(c):
            if M[i][j] == x:
                return (i,j)
    if M[i][j] >= r:
        return (-1,-1)        

#22----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def __priority(B):  #checks if the sons's keys of B are smaller or equal to its key
        b = True
        if B.left != None:
            if B.key > B.left.key:
                b = False
            else:
                b = __priority(B.left) 
        if b and B.right != None:
            b = B.key <= B.right.key and __priority(B.right)
        return b
    

def priority(B):
    return B == None or __priority(B)

#23----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def __symmetric(B,C):
    if B == None or C == None:
        return B == C
    else:
        if B.key != C.key:
            return False
        else:
            return __symmetric(B.left,C.right) and __symmetric(B.right,C.left)

def symmetric(B):  #checks if the binary tree is symmetric
    return B == None or __symmetric(B.left,B.right)

#24----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def isSubTree(sB,B): #checks if a sB is a subtree of the binary tree B
    if sB == None:
        return True
    elif B == None:
        return False
    else:
        if sB.key == B.key:
            return equal(sB,B)
        else:
            return isSubTree(sB,B.left) or isSubTree(sB,B.right)

#25----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def equal(B1,B2):  #checks if 2 Binary Trees are Similar
    if B1 == None:
        return B2 == None
    elif B2 == None:
        return False
    elif B1.key == B2.key:
        return equal(B1.left,B2.left) and equal(B1.right,B2.right)
    else:
        return False


# def minimum(L):
#     m = L[0]
#     for i in range(len(L)):
#         if L[i] <= m:
#             m = L[i]
#     return m

# def maximum(L):
#     m = L[0]
#     for i in range(len(L)):
#         if L[i] > m:
#             m = L[i]
#     return m

# def maxgap(M):
#     for line in M:
#             max = maximum(line)
#             min = minimum(line)
#             maxgaps = max - min
#     maxs = maximum(maxgaps)
#     return maxs


# def bfs(T):
#     q = queue.Queue()
#     if T != None:
#         q.enqueue(T)
#         while not q.isempty():
#             val = q.dequeue()
#             print(val.key,end = " ")
#             if val.left != None:
#                 q.enqueue(val.left)
#             if val.right != None:
#                 q.enqueue(val.right)  # This line adds the right son of the dequeued node to the q thread

# def dfs(T):
#     "T not empty tree"
#     if T == None:
#         return 0
#     else:
#         return dfs(T.left) and dfs(T.right)


# def degenerate(B):
#     "B not empty tree"
#     if B == None:
#         return True
#     else:
#         if B.left != None and B.right != None:
#             return False
#         else:
#             return degenerate(B.left) and degenerate(B.right)

# def occurences(B):
#     "B not empty tree"
#     L = []
#     q = queue.Queue()
#     q.enqueue(B,"")
#     while not q.isempty():
#         (B,occ) = q.dequeue()
#         L.append(occ)
#         if B.left != None:
#             q.enqueue(B, occ + '0')
#         if B.right != None:
#             q.enqueue(B, occ + '1')
#     L[0] = char(949)
#     return L

# def nodes_leaves(B):
#     if B.left == None:
#         return 1
#     else:
#         lleaves = nodes_leaves(B.left)
#         rleaves = nodes_leaves(B.right)
#     return rleaves + lleaves

# def nodes(B):
#     nl = nodes_leaves(B)
#     return (nl - 1,nl)


# def gapline(L):
#     for i in range(len(L)):
#         minline = min(L)
#         maxline = max(L)
#     gap = (maxline - minline)
#     return gap

# def maxgap(M):
#     maximumgap = 0
#     for line in range(len(M)):
#         maxgaps = gapline(M[line])
#         if maxgaps >= maximumgap:
#             maximumgap = maxgaps
#     return maximumgap

# def add_matrices(A,B):
#     (LineA,colA) = (len(A), len(A[0]))
#     (LineB,colB) = (len(B), len(B[0]))
#     if LineA != LineB or colA != colB:
#         raise Exception("these matrices don't contain the same dimensions")
#     else:
#         M = []
#         for line in range(len(A)):
#             subM = []
#             for column in range(len(A[0])):
#                 subM.append(A[line][column] + B[line][column])
#             M.append(subM)
#         return M


# def listcheck(L,A):  #checks if the elements of a list are in a list
#     (lenL,lenA) = (len(L),len(A))
#     if lenA >= lenL:
#         return False
#     else:
#         res = 0
#         for i in range(lenA):
#             for j in range(lenL):
#                 if L[j] == A[i]:
#                     res += 1
#                 else:
#                     res = 0
#         if res == lenA:
#             return True
#         else:
#             return False


# def sub_line(M,L):   #checks in all the lists in a matric=x using function listcheck
#     lenM = len(M)
#     for i in range(len(M)):
#         lcheck = listcheck(M[i],L)
#         if lcheck != None:
#             return True
#         else:
#             return False


# def priority(B):
#     if B.left.key < B.key or B.right.key < B.key :
#         return False
#     else:
#         return priority(B.left) and priority(B.right)  # C'est faux,A revoir la correction !


# def size(B):
#     if B == None:
#         return 1
#     else:
#         return 1 + size(B.left) + size(B.right)



# def perfect_bfs(B):
#     "B not empty tree"
#     if B != None:
#         q = queue.Queue()
#         q.enqueue(B)
#         b = True
#         while not q.isempty():
#             val = q.dequeue()
#             if val.left != None :
#                 q.enqueue(val.left)
#             else:
#                 b = False
#             if val.right != None:
#                 q.enqueue(val.right)
#             else:
#                 b = False
#         if q.isempty() and b:
#             return True
#         else:
#             if q.isempty() and not b:
#                 return False
#     return True

# def height(B):
#     if B == None:
#         return 1
#     else:
#         return 1 + max(height(B.left),height(B.right))

# def perfect(n):
#     if (n == 0):
#         return 1
#     else:
#         return perfect(n-1)+2**(n)

# def perfect_dfs(B):
#     if perfect(height(B)) == size(B):
#         return True
#     else:
#         return False


# def symmetric(B):
#     perf = perfect_bfs(B)
#     if B == perf or B == None:
#         return True
#     else:
#         if B.left != None and B.right != None:
#             symmetric(B.left)
#             symmetric(B.right)

# def height(B):
#     if B == None:
#         return 0
#     else:
#         return 1 + max(height(B.left),height(B.right))

# def perfect_bfs(B):   # checks if a tree is a perfect tree or not
#     'B not empty tree'
#     tree_height = height(B)
#     level = 0
#     q = queue.Queue()
#     if B != None:
#         q.enqueue(B)
#         while not q.isempty():
#             val = q.dequeue()
#             if val.left != None:
#                 q.enqueue(val.left)
#             else:
#                 return False
#             if val.right != None:
#                 q.enqueue(val.right)
#             else:
#                 return False

# def symmetric(M):
#     rowM = len(M)
#     columnM = len(M[0])
#     isSymmetric = True
#     if rowM != columnM:
#         print('Dimensions are not compatible !')
#     else:
#         for i in range(rowM):
#             j = i - 1
#             while j >= 0 and isSymmetric == True:
#                 if M[i][j] != M[j][i]:
#                     return False
#                 j -= 1
#         return isSymmetric


# def exp2str(B):
#     'B not empty tree'
#     if B.left == None and B.right == None:
#         return B.key
#     else:
#         return '(' + exp2str(B.left) + B.key + exp2str(B.right) + ')'

# def to_linear(B):  #gets the 
#     'B not empty tree'
#     if B == None:   
#         return '()'
#     else:
#         s = '(' + str(B.key)
#         return s + to_linear(B.left) +  to_linear(B.right) + ')'

# def width(B):  #gets the maximum width in a binary tree
#     'B not empty tree'
#     if B != None:
#         q = queue.Queue()
#         q.enqueue(B)
#         width = 1
#         numnodes = 1
#         while not q.isempty():
#             numchildren = 0
#             while numnodes > 0:
#                 val = q.dequeue()
#                 if val.left != None:
#                     q.enqueue(val.left)
#                     numchildren += 1
#                 if val.right != None:
#                     q.enqueue(val.right)
#                     numchildren += 1
#                 numnodes -= 1
#             width = max(width,numchildren)
#             numnodes = numchildren
#         return width
#     return 0

# def init(M):  #creates a matrix with values "val"
#     matrix = []
#     for line in range(len(M)):
#         lines = []
#         for column in range(len(M[0])):
#             lines.append(0)
#         matrix.append(lines)
#     return matrix


# def mult_matrices(A,B):  #Technique for multiplying 2 matrices
#     colA = len(A[0])
#     lenB = len(B)
#     if colA != lenA:
#         print('Dimensions are not compatible !')
#     else:
#         lenA = len(A)
#         colB = len(B[0])
#         M = matrix.init(lenA,colA,0)
#         for i in range(lenA):
#             for j in range(colB):
#                 for k in range(colA):
#                     M[i][j] += A[i][k] * B[k][j]
#         return M

# def Siamese(n):  #Magic Square
#     M = matrix.init(n,n,0)
#     i = n - 1
#     j = n // 2
#     M[i][j] = 1
#     for k in range(2,n*n + 1):
#         i2 = (i + 1) % n
#         j2 = (j + 1) % n
#         if M[i2][j2] == 0:
#             (i,j) = (i2,j2)
#         else:
#             i -= 1
#             if i == -1:
#                 i = n - 1
#         M[i][j] = k
#     return M


# def perfect_dfs_depth(B,depth = 0):  
#     if B.left == None:
#         if B.right == None:
#             return depth
#         else:
#             return -1
#     else:
#         if B.right == None:
#             return -1
#         else:
#             ltree = perfect_dfs_depth(B.left,depth += 1)
#             rtree = perfect_dfs_depth(B.right,depth += 1)
#         if ltree = rtree:
#             return ltree
#         else:
#             return -1

# def perfect_dfs(B):
#     if B == None:
#         return True
#     else:
#         return perfect_dfs_depth(B) != -1


# def symetric_vertical(M):  #check if a matrix is symmetric vertically
#     (l,c) = (len(M),len(M[0]))
#     cdiv2 == c // 2
#     i = 0
#     b = False
#     while i < l and not b:
#         j = 0
#         while j < cdiv2 and M[i][j] == M[i][c - j - 1]:
#             j += 1
#         b = (j < cdiv2)
#         i += 1
#     return not b



# def symmetric_diagonal(M):  #check if a matrix is symmetric diagonally
#     (l,c) = len(M),len(M[0])
#     if l != c:
#         return False
#     (i,sym) = 0,True
#     while i < l and sym:
#         j = 0
#         while j < l and sym:
#             sym = M[i][j] == M[j][i]
#             j += 1
#         i += 1
#     return sym

# def symmetric_horizontal(M):  #check if a matrix is symmetric horizontally
#     (l,c) = (len(M),len(M[0]))
#     ldiv2 = l // 2
#     (i,j) = (0,c)
#     while i < ldiv2 and j == c:
#         j = 0
#         while j < c and M[i][j] == M[l - i - 1][j]:
#             j += 1
#         i += 1
#     return j == c


# def transpose(M):   #reverses the Matrix
#     (l,c) = (len(M),len(M[0]))
#     L = []
#     for i in range(c):
#         line = []
#         for j in range(l):
#             line.append(M[j][i])
#         L.append(line)
#     return M




# def Search_Matrix(M,x):  #search x position in Matrix
#     (r,c) = (len(M),len(M[0]))
#     for i in range(r):
#         for j in range(c):
#             if M[i][j] == x:
#                 return (i,j)
#     if M[i][j] >= r:
#         return (-1,-1)        


# def __priority(B):  #checks if the sons's keys of B are smaller or equal to its key
#         b = True
#         if B.left != None:
#             if B.key > B.left.key:
#                 b = False
#             else:
#                 b = __priority(B.left) 
#         if b and B.right != None:
#             b = B.key <= B.right.key and __priority(B.right)
#         return b
    

# def priority(B):
#     return B == None or __priority(B)


# def symmetric(B):  #checks if the binary tree is symmetric
#     return B == None or __symmetric(B.left,B.right)
    
# def __symmetric(B,C):
#     if B == None or C == None:
#         return B == C
#     else:
#         if B.key != C.key:
#             return False
#         else:
#             return __symmetric(B.left,C.right) and __symmetric(B.right,C.left)


# def isSubTree(sB,B): #checks if a sB is a subtree of the binary tree B
#     if sB == None:
#         return True
#     elif B == None:
#         return False
#     else:
#         if sB.key == B.key:
#             return equal(sB,B)
#         else:
#             return isSubTree(sB,B.left) or isSubTree(sB,B.right)

# def equal(B1,B2):  #checks if 2 Binary Trees are Similar
#     if B1 == None:
#         return B2 == None
#     elif B2 == None:
#         return False
#     elif B1.key == B2.key:
#         return equal(B1.left,B2.right) and equal(B1.right,B2.right)
#     else:
#         return False