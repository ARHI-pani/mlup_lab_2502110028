
import os
import re
import csv

os.makedirs("data", exist_ok=True)

input_file = "data/shift_log.txt"
report_file = "data/report.txt"
reject_file = "data/rejects.csv"

valid_records = []
rejected_records = []

# Regex pattern:
# Field 1: Work order must be WO followed by digits
# Field 2: Description
# Field 3: Time
pattern = re.compile(
    r"^\s*(WO\d+)\s*,\s*([^,]+?)\s*,\s*(\S+)\s*$"
)

# READ → PARSE → VALIDATE
with open(input_file, "r") as file:

    for line_number, line in enumerate(file, start=1):

        line = line.strip()

        if not line:
            rejected_records.append(
                [line_number, line, "Empty line"]
            )
            continue

        # OLD SPLIT PARSING METHOD (kept for comparison)
        # parts = line.split(",")
        #
        # if len(parts) != 3:
        #     rejected_records.append(
        #         [line_number, line, "Incorrect number of fields"]
        #     )
        #     continue
        #
        # wo, description, time = [p.strip() for p in parts]
        #
        # The regex method below survived more test lines
        # because it handles flexible spacing around separators
        # and validates the work order shape during parsing.

        # NEW REGEX PARSING METHOD
        match = pattern.match(line)

        if not match:
            rejected_records.append(
                [line_number, line, "Invalid record format"]
            )
            continue

        wo, description, time = match.groups()

        if not description or any(ch in description for ch in "!@#$%"):
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


# AGGREGATE
total_valid = len(valid_records)
total_rejected = len(rejected_records)


# WRITE HUMAN REPORT
with open(report_file, "w") as file:

    file.write("=" * 65 + "\n")
    file.write("                 SHIFT LOG REPORT\n")
    file.write("=" * 65 + "\n")

    file.write(
        f"{'WORK ORDER':<15}{'DESCRIPTION':<35}{'TIME':<15}\n"
    )

    file.write("-" * 65 + "\n")

    for wo, description, time in valid_records:
        file.write(
            f"{wo:<15}{description:<35}{time:<15}\n"
        )

    file.write("-" * 65 + "\n")
    file.write(f"Total valid records   : {total_valid}\n")
    file.write(f"Total rejected records: {total_rejected}\n")
    file.write("=" * 65 + "\n")


# WRITE REJECTS CSV
with open(reject_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Line Number", "Rejected Line", "Reason"])

    writer.writerows(rejected_records)


# DISPLAY SUMMARY
print("REGEX PIPELINE COMPLETED")
print("------------------------")
print("Valid records   :", total_valid)
print("Rejected records:", total_rejected)
print("Report saved to :", report_file)
print("Rejects saved to:", reject_file)
