#1
a = 'JhonDipPeta'
print ('"',a[4:7],'"')

# 2
a = 'JaSonAy'
print ('"',a[-5:-2],'"')

#3
a= 'Pythonrulez'
print('"',a[::-1],'"')

#4
a = 'AaBbCcDdEe'
print('"',a[0::2],'"')

#5
a = 'something'
print(a[0:4])

#6
a="Maria\'s teacher speaks 3 different languages:\n\t1.English\n\t2.Spanish\\French(I don\'t remember exactly)\n\t3.German"
print(a)

#7
a=5
b=10
tmpa=5
tmpb=10
a=tmpb
b=tmpa
print("a=",a,"\nb=",b)

#8
a='ABCDEF'
print(a[-6::2])

#9
print(7*7)

#10
print(7**5)

#11

print("Number 1    Lewis Hamilton\nNumber 2    Valtteri Bottas")
print("Number 1\tLewis Hamilton\nNumber 2\tValtteri Bottas")
print("""Number 1\tLewis Hamilton
Number 2\tValtteri Bottas""")

#12
print ("A cumparat",15//2.4,"chifle.")
print ("Trebuie sa primeasca",15%2.4,"lei inapoi.")

print(13)
a='abcdefghijklmnopqrstuvwxyz'
# "qpo" - 1
b=a[-12:-9:-1]
print(b[::-1])
# "qpo" - 2
b=(a[::-1])
print (b[9:12])

# "edcba" - 1
b=a[0:5]
print(b[::-1])

# "edcba" - 2
b=(a[::-1])
print(b[-5::])

# ultimele 8 caractere, in ordine inversa
print(len(a))
b=a[(len(a)-8)::]
print(b[::-1])

#14
kg=56
m=1.66
bmi=kg/m**2
print(bmi)

#15
print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are")

#16
print(122%55)
print(55%122)

#17
a = 'ASDNt98vncnkjx-089253x.a,se'
b=('5' in a)
print(b)

#18
a= 'mmmclki,31nb3rbczxc'
b=(',' not in a)
print(b)

#19 ?
num3=10
num3=30

#20
num4 = 55
num5 = '55'
a=num4 is num5
print(a)

#21
num6 = 12
num7 = 3
num8 = 4
num9 = 10

a=num6+num7//num8**num9
print(a)
