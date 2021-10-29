# 1.
f = open("valaszok.txt", "r")
valaszok = []
for line in f:
    valaszok.append(line)
f.close()

megoldas = valaszok[0]
valaszok = valaszok[1:]

# 2.

print(f"2.feladat: A versenyen {len(valaszok)} versenyző indult")

# 3.

jatekosMegoldasa = ""
azonosito = input("3.feladat: Kérem adja meg egy versenyző azonosítóját: ")
for valasz in valaszok:
    if valasz[:5] == azonosito:
        print(valasz[6:])
        jatekosMegoldasa = valasz[6:]
if jatekosMegoldasa == "":
    print("Ilyen kóddal nem indult versenyző!")
    valasz = valaszok[0]
    jatekosMegoldasa = valasz[6:]

# 4.

helyes = ""
x = 0
while x < len(megoldas)-1:
    if megoldas[x] == jatekosMegoldasa[x]:
        helyes += "+"
    else:
        helyes += " "
    x += 1
print(f"4.feladat: A helyes megoldás:\n{megoldas}{helyes}")

# 5.

feladatszama = 0
while feladatszama == 0:
    try:
        feladatszama = int(input("5.feladat: Kérem adja meg egy feladat sorszámát: "))
        if feladatszama < 1 or feladatszama > 14:
            print("Nincs ilyen feladatszám!")
            feladatszama = 0
    except ValueError:
        print("Hibás adatbevitel!")

feladatszamaMegoldas = megoldas[feladatszama-1]
megoldasJatekosok = []
jomegoldasok = 0

for valasz in valaszok:
    if valasz[5+feladatszama] == feladatszamaMegoldas:
        jomegoldasok += 1

print(f"5.feladat: A feladatra {jomegoldasok}fő, a versenyzők {jomegoldasok/len(valaszok):.2%}-a adott helyes választ.")

# 6.

g = open("pontok.txt", "w")
megoldasok = []
azonositok = []
pontok = []

for valasz in valaszok:
    azonositok.append(valasz[:5])

for valasz in valaszok:
    megoldasok.append(valasz[6:-1])

for valasz in megoldasok:
    x = 0
    pont = 0
    while x < len(valasz):
        if valasz[x] == megoldas[x]:
            if x <= 4:
                pont += 3
            elif x >= 5 and x <= 9:
                pont += 4
            elif x >= 10 and x <= 12:
                pont += 5
            elif x == 13:
                pont += 6
        x += 1
    pontok.append(pont)

x = 0
while x < len(azonositok)-1:
    g.write(f"{azonositok[x]} {pontok[x]}\n")
    x += 1
g.close()

# 7.

print("7.feladat: A verseny legjobbjai:")
elso = max(pontok)
while elso in pontok:
    pontok.remove(elso)

masodik = max(pontok)
while masodik in pontok:
    pontok.remove(masodik)

harmadik = max(pontok)

g = open("pontok.txt", "r")
for data in g:
    if int(data[6:]) == int(elso):
        print(f"1. díj ({elso}): {data[:5]}")

g = open("pontok.txt", "r")
for data in g:
    if int(data[6:]) == int(masodik):
        print(f"2. díj ({masodik}): {data[:5]}")

g = open("pontok.txt", "r")
for data in g:
    if int(data[6:]) == int(harmadik):
        print(f"3. díj ({harmadik}): {data[:5]}")
g.close()
