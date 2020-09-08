x = ['ab','cd']
for i in x :
    i.upper()
    print(x)

#The function upper() does not modify a string in place but it
# returns a new string which here isn't being stored anywhwere.
#so we will get our original list as output