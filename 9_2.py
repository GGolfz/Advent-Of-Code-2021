arr = []
for i in range(100):
    line = list(map(int,list(input())))
    arr.append(line)
basin = {}
def add_basin(i,j,start):
    if i>=0 and j>=0 and i<len(arr) and j<len(arr[0]) and arr[i][j] != 9:
        if start not in basin:
            basin[start] = set()
        basin[start].add(str(i)+','+str(j))
        try:
            if arr[i][j] < arr[i][j+1]:
                add_basin(i,j+1,start)
        except:
            pass
        try:
            if arr[i][j] < arr[i+1][j]:
                add_basin(i+1,j,start)
        except:
            pass
        try:
            if arr[i][j] < arr[i][j-1]:
                add_basin(i,j-1,start)
        except:
            pass
        try:
            if arr[i][j] < arr[i-1][j]:
                add_basin(i-1,j,start)
        except:
            pass

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == 0:
            if j == 0:
                if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j+1]:
                    add_basin(i,j,str(i)+','+str(j))
            elif j == len(arr[i])-1:
                if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1]:
                    add_basin(i,j,str(i)+','+str(j))
            else:
                if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1] and arr[i][j] < arr[i][j+1]:
                    add_basin(i,j,str(i)+','+str(j))
        elif i == len(arr)-1:
            if j == 0:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i][j+1]:
                    add_basin(i,j,str(i)+','+str(j))
            elif j == len(arr[i])-1:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i][j-1]:
                    add_basin(i,j,str(i)+','+str(j))
            else:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i][j-1] and arr[i][j] < arr[i][j+1]:
                    add_basin(i,j,str(i)+','+str(j))
        else:
            if j == 0:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j+1]:
                    add_basin(i,j,str(i)+','+str(j))
            elif j == len(arr[i])-1:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1]:
                    add_basin(i,j,str(i)+','+str(j))
            else:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1] and arr[i][j] < arr[i][j+1]:
                    add_basin(i,j,str(i)+','+str(j))
ans = []
for i in basin.keys():
    ans.append(len(basin[i]))
ans.sort(reverse=True)
print(ans[0] * ans[1] * ans[2])
