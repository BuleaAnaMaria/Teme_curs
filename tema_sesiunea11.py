meniu = ['1. Comenzi', '2. Persoane', '3. Produse', '4. Preturi', '5. Exit']
persoane = ['Bogdan', 'Andreea', 'Catalin']
produse = ['Lapte', 'Paine', 'Laptop']
pret = ['Lapte - 5', 'Paine - 3', 'Laptop - 2500']
comenzi = ['Lapte 2 Bogdan', 'Paine 5 Andreea', 'Laptop 1 Catalin']
while True:
    print('Meniu principal:')
    for i in meniu:
        print(i)
    optiune=int(input('Selecteaza o optiune:\n>'))
    if optiune==5:
            print('Ai ales sa iesi din program.')
            break
    if optiune == 1:
        for i in comenzi:
            print(i)
        print ('Optiuni: \n 1. Adauga o comanda \n 2. Meniu principal\n>')
        a=int(input('Selecteaza o optiune\n>'))
        if a == 1:
            comanda = input('Comanda pe care vrei sa o adaugi este:\n>')
            comenzi.append(comanda)
            print('Ai adaugat o comanda.')
        if a == 2:
            continue
    if optiune == 2:
        for i in persoane:
            print(i)
        print('Optiuni: \n 1. Adauga o persoana \n 2. Meniu principal\n>')
        b = int(input('Selecteaza o optiune\n>'))
        if b == 1:
            nume = input('Numele pe care vrei sa il adaugi este:\n>')
            persoane.append(nume)
            print('Ai adaugat un nume.')
        if b == 2:
            continue
    if optiune == 3:
        for i in produse:
            print (i)
        print('Optiuni: \n 1. Adauga un produs \n 2. Meniu principal\n>')
        c = int(input('Selecteaza o optiune\n>'))
        if c == 1:
            produs = input('Produsul pe care vrei sa il adaugi este:\n>')
            produse.append(produs)
            print ('Ai adaugat un produs.')
        if c == 2:
            continue
    if optiune==4:
        for i in pret:
            print (i)
        print('Optiuni: \n 1. Adauga un produs - pret \n 2. Meniu principal\n>')
        d = int(input('Selecteaza o optiune\n>'))
        if d == 1:
            pretul = input('Pretul pe care vrei sa il adaugi este:\n>')
            pret.append(pretul)
            print('Ai adaugat un pret.')
        if d == 2:
            continue