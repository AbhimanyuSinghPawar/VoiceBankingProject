#list of having only integers
a= [1,2,3,4,5,6]
#print(a)

#list of having only strings
b=["hello","john","reese"]
#print(b)

#list of having both integers and strings
c= ["hey","you",1,2,3,"go"]
#print(c)

print(c[1])
print(c[-1])
print(c[1: 3])  # include the element at index 1 but exclude the element at index 3
print(c[1:-1])
print(c[-1:2])
print(c[-1:-1])
print(c[-2:-1])

# insert value in the middle
c.insert(3,'value inserted')
print(c)
#insert value at the end of the list
c.append(4)
c.append("abc")
c.append('abhimanyu')
print(c)