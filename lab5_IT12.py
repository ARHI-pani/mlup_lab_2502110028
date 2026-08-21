raw_line = "P-101,25.5,A"

part_code, dia, shift = raw_line.split(",")

dia = float(dia)

print("Part Code:", part_code)
print("Diameter:", dia)
print("Shift:", shift)
print("Diameter + 0.01:", dia + 0.01)