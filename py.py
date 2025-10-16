# ============================================================
# 🐍 15 različnih nalog v Pythonu, ki uporabljajo zanke
# ============================================================

# 1. Izpis števil od 1 do 10 z for zanko
for i in range(1, 11):
    print(i)

# 2. Izpis samo sodih števil med 1 in 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3. Vsota števil od 1 do 100
vsota = 0
for i in range(1, 101):
    vsota += i
print("Vsota:", vsota)

# 4. Štetje črk v nizu z zanko
niz = "programiranje je kul"
stevec = 0
for znak in niz:
    if znak.isalpha():
        stevec += 1
print("Število črk:", stevec)

# 5. Obrni niz ročno z zanko
niz = "Python"
obrnjeno = ""
for znak in niz:
    obrnjeno = znak + obrnjeno
print("Obrnjeno:", obrnjeno)

# 6. Preveri, če je število praštevilo
stevilo = 29
je_prastevilo = True
for i in range(2, int(stevilo**0.5) + 1):
    if stevilo % i == 0:
        je_prastevilo = False
        break
print("Praštevilo?", je_prastevilo)

# 7. Fakulteta (n!) z for zanko
n = 5
fakulteta = 1
for i in range(1, n + 1):
    fakulteta *= i
print("Fakulteta:", fakulteta)

# 8. Iskanje največjega elementa v seznamu
stevila = [12, 3, 99, 45, 67, 1]
najvec = stevila[0]
for x in stevila:
    if x > najvec:
        najvec = x
print("Največje število:", najvec)

# 9. Odstranjevanje samoglasnikov iz niza
niz = "banane in jagode"
rezultat = ""
samoglasniki = "aeiou"
for znak in niz:
    if znak.lower() not in samoglasniki:
        rezultat += znak
print("Brez samoglasnikov:", rezultat)

# 10. Seštevanje vseh števil v seznamu z while zanko
stevila = [3, 5, 8, 2, 10]
i = 0
vsota = 0
while i < len(stevila):
    vsota += stevila[i]
    i += 1
print("Vsota:", vsota)

# 11. Iskanje števila v seznamu
stevila = [1, 4, 7, 9, 12, 15]
iskano = 9
najdeno = False
for x in stevila:
    if x == iskano:
        najdeno = True
        break
print("Najdeno?", najdeno)

# 12. FizzBuzz (klasika)
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 13. Preverjanje palindroma (niz, ki je isti naprej in nazaj)
niz = "anna"
je_palindrom = True
for i in range(len(niz) // 2):
    if niz[i] != niz[-(i + 1)]:
        je_palindrom = False
        break
print("Palindrom?", je_palindrom)

# 14. Ustvari novo listo z kvadrati števil
stevila = [1, 2, 3, 4, 5]
kvadrati = []
for x in stevila:
    kvadrati.append(x**2)
print("Kvadrati:", kvadrati)

# 15. Seštej samo pozitivna števila v seznamu
stevila = [-5, 3, -1, 7, 0, 9]
vsota = 0
for x in stevila:
    if x > 0:
        vsota += x
print("Vsota pozitivnih:", vsota)

print("\n=== 1. zip() — paralelna iteracija ===")
imena = ["Ana", "Bine", "Cene", "Dora"]
ocene = [5, 3, 4, 5]

# zip() združi elemente dveh seznamov
for ime, ocena in zip(imena, ocene):
    print(f"{ime} je dobil oceno {ocena}")


print("\n=== 2. enumerate() — indeksiranje ===")
mesta = ["Ljubljana", "Maribor", "Celje", "Kranj"]

# enumerate() vrne indeks in vrednost
for i, mesto in enumerate(mesta):
    print(f"{i}: {mesto}")


print("\n=== 3. for + else — če ne najde elementa ===")
stevila = [2, 4, 6, 8, 10]
iskano = 7

for s in stevila:
    if s == iskano:
        print(f"Najdeno: {s}")
        break
else:
    print(f"Število {iskano} ni v seznamu")


print("\n=== 4. any() in all() — preverjanje pogojev ===")
stevila = [2, 4, 6, 8]
print("Ali je vsaj eno število > 7:", any(x > 7 for x in stevila))
print("Ali so vsa soda:", all(x % 2 == 0 for x in stevila))


print("\n=== 5. map() in filter() — transformacija in filtriranje ===")
stevila = [1, 2, 3, 4, 5, 6]
kvadrati = list(map(lambda x: x**2, stevila))       # kvadriranje vseh
soda = list(filter(lambda x: x % 2 == 0, kvadrati)) # obdrži samo soda
print("Kvadrati:", kvadrati)
print("Soda števila:", soda)


print("\n=== 6. sorted() in reversed() — sortiranje in obrat ===")
stevila = [5, 1, 7, 3, 2]
print("Naraščajoče:", sorted(stevila))
print("Padajoče:", sorted(stevila, reverse=True))
print("Obratni vrstni red elementov:")
for s in reversed(stevila):
    print(s)


print("\n=== 7. Gnezdene zanke — matrika ===")
matrika = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Zunanji loop za vrstice, notranji za elemente
for vrstica in matrika:
    for e in vrstica:
        print(e, end=" ")
    print()


print("\n=== 8. try-except — napake pri pretvorbi ===")
podatki = ["10", "20", "abc", "30"]
for vrednost in podatki:
    try:
        stevilo = int(vrednost)
        print(f"{vrednost} + 1 = {stevilo + 1}")
    except ValueError:
        print(f"Napaka: '{vrednost}' ni številka")


print("\n=== 9. Kombinacija več stvari (enumerate + sorted + try) ===")
vhod = ["5", "napaka", "10", "1", "abc", "3"]
stevila = []
for v in vhod:
    try:
        stevila.append(int(v))
    except:
        continue
for i, x in enumerate(sorted(stevila)):
    print(f"{i}: {x}")


print("\n=== 10. while + break + continue ===")
x = 0
vsota = 0
while x <= 20:
    x += 1
    if x % 2 != 0:
        continue  # preskoči liha števila
    if x == 18:
        break     # prekini pri 18
    vsota += x
print("Vsota sodih števil do 18:", vsota)