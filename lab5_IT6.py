day_logs = [
    "P-101,25.5,A",
    "P-102,24.8,B",
    "P-103,26.1,C",
    "P-104,25.2,A",
    "P-105,24.9,C"
]

night_logs = [
    "P-103,26.0,C",
    "P-106,25.7,A",
    "P-107,24.6,C",
    "P-108,25.3,A",
    "P-101,25.4,C"
]

def parse_shift(logs):
    total = 0
    accepted = 0
    scrap_parts = []

    for log in logs:
        part_code, dia, status = log.split(",")

        part_code = part_code.strip()
        dia = float(dia.strip())
        status = status.strip()

        total += 1

        if status == "A":
            accepted += 1
        elif status == "C":
            scrap_parts.append(part_code)

    accept_rate = (accepted / total) * 100

    return accept_rate, scrap_parts


day_rate, day_scrap = parse_shift(day_logs)
night_rate, night_scrap = parse_shift(night_logs)

print("Day accept rate:", day_rate, "%")
print("Night accept rate:", night_rate, "%")

day_set = set(day_scrap)
night_set = set(night_scrap)

both_scrapped = day_set & night_set
unique_to_one = day_set ^ night_set

print("Scrapped in both shifts:", both_scrapped)
print("Scrapped in only one shift:", unique_to_one)