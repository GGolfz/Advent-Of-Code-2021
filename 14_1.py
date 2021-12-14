template = input()
blank = input()
case = {}
for _ in range(100):
    tem,res = input().split(" -> ")
    case[tem] = res
str = ""
for _ in range(10):
    str = ""
    count = {}
    for i in range(1,len(template)):
        pair = template[i-1:i+1]
        if pair in case:
            insert = case[pair]
            str += pair[0] + insert
            if pair[0] in count:
                count[pair[0]] += 1
            else:
                count[pair[0]] = 1
            if insert in count:
                count[insert] += 1
            else:
                count[insert] = 1
    if template[-1] in count:
        count[template[-1]] += 1
    else:
        count[template[-1]] = 1
    template = str + template[-1]
    print(max(count.values()) - min(count.values()))