import random

mode = input("Operator mode (halt/skip): ").strip().lower()

accept = rework = scrap = 0
inspected = 0

for _ in range(100):
    diameter = random.uniform(24.90, 25.10)
    inspected += 1

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

    if bin_name == "SCRAP":
        if mode == "halt":
            print(f"\nHALT: SCRAP detected after {inspected} parts inspected.")
            break
        elif mode == "skip":
            print("SKIP: SCRAP logged; continuing batch.")
            continue
    elif mode not in ("halt", "skip"):
        print("Invalid mode. Use 'halt' or 'skip'.")
        break

print("\nShift report")
print(f"Inspected: {inspected}")
print(f"ACCEPT: {accept}")
print(f"REWORK: {rework}")
print(f"SCRAP: {scrap}")