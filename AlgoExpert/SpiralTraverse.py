def spiraltraverse(array):
    result= []
    startRow, endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0])-1
    
    while startRow < endRow  and startCol < endCol:
        
        for column in range(startCol, endCol+1):
            result.append(array[startRow][column])
        
        for row in range(startRow+1, endRow+1):
            result.append(array[row][endCol])
        
        for column in reversed(range(startCol, endCol)):
            result.append(array[endRow][column])
            
        for row in reversed(range(startRow+1, endRow)):
            result.append(array[row][startCol])
        
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
        
    return result
    """
    result=[]
    startRow, endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0])-1

    while startRow <= endRow and startCol <=  endCol:

        for c in range(startCol,endCol+1):
            result.append(array[startRow][c])

        for r in range(startRow+1, endRow+1):
            result.append(array[r][endCol])

        for c in reversed(range(startCol, endCol)):
            result.append(array[endRow][c])

        for r in reversed(range(startRow+1, endRow)):
            result.append(array[r][startCol])

        startRow +=1
        endRow -=1
        startCol +=1
        endCol -=1
    return result
    """

array=[[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
print(spiraltraverse(array))