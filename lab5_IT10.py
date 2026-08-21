logs = [
    "P-101, 25.5, A",
    "P-102, 24.8, B ",
    " P-103, 26.1, A",
    "P-104 , 25.2 , C",
    "P-105, 24.9,A",
    " P-106, 26.4, B",
    "P-107,25.7 , C",
    "P-108 , 25.1,A ",
    "P-109, 26.0, B",
    "P-110 ,24.6,C"
]

diameters = []

for log in logs:
    parts = log.split(",")
    dia = float(parts[1].strip())
    diameters.append(dia)

print("Count:", len(diameters))
print("Average:", sum(diameters) / len(diameters))
print("Min:", min(diameters))
print("Max:", max(diameters))




