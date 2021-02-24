def mean_list(list):
    temp = []
    n = len(list[0])
    for i in range(0, n):
        temp.append(0)

    for i in list:
        for j in range(0, n):
            temp[j] = temp[j] + i[j]

    for i in range(0, n):
        temp[i] = temp[i] / len(list)

    return temp


def distance(list1, list2):
    d = 0
    for i in range(len(list1)):
        d = d + ((list1[i] - list2[i]) ** 2)
    d = d ** 0.5
    return d


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
print(mean_list(tmp))
