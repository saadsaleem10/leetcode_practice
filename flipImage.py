def flipAndInvertImage(self, grid: list[list[int]]) -> list[list[int]]:
    for i in range(len(grid)):
        grid[i]=grid[i][::-1]
        for j in range(len(grid[0])):
            grid[i][j]^=1
    return grid