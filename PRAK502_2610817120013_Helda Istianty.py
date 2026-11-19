def hitung(nilai1, nilai2):
    selisih = nilai1 - nilai2
    if selisih < 0:
        selisih = -selisih
    return selisih

def mutlak(angka):
    if angka < 0:
        return -angka
    return angka

x1, y1, x2, y2 = map(int, input().split())
hasil = hitung(x1, x2) + hitung(y1, y2)
print(mutlak(hasil))