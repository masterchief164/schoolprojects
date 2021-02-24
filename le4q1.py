def mean_list(list):
    temp = []
    n = len(list[0])
    for i in range(0, len(list)):
        temp.append(0)

    for i in list:
        t = 0
        for j in i:
            temp[t] = temp[t] + j
            t += 1

    for i in range(0, len(temp)):
        temp[i] = temp[i] / n


f = open("lists.txt", 'r')
c = 0
lst = []
key_lst = (list(map(float, input().split(','))))
for i in f:
    c += 1
    lst.append(i.strip("\\n"))
tmp = []
for i in lst:
    tmp.append(list(map(float, i.split(','))))
print(tmp)
print(key_lst)

