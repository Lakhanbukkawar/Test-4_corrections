dictionary = {}
dictionary[1] = 1
dictionary['1'] = 2
dictionary[1] += 1
sum = 0
for k in dictionary:
    sum += dictionary[k]
    print(sum)

# in the above dictionary the key 1 enclosed between single quotes and only 1 represents two different
# keys as one of them is integer and other is string.so the output of the program is 4