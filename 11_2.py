arr = []
for i in range(10):
    line = input()
    line = [int(x) for x in line]
    arr.append(line)
count = 0
flash_list = set()
def print_table(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=' ')
        print()

def increase(arr,j,k):
    answer = [i.copy() for i in arr]
    if j >= 0 and j < len(arr) and k >= 0 and k < len(arr[j]):
        answer[j][k] += 1
    return answer

def flash(arr,j,k,flash_list):
    answer = [i.copy() for i in arr]
    temp_flash = flash_list.copy()
    if j >= 0 and j < len(arr) and k >= 0 and k < len(arr[j]) and answer[j][k] > 9 and str(j) + ',' + str(k) not in temp_flash:
        global count
        count+=1
        answer = increase(answer,j-1,k-1)
        answer = increase(answer,j-1,k)
        answer = increase(answer,j-1,k+1)
        answer = increase(answer,j,k-1)
        answer = increase(answer,j,k+1)
        answer = increase(answer,j+1,k-1)
        answer = increase(answer,j+1,k)
        answer = increase(answer,j+1,k+1)
        temp_flash.add(str(j) + ',' + str(k))
        answer,temp_flash = flash(answer,j-1,k-1,temp_flash)
        answer,temp_flash = flash(answer,j-1,k,temp_flash)
        answer,temp_flash = flash(answer,j-1,k+1,temp_flash)
        answer,temp_flash = flash(answer,j,k-1,temp_flash)
        answer,temp_flash = flash(answer,j,k+1,temp_flash)
        answer,temp_flash = flash(answer,j+1,k-1,temp_flash)
        answer,temp_flash = flash(answer,j+1,k,temp_flash)
        answer,temp_flash = flash(answer,j+1,k+1,temp_flash)
    return answer,temp_flash
i=0
while True:
    flash_list = set()
    for j in range(len(arr)):
        for k in range(len(arr[j])):
            arr[j][k] += 1
    for j in range(len(arr)):
        for k in range(len(arr[j])):
            if arr[j][k] > 9:
                arr,flash_list = flash(arr,j,k,flash_list)
    flash_list = sorted(flash_list)
    for fl in flash_list:
        j,k = [int(x) for x in fl.split(",")]
        arr[j][k] = 0
    if len(flash_list) == len(arr) * len(arr[0]):
        print(i+1)
        break
    i+=1
print_table(arr)
print()
print(count)