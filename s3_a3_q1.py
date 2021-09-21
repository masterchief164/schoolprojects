inp = input("Enter the string: ")

freq = {}
for i in inp:
    if i not in freq.keys():
        freq[i] = 1
    else:
        freq[i] += 1
ke = freq.keys()
for i in ke:
    print("Frequency of " + i + " is " + str(freq[i]))
