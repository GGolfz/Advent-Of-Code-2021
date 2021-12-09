arr = []
for i in range(100):
    line = list(input())
    arr.append(line)
sum_risk = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == 0:
            if j == 0:
                if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j+1]:
                    sum_risk += int(arr[i][j])+1
            elif j == len(arr[i])-1:
                if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1]:
                    sum_risk += int(arr[i][j])+1
            else:
                if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1] and arr[i][j] < arr[i][j+1]:
                    sum_risk += int(arr[i][j])+1
        elif i == len(arr)-1:
            if j == 0:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i][j+1]:
                    sum_risk += int(arr[i][j])+1
            elif j == len(arr[i])-1:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i][j-1]:
                    sum_risk += int(arr[i][j])+1
            else:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i][j-1] and arr[i][j] < arr[i][j+1]:
                    sum_risk += int(arr[i][j])+1
        else:
            if j == 0:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j+1]:
                    sum_risk += int(arr[i][j])+1
            elif j == len(arr[i])-1:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1]:
                    sum_risk += int(arr[i][j])+1
            else:
                if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1] and arr[i][j] < arr[i][j+1]:
                    sum_risk += int(arr[i][j])+1
print(sum_risk)