import random

accept = 0
rework = 0
scrap = 0

for _ in range(100):
    diameter = random.uniform(24.90, 25.10)

    if 24.95 <= diameter <= 25.05:
        bin_name = "ACCEPT"
        accept += 1
    elif 24.90 <= diameter < 24.95 or 25.05 < diameter <= 25.10:
        bin_name = "REWORK"
        rework += 1
    else:
        bin_name = "SCRAP"
        scrap += 1

    print(f"{diameter:.2f} mm -> {bin_name}")

print("\nShift report")
print(f"ACCEPT: {accept}")
print(f"REWORK: {rework}")
print(f"SCRAP: {scrap}")

print("\nSame code, ten times the work, zero extra effort.")