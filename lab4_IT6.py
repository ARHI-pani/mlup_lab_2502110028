import random

consecutive_accepts = 0
attempts = 0
MAX_ATTEMPTS = 500

while consecutive_accepts < 5 and attempts < MAX_ATTEMPTS:
    diameter = random.uniform(24.90, 25.10)
    attempts += 1

    if 24.95 <= diameter <= 25.05:
        consecutive_accepts += 1
        print(f"{diameter:.2f} mm -> ACCEPT ({consecutive_accepts}/5 consecutive)")
    else:
        consecutive_accepts = 0
        if diameter < 24.95 or diameter > 25.05:
            bin_name = "REWORK" if 24.90 <= diameter <= 25.10 else "SCRAP"
            print(f"{diameter:.2f} mm -> {bin_name}")

if consecutive_accepts == 5:
    print(f"\nTarget achieved: five consecutive ACCEPTs in {attempts} parts.")
else:
    print(f"\nSafety cap reached: {attempts} attempts without five consecutive ACCEPTs.")



