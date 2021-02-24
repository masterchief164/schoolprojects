f = open("list.txt", 'r')
c = 0
lst = []
for i in f:
    c += 1
    lst.append(i.strip("\\n"))
