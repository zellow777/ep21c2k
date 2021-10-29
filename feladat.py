# 1. Olvassa be és tárolja el a valaszok.txt szöveges állomány adatait!
input
f = open ("valaszok.txt", "r")
valaszok = []
for line in f:
    valaszok.append(line)
f.close()

megoldas = valaszok[0]
valaszok = valaszok[1:]

# 2. Jelenítse meg a képernyőn a mintának megfelelően, hány versenyző vett részt a tesztersenyen!

print(f"2.feladat: A versenyen {len(valaszok)} versenyző indult")

# 3. Kérje be egy versenyző azonosítóját és jelenítse meg a mintának megfelelően a hozzá eltárolt válaszokat! Ha nincs
#ilyen kód, akkor jelenítse meg: Ilyen kóddal nem indult versenyző.

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

# 4. Írassa ki a képernyőre a helyes megoldást! A helyes megoldás alatti sorba tegyen "+" jelet, ha az adott feladatot az
#előző feladatban kiválasztott versenyző eltalálta, egyébként egy szóközt. A kiíratást a mintának megfelelő módon
#alakítsa ki! Ha olyan kód volt megadva, ami nem szerepel a listában, úgy az 1. versenyző megoldását vizsgálja!

helyes = ""
x = 0
while x < len(megoldas)-1:
    if megoldas[x] == jatekosMegoldasa[x]:
        helyes += "+"
    else:
        helyes += " "
    x += 1
print(f"4.feladat: A helyes megoldás:\n{megoldas}{helyes}")

# 5. Kérje be egy feladat sorszámát, majd határozza meg, hány versenyző adott a feladatra helyes megoldást, és ez a
#versenyzők hány százaléka! A százalékos eredményt a mintának megfelelően, 2 tizedesjegy pontossággal írassa ki.

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


# 6. A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10. feladat 4 pontot, a 11-13. feladat
#5 pontot, a 14. feladat 6 pontot ér. Határozza meg az egyes versenyzők pontszámát, és a listát írassa ki a pontok.txt
#nevű állományba! Az állomány minden sora egy versenyző kódját, majd szóközzzel elválasztva az általa elért pontszámot
#tartalmazza!

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
            if x <= 5:
                pont += 3
            elif x >= 6 and x <= 10:
                pont += 4
            elif x >= 11 and x <= 13:
                pont += 5
            elif x == 14:
                pont += 6
        x += 1
    pontok.append(pont)

x = 0
while x < len(azonositok)-1:
    g.write(f"{azonositok[x]} {pontok[x]}\n")
    x += 1
g.close()

# 7. A versenyen a 3 legmagasabb pontszámot elérő összes versenyzőt díjazzák. Például 5 indulónál előfordulhat, hogy 3 db.
#első és 2 db. második díjat adnak ki. Így megtörténhet az is, hogy nem kerül sor mindegyik díj kiadására. Írassa ki
#a mintának megfelelően a képernyőre a díjazottak kódját és pontszámát, pontszám szerint csökkenő sorrendben!

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

