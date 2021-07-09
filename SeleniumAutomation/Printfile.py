print('Abhimanyu singh')

print('Abhimanyu''Singh''Pawar')

print('Abhimanyu'+'Singh')

str = 'Abhay'

print(str)

str1 = str + 'Raj'

print(str)
print(str1)
print(str1 +'Singh')

dd, mm, yyyy = '11', '05', '1993'

# we can only concatinate Str into str
print('DOB of Abhimanyu Singh is:  '+dd+'/'+mm+'/'+yyyy)

#find the type of dd
print(type(dd))

#concatinate a str into int
dd, mm, yyyy = 11, 5, 1993

print("{}{}{}{}{}{}".format('DOB of Abhimanyu Singh is:  ',dd,'/',mm,'/',yyyy))

#Find the type of data
print(type(str))
print(type(dd))