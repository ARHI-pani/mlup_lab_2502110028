
import os
import re
import csv
from datetime import datetime

# FOLDER AND FILE PATHS
data_folder = "data"
history_file = os.path.join(data_folder, "run_history.csv")
plant_report = os.path.join(data_folder, "plant_summary.txt")

os.makedirs(data_folder, exist_ok=True)

# REGEX PATTERN
pattern = re.compile(
    r"^\s*(WO\d+)\s*,\s*([^,]+?)\s*,\s*(\S+)\s*$"
)

# PLANT TOTALS
plant_valid = 0
plant_rejected = 0
plant_processed = 0

plant_records = []
plant_rejects = []

# GET ALL TXT FILES
txt_files = sorted(
    f for f in os.listdir(data_folder)
    if f.lower().endswith(".txt")
    and os.path.isfile(os.path.join(data_folder, f))
    and f != os.path.basename(plant_report)
)

# CREATE HISTORY FILE WITH HEADER IF NEEDED
if not os.path.exists(history_file):
    with open(history_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp",
            "File Name",
            "Records Processed",
            "Rejects"
        ])

# PROCESS EACH FILE
for filename in txt_files:

    input_path = os.path.join(data_folder, filename)

    valid_records = []
    rejected_records = []

    print("\nProcessing:", filename)

    # READ AND VALIDATE
    with open(input_path, "r") as file:

        for line_number, line in enumerate(file, start=1):

            line = line.strip()

            if not line:
                rejected_records.append(
                    [line_number, line, "Empty line"]
                )
                continue

            match = pattern.match(line)

            if not match:
                rejected_records.append(
                    [line_number, line, "Invalid record format"]
                )
                continue

            wo, description, time = match.groups()

            if any(ch in description for ch in "!@#$%"):
                rejected_records.append(
                    [line_number, line, "Invalid description"]
                )
                continue

            if time in ["ERROR", "???", "-999"]:
                rejected_records.append(
                    [line_number, line, "Invalid time"]
                )
                continue

            valid_records.append([wo, description, time])

    # CALCULATE FILE TOTALS
    processed = len(valid_records) + len(rejected_records)
    rejects = len(rejected_records)

    plant_processed += processed
    plant_valid += len(valid_records)
    plant_rejected += rejects

    plant_records.extend(valid_records)

    plant_rejects.extend(
        [[filename] + record for record in rejected_records]
    )

    # GENERATE INDIVIDUAL REPORT
    report_name = filename[:-4] + "_report.txt"
    report_path = os.path.join(data_folder, report_name)

    with open(report_path, "w") as report:

        report.write("=" * 70 + "\n")
        report.write("              INDIVIDUAL SHIFT REPORT\n")
        report.write("=" * 70 + "\n")

        report.write("Source file: " + filename + "\n\n")

        report.write(
            f"{'WORK ORDER':<15}{'DESCRIPTION':<40}{'TIME':<15}\n"
        )

        report.write("-" * 70 + "\n")

        for wo, description, time in valid_records:
            report.write(
                f"{wo:<15}{description:<40}{time:<15}\n"
            )

        report.write("-" * 70 + "\n")
        report.write(f"Records processed: {processed}\n")
        report.write(f"Valid records    : {len(valid_records)}\n")
        report.write(f"Rejected records : {rejects}\n")

    # APPEND RUN HISTORY
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(history_file, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            filename,
            processed,
            rejects
        ])

    print("Valid records:", len(valid_records))
    print("Rejected records:", rejects)
    print("Report created:", report_name)


# GENERATE COMBINED PLANT SUMMARY
with open(plant_report, "w") as report:

    report.write("=" * 75 + "\n")
    report.write("                 PLANT-WIDE SHIFT SUMMARY\n")
    report.write("=" * 75 + "\n")

    report.write(
        f"{'WORK ORDER':<15}{'DESCRIPTION':<45}{'TIME':<15}\n"
    )

    report.write("-" * 75 + "\n")

    for wo, description, time in plant_records:
        report.write(
            f"{wo:<15}{description:<45}{time:<15}\n"
        )

    report.write("-" * 75 + "\n")

    report.write(f"Total files processed : {len(txt_files)}\n")
    report.write(f"Total records processed: {plant_processed}\n")
    report.write(f"Total valid records   : {plant_valid}\n")
    report.write(f"Total rejected records: {plant_rejected}\n")

    report.write("=" * 75 + "\n")

# FINAL CONSOLE SUMMARY
print("\n" + "=" * 45)
print("       BATCH JOB COMPLETED")
print("=" * 45)

print("Files processed :", len(txt_files))
print("Records processed:", plant_processed)
print("Valid records   :", plant_valid)
print("Rejected records:", plant_rejected)

print("\nPlant report:", plant_report)
print("Run history :", history_file)
