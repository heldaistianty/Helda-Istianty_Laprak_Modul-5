def maksimal(a, b):
    if a > b:
        return a
    return b

def minimal(a, b):
    if a < b:
        return a
    return b

n = int(input())
angka = input().split()

maks = -100000
minim = 100000
for x in angka:
    nilai = int(x)
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)

print(maks, minim)