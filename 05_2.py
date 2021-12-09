lines = 500
arr = [[0 for _ in range(1000)] for _ in range(1000)]
for i in range(lines):
    temp = input().split(' -> ')
    f = temp[0].split(',')
    t = temp[1].split(',')
    fc = int(f[0])
    fr = int(f[1])
    tc = int(t[0])
    tr = int(t[1])
    if fc == tc:
        minr = min(fr, tr)
        maxr = max(fr, tr)
        for j in range(minr, maxr + 1):
            arr[j][fc] += 1
    elif fr == tr:
        minc = min(fc, tc)
        maxc = max(fc, tc)
        for j in range(minc, maxc + 1):
            arr[fr][j] += 1
    else:
        if fc < tc and fr < tr:
            step = min(tc - fc, tr - fr)
            for j in range(step+1):
                arr[fr + j][fc + j] += 1
        elif fc > tc and fr > tr:
            step = min(fc - tc, fr - tr)
            for j in range(step+1):
                arr[fr - j][fc - j] += 1
        elif fc < tc and fr > tr:
            step = min(tc - fc, fr - tr)
            for j in range(step+1):
                arr[fr - j][fc + j] += 1
        elif fc > tc and fr < tr:
            step = min(fc - tc, tr - fr)
            for j in range(step+1):
                arr[fr + j][fc - j] += 1
        else:
            print(temp)
        
count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > 1:
            count+=1
print(count)