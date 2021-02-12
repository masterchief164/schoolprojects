inp = input()
file1 = []
file2 = []
print('Execution Started.')
try:
    if not inp:
        raise Exception('No input. Stopping execution.')
except Exception as e:
    print(e)
else:
    print('Processing the first file.')
    try:
        inp = inp.split()
        f = open(inp[0], 'r')
    except FileNotFoundError:
        print('Unable to open the file', inp[0])
    else:
        print('Reading data from file', inp[0])
        for i in f:
            if i.rstrip("\\n") not in file1:
                file1.append(i.rstrip("\\n").split())

        tmp = file1[2:]
        tmp = sorted(tmp, key=lambda l: l[1])
        file1 = file1[:2]
        file1.extend(tmp)
        f.close()
    try:
        f = open("details.txt", 'w')
    except:
        print("Unable to create the file")
    else:
        for i in file1:
            s1 = ""
            for j in i:
                s1 = s1 + " " + j
            s1 += "\n"
            f.write(s1)
        f.close()
    print('Write operation successful.')
    try:
        f = open(inp[1], 'r')
    except FileNotFoundError:
        print('Unable to open the file', inp[1])
    else:
        print('Reading data from file', inp[1])
        for i in f:
            file2.append(i.rstrip("\\n").split())
        file2 = file2[2:]
        f.close()
        f = 0
        for i in file2:
            if i not in file1:
                file1.append(i)
                f = 1
        if f == 1:
            tmp = file1[2:]
            tmp = sorted(tmp, key=lambda l: l[1])
            file1 = file1[:2]
            file1.extend(tmp)
            try:
                f = open("details.txt", "w")
            except:
                print("Unable to create the file")
            else:
                for i in file1:
                    s1 = ""
                    for j in i:
                        s1 = s1 + " " + j
                    s1 += "\n"
                    f.write(s1)
                print('Updated the file details.txt.')
                print('All files closed.')
finally:
    for i in file1:
        s1 = ""
        for j in i:
            s1 = s1 + " " + j
        s1 += "\n"
        print(s1)
    print('Execution completed!')
