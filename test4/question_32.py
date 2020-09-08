data = [x for x in (x for x in 'canoesolutions.spayee.com' if x.isdigit()) if (x in ([x for x in range (20)]))]
print(data)
# since here x have not been converted to int, the condition in the if statement fails and therefore the list remains empty.
