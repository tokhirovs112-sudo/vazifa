def tozalash(royxat):
    natija = []

    for soz in royxat:
        if soz != "" and soz not in natija:
            natija.append(soz)

    return natija


mylist = ["olma", "", "olma", "gilos", ""]

print(tozalash(mylist))