try:
    inp = input()
    if not inp:
        raise ValueError("User hasn't provided any input")
except ValueError as e:
    print(e)
    try:
        f = open("formula.txt", "w")
    except:
        print('Failed to create the file.')
    else:
        print('File created but is empty.')
else:
    try:
        f = open("formula.txt", "w")
    except:
        print('Failed to create the file.')
    else:
        sentence = ""
        inplst = []
        i = 0
        while i < len(inp):
            c = inp[i]
            if c != '.' and c != '?' and c != '!':
                sentence = sentence + c
                i += 1
            else:
                sentence += c
                sentence += "\n"
                inplst.append(sentence)
                sentence = ""
                i += 2

        for i in inplst:
            f.write(i)
        f.close()
        print('File created and the data is written.')
finally:
    print('Execution Completed!')
