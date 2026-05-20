def ortacha(oquvchilar):
    natija = {}

    for ism, fanlar in oquvchilar.items():
        avg = sum(fanlar.values()) / 2
        natija[ism] = avg

    return natija


oquvchilar = {
  "Ali": {"math": 90, "en": 80},
  "Vali": {"math": 70, "en": 85}
}

print(ortacha(oquvchilar))