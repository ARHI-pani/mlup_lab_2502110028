
import os

# Create data folder if it does not exist
os.makedirs("data", exist_ok=True)

# Create 15 shift log records (including 3 filthy records)
records = [
    "WO01, Machine running normally, 08:00",
    "WO02, Oil level checked, 08:15",
    "WO03, Temperature within limits, 08:30",
    "WO04, Conveyor belt inspected, 08:45",
    "WO05, Motor functioning properly, 09:00",
    "WO06, Safety guard checked, 09:15",
    "WO07, Production running smoothly, 09:30",
    "WO08, !!! DIRTY DATA !!!, ERROR",
    "WO09, Filter cleaned, 10:00",
    "WO10, Pressure checked, 10:15",
    "WO11, @@@#$%% INVALID RECORD, ???",
    "WO12, Electrical connections checked, 10:45",
    "WO13, Machine stopped unexpectedly, 11:00",
    "WO14, NULL, -999",
    "WO15, Shift completed successfully, 11:30"
]

# Write records to the file
with open("data/shift_log.txt", "w") as file:
    for record in records:
        file.write(record + "\n")

# Read the file and count lines
with open("data/shift_log.txt", "r") as file:
    lines = file.readlines()

print("Shift log created successfully!")
print("Total number of records:", len(lines))
