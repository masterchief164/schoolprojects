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


def closest_farthest(list1, list2, p):
    lmax = []
    lmin = []
    mx = 0
    mn = 1000000
    for i in list1:
        d = distance(i, list2)
        if d > mx:
            lmax = i
            mx = d
        if d < mn:
            lmin = i
            mn = d
    if p:
        return lmax
    return lmin


def is_in_set(l1, l2):
    if l1 in l2:
        return True
    return False


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
