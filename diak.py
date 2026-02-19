fajl=open ("diak.txt","r",encoding="utf-8")
tartalom = fajl.read()
fajl.close()

print(str(tartalom))


sorok = tartalom.split("\n")
print(len(sorok))


max_nev = ""
max_magassag = 0

for sor in tartalom.split("\n"):
    nev, magassag = sor.strip().split(";")
    magassag = int(magassag)

    if magassag > max_magassag:
        max_magassag = magassag
        max_nev = nev


print("A legmagasabb tanuló:", max_nev)
print("Magassága:", max_magassag, "cm")