def preprocess_input():
    data = {}
    for _ in range(25):
        src,des = input().split('-')
        if src == "start" or des == "start":
            if src == "start":
                if des not in data:
                    data[des] = []
                data[des].append("start")
            else:
                if src not in data:
                    data[src] = []
                data[src].append("start")
        elif src == "end" or des == "end":
            if src == "end":
                if "end" not in data:
                    data["end"] = []
                data["end"].append(des)
            else:
                if "end" not in data:
                    data["end"] = []
                data["end"].append(src)
        else:
            if src not in data:
                data[src] = []
            data[src].append(des)
            if des not in data:
                data[des] = []
            data[des].append(src)
    return data

def visit(data, path):
    if path[0] == "end" and path[-1] == "start":
        return 1
    count = 0
    for node in data[path[-1]]:
        if node != path[0] and (node.isupper() or (node.islower() and node not in path)):
            count += visit(data, path + [node])
    return count
print(visit(preprocess_input(), ["end"]))