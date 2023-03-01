x = input('1 sayi:')
y = input('2.sayi:')

print(type(x))
print(type(y))

toplam = int(x) + int(y)
print(toplam)

x= 5   #int
y = 4.5  #float
name = 'Veli'  #string
isOnline = True  #boolean
print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

#Type Conversion
#int to float
x = float(x)
print(x)
print(type(x))

#float to int
y = int(y)
print(y)
print(type(y))

result = x + y
print(result)

result = str(x) + str(y)
print(result)
print(type(result))

#bool to string
isOnline =str(isOnline)
print(isOnline)
print(type(isOnline))

#bool to int
isOnline = bool(isOnline)
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))
