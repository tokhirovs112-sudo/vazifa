ombor = [
    {"mahsulot": "olma", "miqdor": 5},
    {"mahsulot": "nok", "miqdor": 9},
    {"mahsulot": "shaftoli", "miqdor": 7},
    {"mahsulot": "anor", "miqdor": 4},
    {"mahsulot": "banan", "miqdor": 6},
    {"mahsulot": "uzum", "miqdor": 8},
    {"mahsulot": "gilos", "miqdor": 2},
    {"mahsulot": "tarvuz", "miqdor": 1},
    {"mahsulot": "qovun", "miqdor": 3},
    {"mahsulot": "limon", "miqdor": 5}
]

umumiy = 0
for i in ombor:
    umumiy += i["miqdor"]

print("Umumiy mahsulotlar miqdori:", umumiy)
eng_kam_3 = sorted(ombor, key=lambda x: x["miqdor"])[:3]

print("Eng kam qolgan 3 ta mahsulot:", end=" ")
for h in eng_kam_3:
    print(h["mahsulot"], end=" ")