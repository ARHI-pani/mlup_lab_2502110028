
import os

# Create required folders
os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)


# Create sample input
def create_sample():
    with open("data/input.txt", "w", encoding="utf-8") as file:
        file.write("Apple\n")
        file.write("Banana\n")
        file.write("Orange\n")


# Process input data
def process_data():
    try:
        with open("data/input.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        items = [line.strip() for line in lines if line.strip()]
        report = "Sample Report\n"
        report += "-------------\n"
        report += f"Total items: {len(items)}\n"

        for item in items:
            report += f"- {item}\n"

        return report

    except FileNotFoundError:
        return "Error: Input file not found."


# Test function with normal and hostile inputs
def run_tests():
    print("Running tests...")

    # Normal input test
    result = process_data()
    assert "Total items: 3" in result
    print("Test 1 passed: Normal input")

    # Hostile input test
    with open("data/input.txt", "w", encoding="utf-8") as file:
        file.write("\n\n")

    result = process_data()
    assert "Total items: 0" in result
    print("Test 2 passed: Empty input")

    print("All tests passed!")


# Main program
def main():
    create_sample()

    report = process_data()

    # Save sample report
    with open("reports/example_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print("\nReport generated successfully!")
    print(report)

    # Create README
    readme = """# IT6 - The Handover Pack

## Project Description
A simple Python tool to read input data and
generate reports.

## How to Run
python main.py

## How to Test
python main.py --test

## Sample Report
reports/example_report.txt

## Limitations
- Supports only text input files.
- Does not support Excel or PDF files.
- Does not use a database.
- Does not provide a graphical interface.
- Requires Python 3 to run.
"""

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme)

    print("README.md created successfully!")


if __name__ == "__main__":
    import sys

    if "--test" in sys.argv:
        create_sample()
        run_tests()
    else:
        main()
