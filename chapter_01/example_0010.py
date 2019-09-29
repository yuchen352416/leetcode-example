#!/usr/bin/python3


# 有效的数独
def isValidSudoku(board: list) -> bool:
    container = {}
    for i in range(9):
        rowContainer = []
        columnContainer = []
        for j in range(9):
            rowItem = board[i][j]
            columnItem = board[j][i]
            # 行
            if "." != rowItem:
                if rowContainer.__contains__(rowItem):
                    return False
                else:
                    rowContainer.append(rowItem)
            # 列
            if "." != columnItem:
                if columnContainer.__contains__(columnItem):
                    return False
                else:
                    columnContainer.append(columnItem)
            # 块
            key = (i // 3).__str__() + (j // 3).__str__()
            item = board[i][j]
            if "." != item:
                if container.keys().__contains__(key):
                    arr = container[key]
                    if arr.__contains__(item):
                        return False
                    else:
                        arr.append(item)
                else:
                    arr = []
                    arr.append(item)
                    container[key] = arr
    return True


if __name__ == '__main__':
    arr = [
        ["5", "3", "1", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(arr)
    result = isValidSudoku(arr)
    print(result)
