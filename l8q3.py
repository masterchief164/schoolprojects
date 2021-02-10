def GPA(lst):
    # write your code here..

    q1 = float(lst[1])
    ms = float(lst[2])
    q2 = float(lst[3])
    es = float(lst[4])
    lw = float(lst[5])
    pw = float(lst[6])
    total = (q1 / 20) * .5 + (ms / 50) * 2 + (q2 / 20) * .5 + (es / 100) * 3 + (lw / 100) * 2 + (pw / 50) * 2
    gpa1 = float("%.2f" % total)
    return gpa1


def GRADES(g):
    # write your code here..
    grade1 = ""
    if g > 10:
        return "Invalid GPA"
    elif g == 10:
        return "O"
    elif g >= 9:
        return 'A'
    elif g >= 8:
        return 'B'
    elif g >= 7:
        return 'C'
    elif g >= 6:
        return 'D'
    elif g >= 5.5:
        return "Pass"
    elif 5.5 > g >= 0:
        return "Fail"
    else:
        return "Invalid GPA"


inp = []
try:
    f = open('marks.txt', 'r')
except FileNotFoundError:
    print("File doesn't exist")
else:
    c = 0
    for i in f:
        k = i[:len(i) - 1]
        inp.append(k.split())
    f.close()
for i in range(2, len(inp)):
    f = True
    for j in range(len(inp[i]) - 2):
        if inp[i][j] == "None":
            f = False
    if f:
        gpa = GPA(inp[i])
        inp[i][7] = str(gpa)
        grade = GRADES(gpa)
        inp[i][8] = grade
inp1 = inp[2:]
inp1 = sorted(inp1, key=lambda l: l[0])
inp = inp[:2]
inp.extend(inp1)

try:
    f = open("marks.txt", "w")
except:
    print('Failed to update the file.')
else:
    for i in inp:
        s1 = ""
        for j in i:
            s1 = s1 + " " + j
        s1 += "\n"
        f.write(s1)
    f.close()
