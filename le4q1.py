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


def is_in_set(l2, l1):
    for i in l1:
        f = True
        for j in range(len(i)):
            if i[j] != l2[j]:
                f = False
        if f:
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
print("Mean List is", end=" ")
k = mean_list(tmp)
for i in k:
    print(i, end=" ")
print()
print("Distance between key_list and mean_list is", distance(k, key_lst))
if is_in_set(k, tmp):
    print("mean_list is present in the provided set of lists")
else:
    print("mean_list is not present in the provided set of lists")
clo = closest_farthest(tmp, key_lst, False)
far = closest_farthest(tmp, key_lst, True)
print("the closest list is", end=" ")
for i in clo:
    print(i, end=" ")
print()
print("the farthest list is", end=" ")
for j in far:
    print(j, end=" ")
print()
print("The  distance between the closest list and the farthest list", distance(clo, far))
print("The  distance between the closest list and the key list", distance(clo, key_lst))
print("The  distance between the key list and the farthest list", distance(key_lst, far))
