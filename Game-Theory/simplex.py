INT_MAX = 100001

def input_from_user():
    print("Input the size of the matrix:")
    #get two numbers from the user
    n,m = map(int,input().split())
    #get the matrix from the user
    matrix = [[int(x) for x in input().split()] for i in range(n)]
    #print the matrix
    #print("The matrix is:")
    #print(matrix)
    return n,m,matrix

def addMargins(matrix,n,m):
    for i in range(n):
        matrix[i].append(1)
    matrix.append([-1 for i in range(m+1)])
    matrix[n][m]=0
    return matrix,n+1,m+1
    
def findDominantRow(matrix,n,m):
    #find the dominant row
    number_of_rows = n
    for i1 in range(number_of_rows):
        for i2 in range(i+1,number_of_rows):
            #i1 is dominant row
            for j in range(m):
                if matrix[i1][j]<matrix[i2][j]:
                    break
            #delete the row i2
            else:
                del matrix[i2]
                number_of_rows-=1
            
            #i2 is dominant row
            for j in range(m):
                if matrix[i2][j]<matrix[i1][j]:
                    break
            #delete the row i2
            else:
                del matrix[i2]
                number_of_rows-=1
    return matrix,number_of_rows,m

def findDominantColumn(matrix,n,m):
    
    number_of_columns = m
    #find the dominant column in the matrix
    for j1 in range(number_of_columns):
        for j2 in range(j+1,number_of_columns):
            #j1 is dominant column
            for i in range(n):
                if matrix[i][j1]>matrix[i][j2]:
                    break
            #delete the column j2
            else:
                for i in range(n):
                    del matrix[i][j2]
                number_of_columns-=1
            #j2 is dominant column
            for i in range(n):
                if matrix[i][j2]>matrix[i][j1]:
                    break
            #delete the column j1
            else:
                for i in range(n):
                    del matrix[i][j1]
                number_of_columns-=1
    return matrix,n,number_of_columns

def findAllDominantRowAndColumn(matrix,n,m):
    matrix,n,m = findDominantRow(matrix,n,m)
    matrix,n,m = findDominantColumn(matrix, n, m)

def findSaddlePoint(matrix,n,m):
    #find the saddle point
    #find the minimum in each row
    row_mins = []
    for i in range(n):
        row_mins.append(min(matrix[i]))
    #find the maximum in each column
    columns_maxs = []
    for j in range(m):
        columns_maxs.append(max([matrix[i][j] for i in range(n)]))
    #find the saddle points
    '''print(row_mins)
    print(columns_maxs)'''
    saddle_points = []
    for i in range(n):
        for j in range(m):
            if row_mins[i]==columns_maxs[j]:
                saddle_points.append([i,j])
    return saddle_points
    

def makeAllElementsPositive(matrix,n,m):
    #make all elements of matrix positive by adding
    minVal = INT_MAX
    for i in range(n):
        for j in range(m):
            minVal = min(matrix[i][j],minVal)
    #add MinVal to all elements of matrix
    minVal*=-1
    for i in range(n):
        for j in range(m):
            matrix[i][j]+=minVal
    return matrix, minVal

def changeLabels(labelArray,i,j):
    labelArray[0][i], labelArray[1][j] =  labelArray[1][j], labelArray[0][i]
    return labelArray

def makeLabelArray(n,m):
    x = [i+1 for i in range(n)]
    y = [-(i+1) for i in range(m)]
    labelArray = [x,y]
    return labelArray

def validCols(matrix,n,m):
    valid_Cols = []
    for j in range(m-1):
        if matrix[n-1][j]<0:
            valid_Cols.append(j)
    status = True
    if len(valid_Cols)==0:
        status = False
    return status, valid_Cols

def findValidJoint(matrix,n,m,valid_Cols):
    status = False
    for j in valid_Cols:
        if not(status):
            min_Index = -1
            min_Val = INT_MAX
            for i in range(n-1):
                point = matrix[i][j]
                if point>0:
                    status = True
                    col = j
                    row_Margin = matrix[i][m-1]
                    temp = row_Margin/point
                    if temp<min_Val:
                        min_Val = temp
                        min_Index = i
        else:
            row = min_Index
            return status,col,row
    if status:
        row = min_Index
        return status,col,row
    else:
        return status,-1,-1
                
def newMatrixOnJoint(matrix,n,m,row,col):
    newMatrix = [[matrix[i][j] for j in range(m)] for i in range(n)]
    point = matrix[row][col]
    newMatrix[row][col]=(1/point)
    #changeRows
    for j in range(m):
        if j!=col:
            newMatrix[row][j] = matrix[row][j]/point
    #changeCols
    for i in range(n):
        if i!=row:
            newMatrix[i][col] = -(matrix[i][col]/point)
    #change others
    for i in range(n):
        if i==row:
            continue
        for j in range(m):
            if j==col:
                continue
            r = matrix[row][j]
            c = matrix[i][col]
            newMatrix[i][j] = matrix[i][j] - ((r*c)/point)
    
    return newMatrix

def findV(matrix,n,m,posVal):
    return (1/matrix[n-1][m-1])-posVal

def findStrategy(matrix,n,m,labelArray):
    arrStrategyX = [0 for i in range(n-1)]
    arrStrategyY = [0 for j in range(m-1)]
    lastPoint = matrix[n-1][m-1]
    #find Strategy X
    for j in range(m-1):
        lx = labelArray[1][j]
        if lx>0:
            arrStrategyX[lx-1]= (matrix[n-1][j]/lastPoint)
            
    #find Strategy Y
    for i in range(n-1):
        ly = labelArray[0][i]
        if ly<0:
            ly *= -1
            arrStrategyY[ly-1]=(matrix[i][m-1]/lastPoint)
            
    return arrStrategyX,arrStrategyY
    
    
if __name__ == "__main__":
    print("Everything passed")
    
    n,m, matrix = input_from_user()
    matrix,posVal = makeAllElementsPositive(matrix, n, m)
    labelArray = makeLabelArray(n, m)
    matrix,n,m = addMargins(matrix, n, m)
    while(True):
        status, valid_Cols = validCols(matrix, n, m)
        if not(status):
            break
        status, row, col = findValidJoint(matrix, n, m, valid_Cols)
        if not(status):
             break
        labelArray = changeLabels(labelArray, row, col)
        matrix = newMatrixOnJoint(matrix, n, m, row, col)
       
    
    #print(matrix)
    #print(labelArray)
    gameVal = findV(matrix, n, m, posVal)
    X, Y = findStrategy(matrix, n, m, labelArray)
    print("The Game Value is:     ",round(gameVal, 2))
    print()
    print("Strategy for the X is:   ")
    for i in range(len(X)):
        print("X",i+1,"  is:   ",round(X[i],2),sep="")
    print()
    print("Strategy for the Y is:   ")
    for i in range(len(Y)):
        print("Y",i+1,"  is:   ",round(Y[i],2),sep="")