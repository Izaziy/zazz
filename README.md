# zazz
1. for zanka z več spremenljivkami

for ni omejen samo na eno spremenljivko — lahko iteriraš čez več vrednosti hkrati, če so podatki v obliki parov ali tuple-ov.

To je uporabno pri seznamih parov, slovarjih, matrikah …

pari = [(1, 2), (3, 4), (5, 6)]
for x, y in pari:
    print(x + y)


👉 3 7 11
✅ Uporabno pri: obdelavi podatkov v parih, tabelah, koordinatah, 2D strukturah.

2. while zanka z varnostnim pogojem (guard condition)

Pri while zankah je pomembno, da vedno obstaja izhodni pogoj, drugače se ustvari neskončna zanka.

Lahko uporabiš notranji break kot dodatno varovalo.

x = 0
while True:  # neskončna zanka
    if x >= 10:  # varovalni pogoj
        break
    print(x)
    x += 1


👉 Izpiše 0 do 9.
✅ Uporabno za: igre, menije, simulacije, kjer moraš kontrolirati izhod.

3. range() z negativnim korakom

range() ne gre vedno samo naprej — lahko šteješ tudi nazaj.

for i in range(10, 0, -2):
    print(i)


👉 10 8 6 4 2
✅ Uporabno za: odštevanje, reverzne zanke, premikanje “nazaj”.

4. enumerate() za indeksiranje brez range(len(...))

Pogosta napaka začetnikov je, da delajo:

for i in range(len(seznam)):
    print(i, seznam[i])


Bolj elegantno in zmogljivo je:

for i, vrednost in enumerate(seznam):
    print(i, vrednost)


✅ To je bolj berljivo in manj “buggy”.

5. Gnezdene zanke (nested loops)

Ko imaš dve strukturi podatkov (npr. seznam v seznamu), lahko uporabiš zanko znotraj zanke.

Pomembno je razumeti, kako deluje iteracija po nivojih.

tabela = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for vrstica in tabela:
    for element in vrstica:
        print(element, end=" ")


👉 1 2 3 4 5 6 7 8 9
✅ Uporabno za: delo z 2D podatki, matrikami, tabelami, mapami.

6. zip() za paralelno iteracijo

zip() omogoča, da hkrati iteriraš čez več seznamov.

imena = ["Ana", "Bine", "Cene"]
ocene = [5, 4, 3]

for ime, ocena in zip(imena, ocene):
    print(ime, ocena)


👉

Ana 5  
Bine 4  
Cene 3


✅ Uporabno za: kombiniranje podatkov, branje paralelnih seznamov.

7. break in continue z gnezdenimi pogoji

Pri zahtevnejših pogojih lahko uporabiš break in continue selektivno, znotraj notranjih zank.

for x in range(5):
    for y in range(5):
        if x == y:
            continue  # preskoči če sta enaka
        if x + y > 6:
            break     # ustavi notranjo zanko
        print(x, y)


✅ To omogoča fino kontrolo toka znotraj kompleksnih struktur.

8. else na zanki 😎

Da, for in while imata lahko else.

else blok se izvede samo, če zanka ni bila prekinjena z break.

for i in range(5):
    if i == 10:
        break
else:
    print("Zanka je zaključena brez break")


👉 Izpiše se, ker break ni bil nikoli uporabljen.
✅ Uporabno pri: iskanju elementa, preverjanju pogojev po zaključeni zanki.

9. any() in all() – logika brez ročnih zank

Namesto da sam preverjaš vsak element v zanki, lahko uporabiš logične funkcije:

stevila = [2, 4, 6]
print(all(x % 2 == 0 for x in stevila))  # True
print(any(x > 5 for x in stevila))       # True


✅ Zelo uporabno pri preverjanju pogojev za celoten seznam.

10. List comprehension

“Krajši” način pisanja zank — hitrejši in elegantnejši.

stevila = [x**2 for x in range(10) if x % 2 == 0]
print(stevila)


👉 [0, 4, 16, 36, 64]
✅ Uporabno za: generiranje seznamov, filtriranje podatkov, matematiko.

11. map() in filter()

Namesto zank lahko uporabiš funkcije za funkcionalno obdelavo podatkov.

a = [1, 2, 3, 4]
b = list(map(lambda x: x * 2, a))
c = list(filter(lambda x: x % 2 == 0, b))

print(b)  # [2, 4, 6, 8]
print(c)  # [2, 4, 6, 8]


✅ Uporabno pri transformaciji in filtriranju podatkov brez klasične zanke.

12. reversed() in sorted()

Zanke lahko iterirajo tudi po urejenih ali obrnjenih podatkih, brez spreminjanja originalnega seznama.

a = [3, 1, 4, 2]
for x in sorted(a):
    print(x)  # 1 2 3 4

for x in reversed(a):
    print(x)  # 2 4 1 3


✅ Uporabno za: sortiranje, pregled podatkov v drugem vrstnem redu.

13. dict iteracija (ključi, vrednosti, pari)

Pri slovarjih imaš več načinov iteracije:

podatki = {"ime": "Ana", "starost": 17, "ocena": 5}

for k in podatki:
    print(k, podatki[k])            # čez ključe

for v in podatki.values():
    print(v)                        # čez vrednosti

for k, v in podatki.items():
    print(k, v)                     # čez pare


✅ Uporabno za: delo z mapami, podatkovnimi strukturami, JSON-i.

14. try + zanke (varno izvajanje)

Če v zanki delaš z nepredvidljivimi podatki, lahko uporabiš error handling, da ne sesuješ programa.

stevila = ["10", "20", "abc", "30"]
for s in stevila:
    try:
        print(int(s) + 1)
    except ValueError:
        print("Napaka pri:", s)


✅ Uporabno za: obdelavo podatkov, ki niso vedno pravilni.

15. Kombinacija več konceptov 💪

V realnih programih boš skoraj vedno kombiniral več stvari:

podatki = ["3", "4", "napaka", "6", "8"]

veljavna = []
for s in podatki:
    try:
        x = int(s)
        if x % 2 == 0:
            veljavna.append(x)
    except:
        continue

for i, v in enumerate(sorted(veljavna)):
    print(f"{i}: {v}")


👉 Filtrira samo veljavne, jih pretvori, sortira in izpiše z indeksom.

✅ To je primer realne uporabe try, for, if, sorted(), enumerate() skupaj.

📌 Povzetek naprednih orodij:
Funkcija / ukaz	Namen	Uporaba
zip()	paralelna iteracija	delo z več seznami hkrati
enumerate()	indeksiranje	bolj elegantno kot range(len(...))
else na zanki	dodatna logika po zanki	iskanje elementa, “ni najdeno” scenariji
any(), all()	preverjanje pogojev za vse elemente	hitra logika brez ročnih zank
map(), filter()	funkcionalna obdelava	transformacija podatkov
sorted(), reversed()	sortiranje in obratni vrstni red	kontrola vrstnega reda pri iteraciji
try v zanki	varno izvajanje	program se ne sesuje pri napakah
Gnezdene zanke	delo z več nivoji struktur	matrike, kompleksni podatki