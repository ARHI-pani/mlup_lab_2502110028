logs = [
    "P-101, 25.5, A",
    "P-102, 24.8, B",
    "P-103, 26.1, A",
    "P-104, 25.2, C",
    "P-105, 24.9, A",
    "P-106, 26.4, B",
    "P-107, 25.7, C",
    "P-108, 25.1, A",
    "P-109, 26.0, B",
    "P-110, 24.6, C"
]

accepted = []
rework = []
scrap = []
scrap_parts = []

for log in logs:
    part_code, dia, status = log.split(",")

    part_code = part_code.strip()
    dia = float(dia.strip())
    status = status.strip()

    if status == "A":
        accepted.append(dia)
    elif status == "B":
        rework.append(dia)
    elif status == "C":
        scrap.append(dia)
        scrap_parts.append(part_code)

print("Accepted count:", len(accepted))
print("Rework count:", len(rework))
print("Scrap count:", len(scrap))

if accepted:
    print("Accepted average:", sum(accepted) / len(accepted))
else:
    print("Accepted average: No accepted parts")

print("Scrapped part codes:", scrap_parts)