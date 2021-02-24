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


def distance(list1, list2):
    d = 0
    for i in range(len(list1)):
        d = d + ((list1[i] - list2[i]) ** 2)
    d = d ** 0.5
    return d
