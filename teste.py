lista = ('10 14 13').split()
total= 0

total=0
for i in lista:
    for j in i:
        total += int(j)

print(total)
