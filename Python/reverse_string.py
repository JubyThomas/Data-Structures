str="helloooo this is juby;"

#method 1  -Extended Slicing
print(str[-1::-1])

#Method 2 
result=""
for i in range(len(str)-1,0 ,-1):  #or for i in range(len(str)-1,-1,-1)
    result+=str[i]
print(result)


print(''.join(reversed(str)))


