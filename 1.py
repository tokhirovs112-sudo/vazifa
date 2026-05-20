def eng_kop_3_soz(matn):
    soz = ""
    sozlar = []

    # matnni qo‘lda ajratish (split ishlatmasdan)
    for belgi in matn:
        if belgi != " ":
            soz += belgi
        else:
            if soz != "":
                sozlar.append(soz)
                soz = ""

    
    if soz != "":
        sozlar.append(soz)

    
    hisob = {}

    for s in sozlar:
        if s in hisob:
            hisob[s] += 1
        else:
            hisob[s] = 1

    tartib = sorted(hisob.items(), key=lambda x: x[1], reverse=True)

    natija = []
    for i in range(min(3, len(tartib))):
        natija.append(tartib[i][0])

    return natija


matn = "olma nok olma gilos olma nok shaftoli"
print(eng_kop_3_soz(matn))