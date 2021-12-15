data = []
for i in range(100):
    line = [int(j) for j in input()]
    data.append(line)
expanded = [[0 for _ in range(5*len(data[0]))] for _ in range(5*len(data))]

for x in range(len(expanded)):
	for y in range(len(expanded[0])):
		dist = x//len(data) + y//len(data[0])
		newval = data[x%len(data)][y%len(data[0])]
		for i in range(dist):
			newval+=1
			if newval==10:
				newval=1
		expanded[x][y] = newval

data = expanded
des = (len(data) - 1,len(data[0]) - 1)
current = (0,0,0)
priority_queue = []
finish = False
visited = {}
while not finish:
    if current[0] == des[0] and current[1] == des[1]:
        finish = True
    else:
        if current[0] < des[0]:
            if str(current[0] + 1) + "," + str(current[1]) in visited.keys() and visited[str(current[0] + 1) + "," + str(current[1])] <= data[current[0] + 1][current[1]] +  current[2]:
                pass
            else:
                priority_queue.append((current[2] + data[current[0] + 1][current[1]], current[0] +1,current[1]))
                visited[str(current[0] + 1) + "," + str(current[1])] = current[2] + data[current[0] + 1][current[1]]
        if current[1] < des[1]:
            if str(current[0]) + "," + str(current[1] + 1) in visited.keys() and visited[str(current[0]) + "," + str(current[1] + 1)] <= data[current[0]][current[1] + 1] + current[2]:
                pass
            else:
                priority_queue.append((current[2] + data[current[0]][current[1] + 1], current[0],current[1] + 1))
                visited[str(current[0]) + "," + str(current[1] + 1)] = current[2] + data[current[0]][current[1] + 1]
        if current[0] > 0:
            if str(current[0] - 1) + "," + str(current[1]) in visited.keys() and visited[str(current[0] - 1) + "," + str(current[1])] <= data[current[0] - 1][current[1]] + current[2]:
                pass
            else:
                priority_queue.append((current[2] + data[current[0] - 1][current[1]], current[0]-1,current[1]))
                visited[str(current[0] - 1) + "," + str(current[1])] = current[2] + data[current[0] - 1][current[1]]
        if current[1] > 0:
            if str(current[0]) + "," + str(current[1] - 1) in visited.keys() and visited[str(current[0]) + "," + str(current[1] - 1)] <= data[current[0]][current[1] - 1] + current[2]:
                pass
            else:
                priority_queue.append((current[2] + data[current[0]][current[1] - 1], current[0],current[1] - 1))
                visited[str(current[0]) + "," + str(current[1] - 1)] = current[2] + data[current[0]][current[1] - 1]
        priority_queue = sorted(priority_queue)
        temp = priority_queue[0]
        current = (temp[1],temp[2],temp[0])
        priority_queue = priority_queue[1:]
print(current[2])