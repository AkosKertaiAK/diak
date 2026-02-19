class Diák:
    def __init__(self, nev, magassag):
        self.nev=nev
        self.magassag=magassag
        
    
#fájl feldolgozás

fajl=open("diak.txt", "r", encoding="utf-8")
#sorok feldolgozása
tartalom=fajl.read()
Ltartalom=tartalom.split("\n")

#üres lista a daraboláshoz
Ldiakok=[]

for sor in Ltartalom:
    Ldarabok=sor.split(";")
    nev=Ldarabok[0]
    magassag=int(Ldarabok[1])
    #példányosítás
    diak=Diák(nev, magassag)
    Ldiakok.append(diak)

#adatok kiíratása
for diak in Ldiakok:
    print(diak.nev)

#1. feladat tanulok szama:
print("Tanulók száma:", len(Ldiakok))

#2. legmagasabb(legmagasabb tanuló):
legmagasabb=Ldiakok[0]
for diak in Ldiakok:
    if diak.magassag>legmagasabb.magassag:
        legmagasabb=diak
print("Legmagasabb tanuló:", legmagasabb.nev, "magassága:", legmagasabb.magassag, "cm")

#3 Torna sorba rendezés
Lrendezve=sorted(Ldiakok, key=lambda m: m.magassag, reverse=True)
for diak in Lrendezve:
    print(diak.nev, diak.magassag)



