# file: ex_11_04_csv_gradescsv_grades.py
import csv


def load_grades(filename: str) -> dict[str, list[float]]:
    """Load grades from a CSV file.

    Returns:
        dict mapping student name -> list of grades as floats
    """
    grades = {}
    with open(filename, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name   = row["name"]
            scores = [float(v) for k, v in row.items() if k != "name"]
            grades[name] = scores
    return grades


def write_report(grades: dict[str, list[float]], filename: str) -> None:
    """Write a grade summary CSV sorted by average (highest first)."""
    averages = {name: sum(scores) / len(scores)
                for name, scores in grades.items()}
    sorted_avgs = sorted(averages.items(), key=lambda x: x[1], reverse=True)

    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "average"])
        writer.writeheader()
        for name, avg in sorted_avgs:
            writer.writerow({"name": name, "average": round(avg, 2)})


if __name__ == "__main__":
    grades = load_grades("grades.csv")

    averages = {name: sum(scores) / len(scores)
                for name, scores in grades.items()}
    sorted_avgs = sorted(averages.items(), key=lambda x: x[1], reverse=True)

    print("Grade averages:")
    for name, avg in sorted_avgs:
        print(f"  {name:<8}{avg:.2f}")

    write_report(grades, "grade_report.csv")
    print("\nReport written to grade_report.csv")
