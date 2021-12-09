day = 256
count = [[0 for _ in range(9)] for _ in range(day)]
for j in range(day):
    for i in range(0,9):
        ans = 0
        temp = i - 1
        ans = count[j-1][i-1] + ((1 + count[j-1][6]) if temp == -1 else 0)
        count[j][i] = ans

fish_list = input().split(",")
answer = 0
for i in fish_list:
    try:
        answer += int(count[day-1][int(i)])
    except:
        print(count[day-1][int(i)])
print(answer + len(fish_list))