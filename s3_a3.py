from tabulate import tabulate  # use pip install tabulate to install dependencies


# first question
def fac(n):  # function to calculate the factorial
    if n == 0:  # Base Case
        return 1  # if number turns 0 then multiply 1
    return fac(n - 1) * n  # recursively call the function with decrementation of 1 until the base case
    # is reached and keep the product in the stack


def nCr(n, r): # calculating the nCr and printing it upto Start + 1
    return (fac(n)) // (fac(r) * fac(n - r))


def QuestionOne(finish, start=0):  # function with start and finish parameters with start  having a default
    # value of 0
    if start == finish:  # base case until start reaches finish
        return
    for i in range(finish - start):  # printing spaces until the required position of printing is reached
        print("", end=" ")
    for i in range(start + 1):
        # providing spaces after each element
        print(nCr(start, i), end=" ")
    print()
    QuestionOne(finish, start + 1)


# second Question

def QuestionTwo(matrix):
    data = []  # defining the data list which will have the final data to be printed
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):  # traversing through the matrix
            row = []  # data of each element
            if matrix[i][j] != 0:  # entering the data of the non zero elements
                row.append(i)
                row.append(j)
                row.append(matrix[i][j])
                data.append(row)
    print(tabulate(data, headers=["Row", "Column", "Value"]))  # Printing the data using the tabulate
    # library to beautify the table string formatting could also be used


# third Question

def QuestionThree(array):
    leng = len(array)
    for i in range(leng):  # traversing through the list
        for j in range(0, leng - 1 - i):  # traversing through the list upto i+1 th last term
            if array[j] > array[j + 1]:  # comparing adjacent elements
                tmp = array[j]  # swapping the elements using a third variable
                array[j] = array[j + 1]
                array[j + 1] = tmp
                # array[j], array[j + 1] = array[j + 1], array[j] swapping the elements
                # without third element (python Specials)
    return array


# fourth Question

def QuestionFour(inp):
    ans = 0  # final decimal value
    tmp = 0  # temporary variable to store the last element's value
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  # roman to hindu arabic dictionary
    leng = len(inp)
    for i in reversed(range(leng)):  # loop in reverse to go through the roman number from right to left
        if table[inp[i]] < tmp:  # if last element was less than current element the current will be subtracted
            ans -= table[inp[i]]
        else:  # otherwise added
            ans += table[inp[i]]
        tmp = table[inp[i]]
    return ans


print("Question One")
QuestionOne(5)
QuestionOne(int(input("Enter the limit ")))

print('\n \n \n \n')
print("Question Two")
mat = [[0, 0, 0, 0, 9, 0],
       [0, 8, 0, 0, 0, 0],
       [4, 0, 2, 0, 0, 0],
       [0, 0, 0, 0, 0, 5],
       [0, 0, 0, 0, 0, 5],
       [0, 0, 2, 0, 0, 0]]
QuestionTwo(mat)

print('\n \n \n \n')
print("Question Three")

arr = [8, 5, 7, 3, 1]
print("Unsorted Array", arr)

print("Sorted Array", QuestionThree(arr))
print('\n \n \n \n')
print("Question Four")

print(QuestionFour("III"))
print(QuestionFour("IV"))
print(QuestionFour("IX"))
print(QuestionFour("LVIII"))
print(QuestionFour("MCMXCIV"))
