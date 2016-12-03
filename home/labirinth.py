directions = ((0, 1, 'S'), (1, 0, 'E'), (0, -1, 'N'), (-1, 0, 'W'))
done = False
def get_exit_route(lab, position=(1, 1), path=[], route=''):
    global done
    if done:
        return

    if position == (10, 10):
        print('Yeah')
        done = True
        print(route)
        return
    print(position)
    for x_inc, y_inc, direction in directions:
        x, y = position
        x += x_inc
        y += y_inc

        if 0 <= y < 12 and 0 <= x < 12 and (x, y) not in path and not lab[x][y]:
            path.append((x, y))
            route += direction
            get_exit_route(lab, position=(x, y), route=route)


get_exit_route([
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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

print('Good')
