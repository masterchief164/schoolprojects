names, acc, sit, ratio = input().split("###")
names = names.split(" ")
acc = acc.split(" ")
per = ratio.split(" ")
s = ""
if s == "True":
    index = [0, (int(len(acc) * float(per[0]) / 100)),
             (int(len(acc) * float(per[1]) / 100)) + (int(len(acc) * float(per[0]) / 100)), (len(acc))]
    for i in range(3):

        for j in range(index[i], index[i + 1]):
            s += (" " + names[j])
            s += " " + acc[j]
        s += "###"
else:
    index = [0, (int(len(acc) * float(per[0]) / 100)), (len(acc))]

    for i in range(2):
        for j in range(index[i], index[i + 1]):
            s += (" " + names[j])
            s += " " + acc[j]
        s += "###"
s = s.rstrip("#")
print(s)
