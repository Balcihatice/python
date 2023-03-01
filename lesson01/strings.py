name = 'Sedat'
surname = 'vedat'
age = 35

print('My name is ' + name +' '+ surname)

ad_soyad = 'My name is'
print(ad_soyad +' '+ name + ' ' + surname)

print(ad_soyad +' '+ name + ' ' + surname + ' and \n i am ' + str(age) + ' years old ')

greeting = ad_soyad +' '+ name + ' ' + surname + ' and \n i am ' + str(age) + ' years old'
print(greeting)
lenght = len(greeting)


print(greeting[1])
print(greeting[4])
print(len(greeting))
print(greeting[lenght-1])
print(greeting[-1])
print(greeting[3:7]) #2 den basla 5 e kadar yaz
print(greeting[3:]) #3ten basla sona kadar yaz
print(greeting[:16]) #en bastan baslar 16.karaktere kadar alir
print(greeting[2:40:2]) #2 den basla 40 a kadar git iki karakterden birini al