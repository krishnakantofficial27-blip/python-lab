"""Calculate and display a student's result and grade."""

PASS_MARK = 40.0
def grade_for_average(average: float) -> str:
    """Return the letter grade for an average mark."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"

def read_subject_count() -> int:
    """Read a positive number of subjects."""
    while True:
        try:
            count = int(input("Enter number of subjects: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if count > 0:
            return count
        print("Number of subjects must be positive.")
def read_mark(subject_number: int) -> float:
    """Read one subject mark in the inclusive range 0 to 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for Subject {subject_number}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= mark <= 100:
            return mark
        print("Marks must be between 0 and 100.")

def main() -> None:
    """Collect marks and display the student's grade report."""
    print("========== STUDENT GRADING AUTOMATION ==========")
    student_name = input("Enter Student Name: ").strip()
    usn = input("Enter USN: ").strip()
    subject_count = read_subject_count()
    marks = [read_mark(index) for index in range(1, subject_count + 1)]

    total = sum(marks)
    average = total / subject_count
    passed = all(mark >= PASS_MARK for mark in marks)
    result = "PASS" if passed else "FAIL"
    grade = grade_for_average(average) if passed else "F"

    print("\n================ GRADE REPORT =================")
    print(f"Student Name : {student_name}")
    print(f"USN          : {usn}")
    print(f"Total Marks  : {total:.2f} / {subject_count * 100}")
    print(f"Average      : {average:.2f}")
    print(f"Result       : {result}")
    print(f"Grade        : {grade}")
    print("===============================================")

if __name__ == "__main__":
    main()

