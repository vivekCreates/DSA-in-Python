def paths(arr, r, c):
    n = len(arr)
    m = len(arr[0])

    if r < 0 or c < 0 or r >= n or c >= m:
        return -1000000  

    if r == n - 1:
        return arr[r][c]

    left = paths(arr, r + 1, c - 1)
    down = paths(arr, r + 1, c)
    right = paths(arr, r + 1, c + 1)

    return arr[r][c] + max(left, down, right)


mat = [[2, 7],
       [9, 15]]

ans = max(paths(mat, 0, c) for c in range(len(mat[0])))
print("ans:", ans)
