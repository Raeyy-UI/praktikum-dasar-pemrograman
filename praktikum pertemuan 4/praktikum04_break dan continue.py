for angka in range(1, 11):
    if angka % 2 == 0:
        continue
    print(angka, end=" ")
print("\n")

for angka in range(1, 201):
    if angka % 4 == 0 and angka % 6 == 0:
        print(f"Bilangan pertama yang habis dibagi 4 dan 6 adalah {angka}")
        break