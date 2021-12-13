data = []
max_x = 0
max_y = 0
fold = []
for i in range(910):
    line = input()
    if line.startswith('fold'):
        axis,pos = line.split("fold along ")[1].split("=")
        fold.append((axis,int(pos)))
    elif line == "":
        continue
    else:
        x,y = line.split(',')
        if int(x) > max_x:
            max_x = int(x)
        if int(y) > max_y:
            max_y = int(y)
        data.append((int(x),int(y)))
map = [["." for _ in range(max_x+1)] for _ in range(max_y+1)]
for i in range(max_y+1):
    for j in range(max_x+1):
        if (j,i) in data:
            map[i][j] = '#'

for f in fold:
    axis,pos = f
    if axis == 'x':
        for i in range (max_y+1):
            for j in range(0, pos+1):
                if j == pos:
                    map[i][j] = '-'
                elif  2*pos - j < len(map[0]) and map[i][2*pos - j] == '#':
                    map[i][j] = '#'
        temp_map = [["." for _ in range(0,pos)] for _ in range(max_y+1)]
        for i in range(max_y+1):
            for j in range(0,pos):
                temp_map[i][j] = map[i][j]
        map = temp_map
        max_x = pos - 1
    elif axis == 'y':
        for i in range(0, pos+1):
            for j in range(max_x+1):
                if i == pos:
                    map[i][j] = '-'
                elif 2*pos - i < len(map) and map[2*pos - i][j] == '#':
                    map[i][j] = '#' 
        temp_map = [["." for _ in range(max_x+1)] for _ in range(0,pos)]
        for i in range(0,pos):
            for j in range(max_x+1):
                temp_map[i][j] = map[i][j]
        map = temp_map
        max_y = pos - 1

for i in range(max_y+1):
    for j in range(max_x+1):
        if map[i][j] == '.':
            print(' ',end='')
        else:
            print(map[i][j], end='')
    print()