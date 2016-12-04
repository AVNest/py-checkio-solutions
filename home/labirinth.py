directions = ((1, 0, 'S'), (0, 1, 'E'), (0, -1, 'W'), (-1, 0, 'N'))
final_route = None

def get_exit_route(lab, position=(1, 1), path=((1, 1)), route=''):
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
            get_exit_route(lab, (x, y), path, route)

    return final_route

def get_exit_route1(lab):
    def visit_point(i, j, direction):
        if 0 <= i < 12 and 0 <= j < 12 and (i, j) not in path and not lab[i][j]:
            stack.append((i, j, route+direction))

    end = (10, 10)
    route = ''
    path = []
    stack = [(1, 1, '')]
    while stack:
        r, c, route = stack.pop()
        if (r, c) == end:
            print(route)
            return route

        path.append((r, c))
        visit_point(r-1, c, 'N')
        visit_point(r, c-1, 'W')
        visit_point(r, c+1, 'E')
        visit_point(r+1, c, 'S')


assert get_exit_route1([
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
