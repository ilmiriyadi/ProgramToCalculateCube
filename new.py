def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Input panjang persegi: "))
width = float(input("Input lebar persegi: "))
area, perimeter = calculate_area_and_perimeter(length, width)

print("Program Hitung Luas dan Keliling Persegi Panjang")
print("=====================================================")
print()
print("Nama: [M. Riyadi Ilmi]")
print("NIM : [C030323093]")
print("Kelas: [TI_B]")
print()
print(f"Panjang: {length}")
print(f"Lebar: {width}")
print(f"Luas Persegi: {area}")
print(f"Keliling Persegi: {perimeter}")
