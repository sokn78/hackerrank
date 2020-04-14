

grid = [
[1, 1, 0, 0],
[0, 1, 1, 0],
[0, 0, 1, 0],
[1, 0, 0, 0]
]

# find connected components


def maxRegion(grid):

    def get_adjacents(i, j):
        return [(i + delta_i, j + delta_j) for delta_i in [-1, 0, 1] for delta_j in [-1, 0, 1]
                if 0 <= (i + delta_i) < row_nb and 0 <= (j + delta_j) < col_nb and not (delta_i == 0 and delta_j == 0)]

    def regions_attributions(i, j, current_region):
        if ((i, j) not in regions) & (grid[i][j] == 1):
            regions[(i, j)] = current_region
            adjacents = get_adjacents(i, j)
            for (i_adj, j_adj) in adjacents:
                regions_attributions(i_adj, j_adj, current_region)

    regions = dict()
    row_nb = len(grid)
    col_nb = len(grid[0])

    current_region = 0
    for i in range(row_nb):
        for j in range(col_nb):
            regions_attributions(i,j, current_region)
            current_region += 1

    regions_size = dict()

    for region in regions.values():
        regions_size[region] = regions_size.get(region, 0) + 1

    return max(regions_size.values())

maxRegion(grid)

