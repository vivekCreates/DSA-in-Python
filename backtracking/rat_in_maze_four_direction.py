def ways(sr, sc, er, ec, arr,res):
    # out of bounds
    if sr < 0 or sc < 0 or sr > er or sc > ec:
        return 0

    # destination reached
    if sr == er and sc == ec:
        print(res,end='\n')
        return 1

    # already visited
    if arr[sr][sc] == -1:
        return 0

    # mark visited
    arr[sr][sc] = -1

    right = ways(sr, sc + 1, er, ec, arr,res+"R")
    down  = ways(sr + 1, sc, er, ec, arr,res+"D")
    left  = ways(sr, sc - 1, er, ec, arr,res+"L")
    up    = ways(sr - 1, sc, er, ec, arr,res+"U")

    # unmark (backtrack)
    arr[sr][sc] = 1

    return right + down + left + up


def ways_to_reached_destination(m, n):
    arr = [[1 for _ in range(n)] for _ in range(m)]
    return ways(0, 0, m - 1, n - 1, arr,"")


ans = ways_to_reached_destination(3, 3)
print("ways:", ans)
