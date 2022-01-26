#SLicing in Python 

arr ="Apple Or Twaooo"
print(arr[4:])  # Get the characters from position 4 and all the way to the end:
print(arr[-1:]) # Get the position  


#Convert to upper case
a = "Hello, World!"
print(a.upper())


#Convert to lower case
a = "Hello, World!"
print(a.lower())


#to remove white spaces before and after a string
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))


#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

x = range(6)
for n in x:
  print(n)     
# 0 1 2 3 4 5

x = range(3,6)
for n in x:
  print(n)   
  
# 3 4 5  



txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 
  