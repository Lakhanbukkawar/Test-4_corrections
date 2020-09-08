x = ['ab','cd']
for i in x:
    x.append(i.upper())
    print(x)

# the loop does not terminate as new elements are being added to the list in each iteration.So our program will stuck in infinite loop