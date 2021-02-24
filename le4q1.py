f = open("lists.txt", 'r')
c = 0
lst = []
key_lst = input().split(",")
for i in f:
    c += 1
    lst.append(i.strip("\\n"))
