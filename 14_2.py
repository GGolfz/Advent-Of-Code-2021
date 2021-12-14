template = input()
blank = input()
case = {}
for _ in range(100):
    tem,res = input().split(" -> ")
    case[tem] = res
pairs = {}
count = {}
for i in range(len(template) - 1):
    pair = template[i:i+2]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1
    if template[i] in count:
        count[template[i]] += 1
    else:
        count[template[i]] = 1
if template[-1] in count:
    count[template[-1]] += 1
else:
    count[template[-1]] = 1
def get_new_pairs(pairs):
    new_pairs = {}
    for pair in pairs:
        gen = case[pair]
        p1,p2 = pair[0] + gen, gen + pair[1]
        if gen in count:
            count[gen] += int(pairs[pair])
        else:
            count[gen] = int(pairs[pair])
        if p1 in new_pairs:
            new_pairs[p1] += int(pairs[pair])
        else:
            new_pairs[p1] = int(pairs[pair])
        if p2 in new_pairs:
            new_pairs[p2] += int(pairs[pair])
        else:
            new_pairs[p2] = int(pairs[pair])
    return new_pairs

for _ in range(40):
    pairs = get_new_pairs(pairs)
print(max(count.values()) - min(count.values()))