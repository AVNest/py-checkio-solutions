directions = ((1, 0, 'S'), (0, 1, 'E'), (0, -1, 'W'), (-1, 0, 'N'))
final_route = None

def get_exit_route1(lab, position=(1, 1), path=((1, 1)), route=''):
    global final_route
    if final_route:
        return final_route

    if position == (10, 10):
        final_route = route
        return route

    for x_inc, y_inc, direction in directions:
        x, y = position
        x += x_inc
        y += y_inc

        if 0 <= y < 12 and 0 <= x < 12 and (x, y) not in path and not lab[x][y]:
            path += ((x, y), )
            route += direction
            get_exit_route1(lab, (x, y), path, route)

    return final_route

def get_exit_route(lab):
    n = m = 12
    end = (10, 10)
    stack = [(1, 1, '')]
    while stack:
        row, col, route = stack.pop()
        if (row, col) == end:
            return route

        if 0 <= row < m and 0 <= col < n and lab[row][col] == 0:
            stack.append((row-1, col, route+'N'))
            stack.append((row, col-1, route+'W'))
            stack.append((row, col+1, route+'E'))
            stack.append((row+1, col, route+'S'))

        lab[row][col] = 1


assert get_exit_route([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 'SSSSSSSSSEENENNEESEEEESS'

print('Good')
