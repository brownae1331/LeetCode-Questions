def searchMatrixVer1(matrix: list[list[int]], target: int) -> bool:
    for row in matrix:
        if target <= row[-1]:
            l, r = 0, len(row) - 1
            while l <= r:
                m = (l + r) // 2
                if row[m] < target:
                    l = m + 1
                elif row[m] > target:
                    r = m - 1
                else:
                    return True
            return False
    return False

def searchMatrixVer2(matrix: list[list[int]], target: int) -> bool:
    top, bot = 0, len(matrix) - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False
    
    row = (top + bot) //2
    l, r = 0, len(matrix[row]) - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False

if __name__ == "__main__":
    output = searchMatrixVer2(matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]], target=10)
    print(output)