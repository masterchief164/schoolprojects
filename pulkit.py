def calc_gpa(l):
    q1 = l[1]
    ms = l[2]
    q2 = l[3]
    es = l[4]
    lb = l[5]
    p = l[6]
    q1 = float(q1)
    ms = float(ms)
    q2 = float(q2)
    es = float(es)
    lb = float(lb)
    p = float(p)
    total = (q1 / 20) * .5 + (ms / 50) * 2 + (q2 / 20) * .5 + (es / 100) * 3 + (lb / 100) * 2 + (p / 50) * 2
    gpa = float("%.2f" % total)
    return gpa


def calc_grade(g):
    grade1 = ""
    if g > 10:
        return "Invalid GPA"
    elif g == 10:
        return 'O'
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


list = []
try:
    marks_file = open("marks.txt", "r")
except:
    print("File doesn't exist")
else:
    for i in marks_file:
        list.append(i[:len(i) - 1].split())
    for i in range(2, len(list)):
        l = list[i][:len(list[i]) - 2]
        if "NONE" not in l:
            g = calc_gpa(l)
            grade = calc_grade(g)
            list[i][7] = str(g)
            list[i][8] = grade
    print(list)
