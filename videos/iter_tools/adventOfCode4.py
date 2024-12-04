with open('/Users/anks/Documents/abc4.txt', 'r') as file:
    grid = [list(a.strip()) for a in file]

word = 'XMAS'


def get_char(grid, grid_idx, line_idx):
    out = ''
    if grid_idx >= 0 and line_idx >= 0:
        try:
            out = grid[grid_idx][line_idx]
        except:
            out = ''
    return out


def get_combinations(grid):
    all_combinations = []
    for grid_idx in range(0, len(grid)):
        for line_idx in range(0, len(grid[grid_idx])):
            forward = get_char(grid, grid_idx, line_idx) + get_char(grid, grid_idx, line_idx + 1) + get_char(grid,
                                                                                                             grid_idx,
                                                                                                             line_idx + 2) + get_char(
                grid, grid_idx, line_idx + 3)
            backward = get_char(grid, grid_idx, line_idx) + get_char(grid, grid_idx, line_idx - 1) + get_char(grid,
                                                                                                              grid_idx,
                                                                                                              line_idx - 2) + get_char(
                grid, grid_idx, line_idx - 3)
            forward_diagonal = get_char(grid, grid_idx, line_idx) + get_char(grid, grid_idx + 1, line_idx + 1) + get_char(grid,
                                                                                                                  grid_idx + 2,
                                                                                                                  line_idx + 2) + get_char(
                grid, grid_idx + 3, line_idx + 3)
            bottom = get_char(grid, grid_idx, line_idx) + get_char(grid, grid_idx + 1, line_idx) + get_char(grid,
                                                                                                            grid_idx + 2,
                                                                                                            line_idx) + get_char(
                grid, grid_idx + 3, line_idx)
            top = get_char(grid, grid_idx, line_idx) + get_char(grid, grid_idx - 1, line_idx) + get_char(grid,
                                                                                                         grid_idx - 2,
                                                                                                         line_idx) + get_char(
                grid, grid_idx - 3, line_idx)
            reverse_diagonal = get_char(grid, grid_idx, line_idx) + get_char(grid, grid_idx - 1,
                                                                             line_idx - 1) + get_char(grid,
                                                                                                      grid_idx - 2,
                                                                                                      line_idx - 2) + get_char(
                grid, grid_idx - 3, line_idx - 3)

            backward_diagonal = get_char(grid, grid_idx, line_idx) + get_char(grid, grid_idx + 1,
                                                                             line_idx - 1) + get_char(grid,
                                                                                                      grid_idx + 2,
                                                                                                      line_idx - 2) + get_char(
                grid, grid_idx + 3, line_idx - 3)

            backward_reverse_diagonal = get_char(grid, grid_idx, line_idx) + get_char(grid, grid_idx - 1,
                                                                              line_idx + 1) + get_char(grid,
                                                                                                       grid_idx - 2,
                                                                                                       line_idx + 2) + get_char(
                grid, grid_idx - 3, line_idx + 3)

            all_combinations.append(forward)
            all_combinations.append(backward)
            all_combinations.append(forward_diagonal)
            all_combinations.append(bottom)
            all_combinations.append(top)
            all_combinations.append(reverse_diagonal)
            all_combinations.append(backward_diagonal)
            all_combinations.append(backward_reverse_diagonal)
            # print(grid_idx, line_idx, forward, backward, forward_diagonal, bottom, top, reverse_diagonal, backward_diagonal, backward_reverse_diagonal)
    return all_combinations


# print(get_combinations(grid))
all_combinations = get_combinations(grid).count(word)
print(all_combinations)
