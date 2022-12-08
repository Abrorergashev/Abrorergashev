mahsulotlar = ['un', "yog'", "sovun", "tuxum", "piyoz", "kartoshkd", "olma", "banan", "uzum", "qovun",]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qoshing:"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"do'konimizda {mahsulot} bor")
    else:
        print(f"do'konimizda {mahsulot} yo'q")
        

    