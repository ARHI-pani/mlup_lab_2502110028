
import os

# Create project folders
os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Create sample input file
input_file = "data/input.txt"

with open(input_file, "w", encoding="utf-8") as f:
    f.write("Welcome to IT10 Project!\n")
    f.write("README and Tidy Exercise.\n")
    f.write("Python file handling example.")

# Read input file
try:
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    print("Input file read successfully!")

    # Generate output file
    output_file = "reports/output.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("IT10 Project Output\n")
        f.write("-------------------\n")
        f.write(content)

    print("Output file created successfully!")

    # Generate README file
    readme = """# IT10 - README & Tidy

## Project Description
A simple Python project demonstrating file handling
and repository organization.

## Folder Structure
- main.py
- README.md
- data/input.txt
- reports/output.txt

## How to Run
Run the following command:

python main.py

## Sample Input
data/input.txt

## Output
reports/output.txt
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    print("README.md created successfully!")
    print("Project organized successfully!")

except FileNotFoundError:
    print("Error: Input file not found.")

except PermissionError:
    print("Error: Permission denied.")

except OSError as error:
    print("File error:", error)
