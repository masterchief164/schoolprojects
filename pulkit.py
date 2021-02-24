def mean_list(l):
    mean_l = []
    length_of_each_list = len(l[0])
    for i in range(0, length_of_each_list):
        mean_l.append(0)

    for i in l:
        for j in range(0, length_of_each_list):
            mean_l[j] = mean_l[j] + i[j]

    for i in range(0, length_of_each_list):
        mean_l[i] = mean_l[i] / len(l)

    return mean_l

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
    if l1 not in l2:
        return False
    return True

myfile = open("lists.txt", 'r')
final_list = []
keylist = (list(map(float, input().split(','))))
for i in myfile:
    final_list.append(i.strip("\\n"))
f_list = []
for i in final_list:
    #changing each value of the list to float
    f_list.append(list(map(float, i.split(','))))
print("Mean_list: ", end=" ")
m_list = mean_list(f_list)
for i in m_list:
    print(i, end=" ")
print()
print("Distance between key_list and mean_list: ", distance(m_list, keylist))
if is_in_set(m_list, f_list):
    print("mean_list is present in the File")
else:
    print("mean_list is not present in the File")
d1 = closest_farthest(f_list, keylist, False)
d2 = closest_farthest(f_list, keylist, True)
print("Closest List: ",end=" ")
for i in d1:
    print(i,end=" ")
print()
print("Distance between closest list and keylist:", distance(d1, keylist))
print("Farthest list: ",end=" ")
for i in d2:
    print(i,end=" ")
print()
print("Distance between farthest list and key list:", distance(d2,keylist))
print("Distance between closest list and farthest list: ", distance(d1,d2))