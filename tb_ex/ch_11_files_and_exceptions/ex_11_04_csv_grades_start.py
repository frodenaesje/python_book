# file: ex_11_04_csv_gradescsv_grades_start.py
import csv


def load_grades(filename: str) -> dict[str, list[float]]:
    """Load grades from a CSV file.

    Returns:
        dict mapping student name -> list of grades as floats
        Example: {"Alice": [5.5, 6.0, 4.5, 5.0], ...}
    """
    # TODO: open the file and use csv.DictReader to read rows
    # TODO: for each row, extract the name and convert remaining values to floats
    # TODO: return a dict[str, list[float]]
    pass


def write_report(grades: dict[str, list[float]], filename: str) -> None:
    """Write a grade summary CSV sorted by average (highest first).

    Columns: name, average
    """
    # TODO: compute the average for each student
    # TODO: sort by average descending
    # TODO: write to CSV using csv.DictWriter with fieldnames ["name", "average"]
    pass


if __name__ == "__main__":
    grades = load_grades("grades.csv")

    # TODO: print averages for each student (sorted highest first)

    write_report(grades, "grade_report.csv")
    print("\nReport written to grade_report.csv")
