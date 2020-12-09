
"""
# 1. ukol (funkcni)

Puvodni funkcni fce pro nalezeni 2 cisel


def dve_cisla(soucet):

    with open("input.txt", "r") as myfile:
        mylist = [line[:-1] for line in myfile.readlines()]

    for a in mylist:
        b = soucet-int(a)
        if str(b) in mylist:
            c = int(a)*int(b)
            return(f'Hledana dvojice je {a} a {b}. A*B= {c}')
        else:
            pass
"""

# 2. ukol (funkcni)

def dve_cisla(soucet):

    with open("input.txt", "r") as myfile:
        mylist = [line[:-1] for line in myfile.readlines()]

    for a in mylist:
        b = soucet-int(a)
        if str(b) in mylist:
            return(int(a),b)
        else:
            pass

def tri_cisla(cilovy_soucet):
    with open("input.txt", "r") as myfile:
        mylist = [line[:-1] for line in myfile.readlines()]

    for a in mylist:
        mezicislo = cilovy_soucet - int(a)
        dvojice = dve_cisla(mezicislo)
        if dvojice != None:
            print(f'Nasobek je ', (int(a)*dvojice[0]*dvojice[1]), ' a cisla jsou: ')
            return(a,dvojice[0],dvojice[1])
        else:
            pass

print(tri_cisla(2020))
#print(dve_cisla(2019))