#Sa scriem un program care afiseaza numarul de vocale si consoane dintr-un string primit de la tastatura

a=input('Scrie un string care sa contina doar litere:\n>')
a=a.lower()
v=0
c=0
for i in a:
    if i in 'aeiou':
        v=v+1
    else:
        c=c+1
print(f' String-ul "{a}" contine {v} vocale si {c} consoane.')