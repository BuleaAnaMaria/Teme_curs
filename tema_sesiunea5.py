
# 1 Scrieti un program care afiseaza daca valoarea unei variabile de tip int (de la tastatura) este para sau impara

# a=int(input('Introdu un numar\n>'))
# if(a%2==0):
#     print (f'{a} este numar par')
# else:
#     print(f'{a} nu este numar par')


# 2 Scrieti un program care afiseaza daca valoarea unei variabile de tip str ( care sa contina o singura litera, preluata de la tastatura ) este consoana sau vocala
# a=input('Introdu o litera\n>')
# if (a =='a') or (a =='e') or (a =='i') or (a =='o') or (a =='u')
#     print ('Ai introdus o vocala.')
# else:
#      print ('Ai introdus o consoana.')

# 3 Scrieti un program care preia de la tastatura:
# numele
# kg
# inaltimea
# varsta
# Acest program trebuie sa:
# afiseze un salut mentionand persoana
# sa calculeze BMI dupa formula bmi = kg/inaltime la patrat
# sa afiseze scorul BMI cu maxim 3 zecimale
# nume=input('Cum te numesti?\n>')
# kg=float(input('Ce greutate ai?\n>'))
# inaltime=float(input('Ce inaltime ai?\n>'))
# varsta=int(input('Ce varsta ai?\n>'))
# bmi=kg/inaltime**2
# print('Salut,%s! Scorul tau BMI este %.3f.'% (nume , bmi))


# 4 Scrieti un program care preia de la tastatura numele si varsta
# acest program trebuie sa raspunda cu un salut la adresa persoanei si
# sa mentioneze cati ani are pana ajunge la 100 de ani
# nume=input('Cum te numesti?\n>')
# varsta=int(input('Cati ani ai?\n>'))
# if varsta<100:
#     print('Salut %s, ai varsta de %d ani' %(nume, varsta))

# 5 Scrieti un program care preia urmatorul text:

# dupa ce s-a sfârşit nunta, feciorii s-au dus în treaba lor,iar nora rămase cu
# soacra.chiar în acea zi, cătră seară,baba începu să puie la cale viaţa nurori-sa.pentru babă,sita
# nouă nu mai avea loc în cuiu.„de  ce  mi-am  făcutcleşte? ca să nu mă ard“, zicea ea.apoi se suie iute
# în podşi coboară de acolo un ştiubeiu cu pene rămase tocmai dela răposata soacră-sa, nişte chite de cânepă
# şi vreo douădimerlii de păsat.

# Rezultatul final(o singura variabila) printat trebuie sa indeplineasca urmatoarele:
# Fiecare inceput de propozitie trebuie sa fie cu litera mare(propozitiile sunt delimitate de punct)
# Fiecare propozitie incepe de la o linie noua
# import string
# a='''dupa ce s-a sfârşit nunta, feciorii s-au dus în treaba lor,iar nora rămase cu soacra.chiar în acea zi, cătră seară,baba începu să puie la cale viaţa nurori-sa.pentru babă,sita nouă nu mai avea loc în cuiu.„de  ce  mi-am  făcutcleşte? ca să nu mă ard“, zicea ea.apoi se suie iute în podşi coboară de acolo un ştiubeiu cu pene rămase tocmai dela răposata soacră-sa, nişte chite de cânepăşi vreo douădimerlii de păsat.'''
# b=string.capwords(a,'.')
# b=b.replace('.','.\n')
# print(b)


# 6 Scrieti un program care primeste 2 numere diferite de la tastatura, face comparatia intre ele si
# anunta care este numarul mai mare si care este mai mic
# a = float(input('Scrie un numar:\n>'))
# b=float(input('Scrie un alt numar:\n>'))
# if (a==b):
#      print ('Numerele sunt egale.')
# else:
#     if (a<b):
#         print(f'{a} este mai mic decat {b}')
#     else:
#         print(f'{b} este mai mic decat {a}')


# 7 scrieti un program care primeste urmatoarele variabile
# a = '  sdYuri'
# a1 = '**#$)!Gagarin!23      '
# b = 'Alan!@Sheppard'
# c = 'JOSEPH_L_K'
# c1 = 'WALKER><>'
# d = 'D!@#avid'
# d1 = 'saint-jacques-----'
# Trebuie sa afisam numele fiecarui astronaut corect
# un nume este format din una sau mai multe variabile (ex: prenume a nume a1 )
# Fiecare numele trebuie sa inceapa cu Litera mare, si restul numelui cu litere mici.

# a = '  sdYuri'
# a1 = '**#$)!Gagarin!23      '
# b = 'Alan!@Sheppard'
# c = 'JOSEPH_L_K'
# c1 = 'WALKER><>'
# d = 'D!@#avid'
# d1 = 'saint-jacques-----'
# b1=a.split('d')
# a1_p=b1[1]
# c2=a1.split('!')
# a1_n=c2[1]
# print ('Numele si prenumele primului astronaut este:%s %s.' %(a1_n , a1_p))
# e=b.replace('!','')
# e=e.split('@')
# print('Numele si prenumele celui de-al doilea astronaut este: %s %s.'%(e[1] , e[0]))
# f=c.replace('_L_K','')
# f=f.lower()
# f=f.capitalize()
# g=c1.replace('><>','')
# g=g.lower()
# g=g.capitalize()
# print('Numele si prenumele celui de-al treilea astronaut este: %s %s.' %(g,f))
# h=d.replace('!@#','')
# d1=d1.rstrip('-')
# d1=d1.title()
# print('Numele si prenumele celui de-al patrulea astronaut este: %s %s.' %(d1,h))


# 8 Scrieti un program de tip casier
# casierul primeste de la tastatura un produs, cantitatea, pretul, si cati bani are clientul
# casierul trebuie sa afiseze informatiile relevante pentru client.
# produsul, cate cumpara, cat costa in total, si restul.
# produs=input('Ce vrei sa cumperi?\n>')
# cantitate=int(input('Cate bucati vrei sa cumperi?\n>'))
# pret=float(input('Cat costa produsul?\n>'))
# bani=float(input('Cati bani ai primit de la client?\n>'))
# total=cantitate*pret
# rest=bani-total
# if (rest<0):
#     print(f'Doriti sa cumparati {cantitate} bucati de {produs}. Totul costa {total} lei, insa am primit doar {bani} lei. Va rog sa imi dati diferenta')
# else:
#     print(f'Doriti sa cumparati {cantitate} bucati de {produs}. Totul costa {total} lei, iar eu trebuie sa va dau rest {rest} lei.')

# 9 Scrieti un program care cere un nume si varsta
# Cand ambele valori au fost introduse, verificam daca persoana are varsta corecta de a merge intr-o vacanta:
# 18-30 (peste 18 si sub 31)
# daca evaluarea este adevarata atunci le puteti ura bun venit in vacanta, daca nu, ii puteti refuza politicos
# nume=input('Cum va numiti?\n>')
# varsta=int(input('Ce varsta avet?\n>'))
# if varsta>18 and varsta<31:
#     print('Salut, %s! Bine ai venit in vacanta!' %nume)
# else:
#     print ('Imi pare rau, %s, insa nu ai varsta necesara pentru a putea veni in vacanta!'%nume)


# 10 Scrieti un program care cere 2 lucruri
# tipul programului ( lowercase sau uppercase )
# si un string
# in functie de tipul programului, returnati acel string inapoi in lowercase sau uppercase.
# s=input('Scrie un sir de caractere:\n>')
# a=input('Tipul programului:\n>')
# b=a.lower()
# if b=='lowercase':
#     print(s.lower())
# else:
#     print(s.upper())