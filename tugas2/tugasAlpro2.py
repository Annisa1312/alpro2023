
nilai = int(input("masukan nilai:"))

if nilai >= 85:
    grade ="A"
elif nilai >= 80:
    grade="A-"
elif nilai >= 75:
    grade ="B+"
elif nilai >= 70:
    grade="B"
elif nilai >= 65:
    grade ="B-"
elif nilai >= 60:
    grade ="C+"
elif nilai >= 55:
    grade ="C"
elif nilai >= 50:
    grade ="C-"
elif nilai >= 40:
    grade ="D-"
else:
    grade ="E"

print(F"grade anda adalah {grade}")
