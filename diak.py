fajl=open ("diak.txt","r",encoding="utf-8")
tartalom = fajl.read()
fajl.close()

print(str(tartalom))


sorok = tartalom.split("\n")
print(len(sorok))