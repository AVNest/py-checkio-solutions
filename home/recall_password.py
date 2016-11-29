def recall_password(cipher_map, table):
    n = m = 4
    password = ''
    for _ in range(0, 360, 90):
        password += ''.join(table[i][j] for i, row in enumerate(cipher_map)
                                        for j, val in enumerate(row) if val == 'X')
        cipher_map = [[cipher_map[j][i] for j in range(m-1, -1, -1)] for i in range(n)]

    return password

assert recall_password(
            ('X...',
             '..X.',
             'X..X',
             '....'),
            ('itdf',
             'gdce',
             'aton',
             'qrdi')) == 'icantforgetiddqd'

assert recall_password(
            ('....',
             'X..X',
             '.X..',
             '...X'),
            ('xhwc',
             'rsqx',
             'xqzz',
             'fyzr')) == 'rxqrwsfzxqxzhczy'
print('Good')
