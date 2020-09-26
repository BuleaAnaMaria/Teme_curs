# Sa scriem o functie:
# Functia poate primi doua argumente:
# - primul este un string in care vom cauta
# - al2lea este un string care il vom cauta in primul string
# Daca s-a gasit string in string, returnam True si printam 'S-a gasit {stringul_cautat}'.
# In caz contrar returnam False si printam 'Nu s-a gasit'.
#
# Sa se apeleze functia de cateva ori cu stringuri diferite, sa putem observa ca functioneaza
# corect in ambele cazuri ( ca s-a gasit, sau ca nu s-a gasit)
#
# def search_string(a,b):
#     c=a.find(b)
#     if c!=-1:
#         print(f'S-a gasit {b}')
#         return True
#     else:
#         print(f'Nu s-a gasit {b}')
#         return False
#
# print(search_string('abc','b'))
# print(search_string('ABC','y'))

def search_string(a,b):
    for i in a:
        if i == b:
            print('s-a gasit string-ul')
            return True
            break
        else:
            continue
    print('nu s-a gasit string-ul')
    return False

print(search_string('abc','b'))
#print(search_string('ABC','b'))