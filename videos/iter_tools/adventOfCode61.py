with open('/Users/anks/Documents/abc.txt', 'r') as file:
    grid = [line.strip() for line in file]


def get_direction(move_up, move_down, move_left, move_right):
    direction = ''
    if move_left:
        direction = '<'

    if move_up:
        direction = '^'

    if move_right:
        direction = '>'

    if move_down:
        direction = 'd'

    return direction


def get_char(grid, grid_idx, line_idx):
    ch = 'escape'
    if grid_idx < 0 or line_idx < 0:
        ch = 'escape'
    else:
        try:
            ch = grid[grid_idx][line_idx]
        except:
            ch = 'escape'
    return ch


def get_grid_shape(grid):
    return len(grid), len(grid[0])


def where_is_the_guard(grid):
    for grid_idx in range(0, len(grid)):
        for line_idx in range(0, len(grid[grid_idx])):
            if grid[grid_idx][line_idx] == '^':
                guard_position = (grid_idx, line_idx)
    return guard_position


def escaped(grid, guard_position, obs_grid_cord, obs_line_cord):
    grid_idx, line_idx = guard_position
    max_grid_idx, max_line_idx = get_grid_shape(grid)
    move_right = False
    move_down = False
    move_left = False
    move_up = True


    obs_hit = set()

    while True:
        curr_char = get_char(grid, grid_idx, line_idx)
        if curr_char in '#' or (grid_idx == obs_grid_cord and line_idx == obs_line_cord):

            if (get_direction(move_up, move_down, move_left, move_right), grid_idx, line_idx) in obs_hit:
                break
            else:
                obs_hit.add((get_direction(move_up, move_down, move_left, move_right), grid_idx, line_idx))

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
                return True

            # Guard Initial Position
            if curr_char == '^':
                pass

            if move_up:
                grid_idx = grid_idx - 1
                continue

            if move_right:
                line_idx = line_idx + 1
                continue

            if move_down:
                grid_idx = grid_idx + 1
                continue

            if move_left:
                line_idx = line_idx - 1
                continue

    return False


guard_pos = where_is_the_guard(grid)

obs = set()
for grid_idx in range(0, len(grid)):
    for line_idx in range(0, len(grid[grid_idx])):
        if grid[grid_idx][line_idx] != '#':
            obs_grid_cord, obs_line_cord = grid_idx, line_idx
            if not escaped(grid, guard_pos, obs_grid_cord, obs_line_cord):
                print(obs_grid_cord, obs_line_cord, 'blocked')
                obs.add((obs_grid_cord, obs_line_cord))
            else:
                print(obs_grid_cord, obs_line_cord, 'escaped')
        else:
            pass


print(len(obs))
