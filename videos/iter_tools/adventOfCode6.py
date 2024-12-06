with open('/Users/anks/Documents/abc.txt', 'r') as file:
    grid = [line.strip() for line in file]


def get_char(grid, grid_idx, line_idx):
    ch = 'escape'
    try:
        ch = grid[grid_idx][line_idx]
    except:
        pass
    return ch

def where_is_the_guard(grid):
    for grid_idx in range(0, len(grid)):
        for line_idx in range(0, len(grid[grid_idx])):
            if grid[grid_idx][line_idx] == '^':
                guard_position = (grid_idx, line_idx)
    return guard_position

def safe_path_index(grid, guard_position):
    grid_idx, line_idx = guard_position
    move_right = False
    move_down = False
    move_left = False
    move_up = True

    safe_cordinates = []
    print('Guard: ', guard_position)

    while True:
        curr_char = get_char(grid, grid_idx, line_idx)
        if curr_char == '#':
            if move_up:
                move_right = True
                move_up = False
                grid_idx = grid_idx + 1
                line_idx = line_idx + 1
                continue

            if move_right:
                move_down = True
                move_right = False
                line_idx = line_idx - 1
                grid_idx = grid_idx + 1
                continue

            if move_down:
                move_left = True
                move_down = False
                grid_idx = grid_idx - 1
                line_idx = line_idx - 1
                continue

            if move_left:
                move_up = True
                move_left = False
                line_idx = line_idx + 1
                grid_idx = grid_idx - 1
                continue
        else:

            if curr_char == 'escape':
                break

            # Guard Initial Position
            if curr_char == '^':
                pass

            safe_cordinates.append((grid_idx, line_idx))
            if move_up:
                grid_idx = grid_idx - 1

            if move_right:
                line_idx = line_idx + 1

            if move_down:
                grid_idx =  grid_idx + 1

            if move_left:
                line_idx = line_idx - 1

    return safe_cordinates



guard_pos = where_is_the_guard(grid)
coordinates = safe_path_index(grid, guard_pos)
print(len(set(coordinates)))