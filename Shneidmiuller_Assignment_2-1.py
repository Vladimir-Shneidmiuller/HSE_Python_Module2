variable = str(input())
print ("Word =", variable)

if len(variable) % 2 == 0:
    index1 = len(variable)//2-1 
    index2 = index1 + 1
    for i in index1, index2:
        print(variable[i], end="")
else:
    index1 = len(variable)//2
    print(variable[index1], end="")
