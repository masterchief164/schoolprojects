inp1 = input("Enter the coefficients of the first expression ") # x0 x1 x2
inp2 = input("Enter the coefficients of the second expression ")# x0
inp1 = list(map(int, inp1.strip().split()))
inp2 = list(map(int, inp2.strip().split()))
length = len(inp1) < len(inp2) and len(inp1) or len(inp2)
ans = []
for i in range(length):
    ans.append(inp1[i] + inp2[i])
if len(inp2) > len(inp1):
    for i in range(len(inp1), len(inp2)):
        ans.append(inp2[i])
else:
    for i in range(len(inp2), len(inp1)):
        ans.append(inp1[i])
for i in ans:
    print(i, end=" ")
